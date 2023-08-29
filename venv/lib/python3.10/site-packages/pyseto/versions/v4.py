import hashlib
import hmac
from secrets import token_bytes
from typing import Any, Union

from cryptography.hazmat.primitives import serialization
from cryptography.hazmat.primitives.asymmetric.ed25519 import (
    Ed25519PrivateKey,
    Ed25519PublicKey,
)

from ..exceptions import DecryptError, SignError, VerifyError
from ..key_sodium import SodiumKey
from ..utils import base64url_encode, pae


class V4Local(SodiumKey):
    """
    The key object for v4.local.
    """

    _VERSION = 4
    _TYPE = "local"

    def __init__(self, key: Union[str, bytes]):
        super().__init__(key)
        if len(self._key) > 64:
            raise ValueError("key length must be up to 64 bytes.")
        return

    def to_paserk_id(self) -> str:
        h = "k4.lid."
        p = self.to_paserk()
        b = hashlib.blake2b(digest_size=33)
        b.update((h + p).encode("utf-8"))
        d = b.digest()
        return h + base64url_encode(d).decode("utf-8")

    def encrypt(
        self,
        payload: bytes,
        footer: bytes = b"",
        implicit_assertion: bytes = b"",
        nonce: bytes = b"",
    ) -> bytes:
        if nonce:
            if len(nonce) != 32:
                raise ValueError("nonce must be 32 bytes long.")
        else:
            nonce = token_bytes(32)
        tmp = self._generate_hash(self._key, b"paseto-encryption-key" + nonce, 56)
        ek = tmp[0:32]
        n2 = tmp[32:]
        ak = self._generate_hash(self._key, b"paseto-auth-key-for-aead" + nonce, 32)

        c = self._encrypt(ek, n2, payload)
        pre_auth = pae([self.header, nonce, c, footer, implicit_assertion])
        t = self._generate_hash(ak, pre_auth, 32)
        token = self._header + base64url_encode(nonce + c + t)
        if footer:
            token += b"." + base64url_encode(footer)
        return token

    def decrypt(self, payload: bytes, footer: bytes = b"", implicit_assertion: bytes = b"") -> bytes:
        n = payload[0:32]
        c = payload[32 : len(payload) - 32]
        t = payload[-32:]
        tmp = self._generate_hash(self._key, b"paseto-encryption-key" + n, 56)
        ek = tmp[0:32]
        n2 = tmp[32:]
        ak = self._generate_hash(self._key, b"paseto-auth-key-for-aead" + n, 32)
        pre_auth = pae([self.header, n, c, footer, implicit_assertion])
        t2 = self._generate_hash(ak, pre_auth, 32)
        if not hmac.compare_digest(t, t2):
            raise DecryptError("Failed to decrypt.")
        return self._decrypt(ek, n2, c)


class V4Public(SodiumKey):
    """
    The key object for v4.public.
    """

    _VERSION = 4
    _TYPE = "public"

    def __init__(self, key: Any):
        super().__init__(key)
        self._sig_size = 64

        if not isinstance(self._key, (Ed25519PublicKey, Ed25519PrivateKey)):
            raise ValueError("The key is not Ed25519 key.")

        if isinstance(self._key, Ed25519PublicKey):
            self._is_secret = False
        return

    # @classmethod
    # def from_public_bytes(cls, key: bytes):
    #     try:
    #         k = Ed25519PublicKey.from_public_bytes(key)
    #     except Exception as err:
    #         raise ValueError("Invalid bytes for the key.") from err
    #     return cls(k)

    def to_paserk_id(self) -> str:
        p = self.to_paserk()
        h = "k4.pid." if isinstance(self._key, Ed25519PublicKey) else "k4.sid."
        b = hashlib.blake2b(digest_size=33)
        b.update((h + p).encode("utf-8"))
        d = b.digest()
        return h + base64url_encode(d).decode("utf-8")

    def to_peer_paserk_id(self) -> str:
        if not self._is_secret:
            return ""

        h1 = "k4.public."
        pub = self._key.public_key().public_bytes(
            encoding=serialization.Encoding.Raw,
            format=serialization.PublicFormat.Raw,
        )
        p = h1 + base64url_encode(pub).decode("utf-8")

        h2 = "k4.pid."
        b = hashlib.blake2b(digest_size=33)
        b.update((h2 + p).encode("utf-8"))
        d = b.digest()
        return h2 + base64url_encode(d).decode("utf-8")

    def sign(self, payload: bytes, footer: bytes = b"", implicit_assertion: bytes = b"") -> bytes:
        if isinstance(self._key, Ed25519PublicKey):
            raise ValueError("A public key cannot be used for signing.")

        m2 = pae([self.header, payload, footer, implicit_assertion])
        try:
            return self._key.sign(m2)
        except Exception as err:
            raise SignError("Failed to sign.") from err

    def verify(self, payload: bytes, footer: bytes = b"", implicit_assertion: bytes = b""):
        if len(payload) <= self._sig_size:
            raise ValueError("Invalid payload.")

        sig = payload[-self._sig_size :]
        m = payload[: len(payload) - self._sig_size]
        k = self._key if isinstance(self._key, Ed25519PublicKey) else self._key.public_key()
        m2 = pae([self.header, m, footer, implicit_assertion])
        try:
            k.verify(sig, m2)
        except Exception as err:
            raise VerifyError("Failed to verify.") from err
        return m
