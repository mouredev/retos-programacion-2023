import hashlib
from secrets import token_bytes
from typing import Any, Union

from Cryptodome.Cipher import ChaCha20
from cryptography.hazmat.primitives import serialization
from cryptography.hazmat.primitives.asymmetric.ed25519 import (
    Ed25519PrivateKey,
    Ed25519PublicKey,
)
from cryptography.hazmat.primitives.asymmetric.x25519 import (
    X25519PrivateKey,
    X25519PublicKey,
)
from cryptography.hazmat.primitives.serialization import (
    Encoding,
    PublicFormat,
    load_pem_private_key,
    load_pem_public_key,
)
from passlib.hash import argon2

from .exceptions import DecryptError, EncryptError
from .key_interface import KeyInterface
from .utils import base64url_decode, base64url_encode


class SodiumKey(KeyInterface):
    """
    Sodium (v2, v4) PASETO key.
    """

    # _VERSION = 2 or 4
    # _TYPE = "local", "public" or "secret"

    def __init__(self, key: Any):
        super().__init__(self._VERSION, self._TYPE, key)
        return

    @classmethod
    def from_paserk(
        cls,
        paserk: str,
        wrapping_key: bytes = b"",
        password: bytes = b"",
        unsealing_key: bytes = b"",
    ) -> KeyInterface:
        if wrapping_key and password:
            raise ValueError("Only one of wrapping_key or password should be specified.")

        frags = paserk.split(".")
        if frags[0] != f"k{cls._VERSION}":
            raise ValueError(f"Invalid PASERK version: {frags[0]}.")

        if wrapping_key:
            # {local, secret}-wrap
            if len(frags) != 4:
                raise ValueError("Invalid PASERK format.")
            if frags[2] != "pie":
                raise ValueError(f"Unknown wrapping algorithm: {frags[2]}.")

            h = frags[0] + "." + frags[1] + ".pie."
            if frags[1] == "local-wrap":
                return cls(cls._decode_pie(h, wrapping_key, frags[3]))
            if frags[1] == "secret-wrap":
                k = cls._decode_pie(h, wrapping_key, frags[3])[0:32]
                return cls(Ed25519PrivateKey.from_private_bytes(k))
            raise ValueError(f"Invalid PASERK type: {frags[1]}.")

        if len(frags) != 3:
            raise ValueError("Invalid PASERK format.")

        if password:
            # {local, secret}-pw
            h = frags[0] + "." + frags[1] + "."
            if frags[1] == "local-pw":
                return cls(cls._decode_pbkw(h, password, frags[2]))
            if frags[1] == "secret-pw":
                k = cls._decode_pbkw(h, password, frags[2])[0:32]
                return cls(Ed25519PrivateKey.from_private_bytes(k))
            raise ValueError(f"Invalid PASERK type: {frags[1]}.")

        if unsealing_key:
            # seal
            h = frags[0] + "." + frags[1] + "."
            if frags[1] != "seal":
                raise ValueError(f"Invalid PASERK type: {frags[1]}.")
            if unsealing_key.startswith(b"-----BEGIN PRIVATE KEY"):
                sk = load_pem_private_key(unsealing_key, password=None)
            else:
                raise ValueError("Invalid or unsupported PEM format.")
            raw_key = sk.private_bytes(
                encoding=serialization.Encoding.Raw,
                format=serialization.PrivateFormat.Raw,
                encryption_algorithm=serialization.NoEncryption(),
            )
            k = cls._decode_pke(h, raw_key, frags[2])
            return cls(k)

        k = base64url_decode(frags[2])

        # local
        if cls._TYPE == "local":
            if frags[1] == "local":
                return cls(k)
            if frags[1] == "local-wrap":
                raise ValueError(f"{frags[1]} needs wrapping_key.")
            if frags[1] == "local-pw":
                raise ValueError(f"{frags[1]} needs password.")
            if frags[1] == "seal":
                raise ValueError(f"{frags[1]} needs unsealing_key.")
            raise ValueError(f"Invalid PASERK type: {frags[1]}.")

        # public, secret
        if frags[1] == "public":
            return cls(Ed25519PublicKey.from_public_bytes(k))
        if frags[1] == "secret":
            return cls(Ed25519PrivateKey.from_private_bytes(k[0:32]))
        if frags[1] == "secret-wrap":
            raise ValueError(f"{frags[1]} needs wrapping_key.")
        if frags[1] == "secret-pw":
            raise ValueError(f"{frags[1]} needs password.")
        raise ValueError(f"Invalid PASERK type: {frags[1]}.")

    def to_paserk(
        self,
        wrapping_key: Union[bytes, str] = b"",
        password: Union[bytes, str] = b"",
        sealing_key: Union[bytes, str] = b"",
        iteration: int = 100000,
        memory_cost: int = 15 * 1024,
        time_cost: int = 2,
        parallelism: int = 1,
    ) -> str:
        if wrapping_key and password:
            raise ValueError("Only one of wrapping_key or password should be specified.")

        if wrapping_key:
            # local-wrap
            bkey = wrapping_key if isinstance(wrapping_key, bytes) else wrapping_key.encode("utf-8")
            if self.purpose == "local":
                h = f"k{self.version}.local-wrap.pie."
                return h + self._encode_pie(h, bkey, self._key)

            # secret-wrap
            if not isinstance(self._key, Ed25519PrivateKey):
                raise ValueError("Public key cannot be wrapped.")

            h = f"k{self.version}.secret-wrap.pie."
            priv = self._key.private_bytes(
                encoding=serialization.Encoding.Raw,
                format=serialization.PrivateFormat.Raw,
                encryption_algorithm=serialization.NoEncryption(),
            )
            pub = self._key.public_key().public_bytes(
                encoding=serialization.Encoding.Raw,
                format=serialization.PublicFormat.Raw,
            )
            return h + self._encode_pie(h, bkey, priv + pub)

        if password:
            # local-pw
            bpw = password if isinstance(password, bytes) else password.encode("utf-8")
            if self.purpose == "local":
                h = f"k{self.version}.local-pw."
                return h + self._encode_pbkw(h, bpw, self._key, memory_cost, time_cost, parallelism)

            # secret-pw
            if not isinstance(self._key, Ed25519PrivateKey):
                raise ValueError("Public key cannot be wrapped.")

            h = f"k{self.version}.secret-pw."
            priv = self._key.private_bytes(
                encoding=serialization.Encoding.Raw,
                format=serialization.PrivateFormat.Raw,
                encryption_algorithm=serialization.NoEncryption(),
            )
            pub = self._key.public_key().public_bytes(
                encoding=serialization.Encoding.Raw,
                format=serialization.PublicFormat.Raw,
            )
            return h + self._encode_pbkw(h, bpw, priv + pub, memory_cost, time_cost, parallelism)

        if sealing_key:
            # seal
            bkey = sealing_key if isinstance(sealing_key, bytes) else sealing_key.encode("utf-8")
            if self.purpose != "local":
                raise ValueError("Key sealing can only be used for local key.")
            if bkey.startswith(b"-----BEGIN PUBLIC KEY"):
                pk = load_pem_public_key(bkey)
            else:
                raise ValueError("Invalid or unsupported PEM format.")
            raw_key = pk.public_bytes(
                encoding=serialization.Encoding.Raw,
                format=serialization.PublicFormat.Raw,
            )
            h = f"k{self.version}.seal."
            return h + self._encode_pke(h, raw_key, self._key)

        # local
        if self.purpose == "local":
            h = f"k{self.version}.local."
            return h + base64url_encode(self._key).decode("utf-8")

        # public
        if isinstance(self._key, Ed25519PublicKey):
            h = f"k{self.version}.public."
            pub = self._key.public_bytes(
                encoding=serialization.Encoding.Raw,
                format=serialization.PublicFormat.Raw,
            )
            return h + base64url_encode(pub).decode("utf-8")

        # secret
        h = f"k{self.version}.secret."
        priv = self._key.private_bytes(
            encoding=serialization.Encoding.Raw,
            format=serialization.PrivateFormat.Raw,
            encryption_algorithm=serialization.NoEncryption(),
        )
        pub = self._key.public_key().public_bytes(
            encoding=serialization.Encoding.Raw,
            format=serialization.PublicFormat.Raw,
        )
        return h + base64url_encode(priv + pub).decode("utf-8")

    @classmethod
    def _encode_pie(cls, header: str, wrapping_key: bytes, ptk: bytes) -> str:
        h = header.encode("utf-8")
        n = token_bytes(32)
        x = cls._generate_hash(wrapping_key, b"\x80" + n, 56)
        ek = x[0:32]
        n2 = x[32:]
        ak = cls._generate_hash(wrapping_key, b"\x81" + n, 32)
        c = cls._encrypt(ek, n2, ptk)
        t = cls._generate_hash(ak, h + n + c, 32)
        return base64url_encode(t + n + c).decode("utf-8")

    @classmethod
    def _decode_pie(cls, header: str, wrapping_key: bytes, data: str) -> bytes:
        h = header.encode("utf-8")
        d = base64url_decode(data)
        t = d[0:32]
        n = d[32:64]
        c = d[64:]
        ak = cls._generate_hash(wrapping_key, b"\x81" + n, 32)

        t2 = cls._generate_hash(ak, h + n + c, 32)
        if t != t2:
            raise DecryptError("Failed to unwrap a key.")

        x = cls._generate_hash(wrapping_key, b"\x80" + n, 56)
        ek = x[0:32]
        n2 = x[32:]
        return cls._decrypt(ek, n2, c)

    @classmethod
    def _encode_pbkw(
        cls,
        header: str,
        password: bytes,
        ptk: bytes,
        memory_cost: int,
        time_cost: int,
        parallelism: int,
    ) -> str:
        h = header.encode("utf-8")
        s = token_bytes(16)
        argon2_k = argon2.using(
            salt=s,
            memory_cost=memory_cost,
            time_cost=time_cost,
            parallelism=parallelism,
            digest_size=32,
        ).hash(password)
        frags = argon2_k.split("$")
        key = base64url_decode(frags[5])
        ek = cls._digest(b"\xff" + key, 32)
        ak = cls._digest(b"\xfe" + key, 32)
        n = token_bytes(24)
        edk = cls._encrypt(ek, n, ptk)
        mem = (memory_cost * 1024).to_bytes(8, byteorder="big")
        time = time_cost.to_bytes(4, byteorder="big")
        para = parallelism.to_bytes(4, byteorder="big")
        t = cls._generate_hash(ak, h + s + mem + time + para + n + edk, 32)
        return base64url_encode(s + mem + time + para + n + edk + t).decode("utf-8")

    @classmethod
    def _decode_pbkw(cls, header: str, password: bytes, data: str) -> bytes:
        h = header.encode("utf-8")
        d = base64url_decode(data)

        s = d[0:16]
        mem = d[16:24]
        time = d[24:28]
        para = d[28:32]
        n = d[32:56]
        edk = d[56 : len(d) - 32]
        t = d[-32:]
        memory_cost = int.from_bytes(mem, byteorder="big")
        time_cost = int.from_bytes(time, byteorder="big")
        parallelism = int.from_bytes(para, byteorder="big")
        argon2_k = argon2.using(
            salt=s,
            memory_cost=int(memory_cost / 1024),
            time_cost=time_cost,
            parallelism=parallelism,
            digest_size=32,
        ).hash(password)
        frags = argon2_k.split("$")
        k = base64url_decode(frags[5])
        ak = cls._digest(b"\xfe" + k, 32)
        t2 = cls._generate_hash(ak, h + s + mem + time + para + n + edk, 32)
        if t != t2:
            raise DecryptError("Failed to unwrap a key.")

        ek = cls._digest(b"\xff" + k, 32)
        return cls._decrypt(ek, n, edk)

    @classmethod
    def _encode_pke(
        cls,
        header: str,
        sealing_key: bytes,
        ptk: bytes,
    ) -> str:
        h = header.encode("utf-8")

        xpk = X25519PublicKey.from_public_bytes(sealing_key)
        esk = X25519PrivateKey.generate()
        epk = esk.public_key().public_bytes(Encoding.Raw, PublicFormat.Raw)
        xk = esk.exchange(xpk)

        ek = cls._digest(b"\x01" + h + xk + epk + sealing_key, 32)
        ak = cls._digest(b"\x02" + h + xk + epk + sealing_key, 32)
        n = cls._digest(epk + sealing_key, 24)

        edk = cls._encrypt(ek, n, ptk)
        t = cls._generate_hash(ak, h + epk + edk, 32)
        return base64url_encode(t + epk + edk).decode("utf-8")

    @classmethod
    def _decode_pke(cls, header: str, unsealing_key: bytes, data: str) -> bytes:
        h = header.encode("utf-8")
        d = base64url_decode(data)

        t = d[0:32]
        epk = d[32:64]
        edk = d[64:]

        xsk = X25519PrivateKey.from_private_bytes(unsealing_key)
        xpk = xsk.public_key().public_bytes(Encoding.Raw, PublicFormat.Raw)
        xk = xsk.exchange(X25519PublicKey.from_public_bytes(epk))

        ak = cls._digest(b"\x02" + h + xk + epk + xpk, 32)
        t2 = cls._generate_hash(ak, h + epk + edk, 32)
        if t != t2:
            raise DecryptError("Failed to unseal a key.")

        ek = cls._digest(b"\x01" + h + xk + epk + xpk, 32)
        n = cls._digest(epk + xpk, 24)
        return cls._decrypt(ek, n, edk)

    @staticmethod
    def _generate_hash(key: bytes, msg: bytes, size: int) -> bytes:
        try:
            h = hashlib.blake2b(key=key, digest_size=size)
            h.update(msg)
            return h.digest()
        except Exception as err:
            raise EncryptError("Failed to generate hash.") from err

    @staticmethod
    def _digest(msg: bytes, size: int) -> bytes:
        h = hashlib.blake2b(digest_size=size)
        h.update(msg)
        return h.digest()

    @staticmethod
    def _encrypt(key: bytes, nonce: bytes, msg: bytes) -> bytes:
        try:
            cipher = ChaCha20.new(key=key, nonce=nonce)
            return cipher.encrypt(msg)
        except Exception as err:
            raise EncryptError("Failed to encrypt.") from err

    @staticmethod
    def _decrypt(key: bytes, nonce: bytes, msg: bytes) -> bytes:
        try:
            cipher = ChaCha20.new(key=key, nonce=nonce)
            return cipher.decrypt(msg)
        except Exception as err:
            raise DecryptError("Failed to decrypt.") from err
