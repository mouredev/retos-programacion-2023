import hashlib
from secrets import token_bytes
from typing import Any, Union

# from cryptography.hazmat.primitives.ciphers.aead import ChaCha20Poly1305
from Cryptodome.Cipher import ChaCha20_Poly1305
from cryptography.hazmat.primitives import serialization
from cryptography.hazmat.primitives.asymmetric.ed25519 import (
    Ed25519PrivateKey,
    Ed25519PublicKey,
)

from ..exceptions import DecryptError, EncryptError, SignError, VerifyError
from ..key_sodium import SodiumKey
from ..utils import base64url_encode, pae


class V2Local(SodiumKey):
    """
    The key object for v2.local.
    """

    _VERSION = 2
    _TYPE = "local"

    def __init__(self, key: Union[str, bytes]):
        super().__init__(key)
        if len(self._key) != 32:
            raise ValueError("key must be 32 bytes long.")
        return

    def to_paserk_id(self) -> str:
        h = "k2.lid."
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
        n = self._generate_nonce(nonce, payload)
        pre_auth = pae([self.header, n, footer])

        try:
            cipher = ChaCha20_Poly1305.new(key=self._key, nonce=n)
            cipher.update(pre_auth)
            c, tag = cipher.encrypt_and_digest(payload)
            token = self._header + base64url_encode(n + c + tag)
            if footer:
                token += b"." + base64url_encode(footer)
            return token
        except Exception as err:
            raise EncryptError("Failed to encrypt.") from err

    def decrypt(self, payload: bytes, footer: bytes = b"", implicit_assertion: bytes = b"") -> bytes:
        n = payload[0:24]
        c = payload[24 : len(payload) - 16]
        tag = payload[-16:]
        pre_auth = pae([self.header, n, footer])

        try:
            cipher = ChaCha20_Poly1305.new(key=self._key, nonce=n)
            cipher.update(pre_auth)
            return cipher.decrypt_and_verify(c, tag)
        except Exception as err:
            raise DecryptError("Failed to decrypt.") from err

    @staticmethod
    def _generate_nonce(key: bytes, msg: bytes) -> bytes:
        if key:
            if len(key) != 24:
                raise ValueError("nonce must be 24 bytes long.")
        else:
            key = token_bytes(24)

        try:
            h = hashlib.blake2b(key=key, digest_size=24)
            h.update(msg)
            return h.digest()
        except Exception as err:
            raise EncryptError("Failed to generate internal nonce.") from err


class V2Public(SodiumKey):
    """
    The key object for v2.public.
    """

    _VERSION = 2
    _TYPE = "public"

    def __init__(self, key: Any):
        super().__init__(key)
        self._sig_size = 64

        if not isinstance(self._key, (Ed25519PublicKey, Ed25519PrivateKey)):
            raise ValueError("The key is not Ed25519 key.")

        if isinstance(self._key, Ed25519PublicKey):
            self._is_secret = False
        return

    def to_paserk_id(self) -> str:
        p = self.to_paserk()
        h = "k2.pid." if isinstance(self._key, Ed25519PublicKey) else "k2.sid."
        b = hashlib.blake2b(digest_size=33)
        b.update((h + p).encode("utf-8"))
        d = b.digest()
        return h + base64url_encode(d).decode("utf-8")

    def to_peer_paserk_id(self) -> str:
        if not self._is_secret:
            return ""

        h1 = "k2.public."
        pub = self._key.public_key().public_bytes(
            encoding=serialization.Encoding.Raw,
            format=serialization.PublicFormat.Raw,
        )
        p = h1 + base64url_encode(pub).decode("utf-8")

        h2 = "k2.pid."
        b = hashlib.blake2b(digest_size=33)
        b.update((h2 + p).encode("utf-8"))
        d = b.digest()
        return h2 + base64url_encode(d).decode("utf-8")

    # @classmethod
    # def from_public_bytes(cls, key: bytes):
    #     try:
    #         k = Ed25519PublicKey.from_public_bytes(key)
    #     except Exception as err:
    #         raise ValueError("Invalid bytes for the key.") from err
    #     return cls(k)

    def sign(self, payload: bytes, footer: bytes = b"", implicit_assertion: bytes = b"") -> bytes:
        if isinstance(self._key, Ed25519PublicKey):
            raise ValueError("A public key cannot be used for signing.")
        m2 = pae([self.header, payload, footer])
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
        m2 = pae([self.header, m, footer])
        try:
            k.verify(sig, m2)
        except Exception as err:
            raise VerifyError("Failed to verify.") from err
        return m
