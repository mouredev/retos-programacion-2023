import hashlib
import hmac
from secrets import token_bytes
from typing import Any, Union

from cryptography.hazmat.primitives import hashes
from cryptography.hazmat.primitives.asymmetric import ec
from cryptography.hazmat.primitives.asymmetric.ec import (
    EllipticCurvePrivateKey,
    EllipticCurvePublicKey,
)
from cryptography.hazmat.primitives.asymmetric.utils import (
    decode_dss_signature,
    encode_dss_signature,
)
from cryptography.hazmat.primitives.kdf.hkdf import HKDF

from ..exceptions import DecryptError, SignError, VerifyError
from ..key_interface import KeyInterface
from ..key_nist import NISTKey
from ..utils import (
    base64url_decode,
    base64url_encode,
    ec_public_key_compress,
    i2osp,
    os2ip,
    pae,
)


class V3Local(NISTKey):
    """
    The key object for v3.local.
    """

    _VERSION = 3
    _TYPE = "local"

    def __init__(self, key: Union[str, bytes]):
        super().__init__(key)
        return

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
        e = HKDF(
            algorithm=hashes.SHA384(),
            length=48,
            salt=None,
            info=b"paseto-encryption-key" + nonce,
        )
        a = HKDF(
            algorithm=hashes.SHA384(),
            length=48,
            salt=None,
            info=b"paseto-auth-key-for-aead" + nonce,
        )
        try:
            tmp = e.derive(self._key)
            ek = tmp[0:32]
            n2 = tmp[32:]
            ak = a.derive(self._key)
        except Exception as err:
            raise DecryptError("Failed to derive keys.") from err

        c = self._encrypt(ek, n2, payload)
        pre_auth = pae([self.header, nonce, c, footer, implicit_assertion])
        t = hmac.new(ak, pre_auth, hashlib.sha384).digest()
        token = self._header + base64url_encode(nonce + c + t)
        if footer:
            token += b"." + base64url_encode(footer)
        return token

    def decrypt(self, payload: bytes, footer: bytes = b"", implicit_assertion: bytes = b"") -> bytes:
        n = payload[0:32]
        c = payload[32 : len(payload) - 48]
        t = payload[-48:]
        e = HKDF(
            algorithm=hashes.SHA384(),
            length=48,
            salt=None,
            info=b"paseto-encryption-key" + n,
        )
        a = HKDF(
            algorithm=hashes.SHA384(),
            length=48,
            salt=None,
            info=b"paseto-auth-key-for-aead" + n,
        )
        try:
            tmp = e.derive(self._key)
            ek = tmp[0:32]
            n2 = tmp[32:]
            ak = a.derive(self._key)
        except Exception as err:
            raise DecryptError("Failed to derive keys.") from err

        pre_auth = pae([self.header, n, c, footer, implicit_assertion])
        t2 = hmac.new(ak, pre_auth, hashlib.sha384).digest()
        if not hmac.compare_digest(t, t2):
            raise DecryptError("Failed to decrypt.")
        return self._decrypt(ek, n2, c)

    def to_paserk_id(self) -> str:
        h = "k3.lid."
        p = self.to_paserk()
        digest = hashes.Hash(hashes.SHA384())
        digest.update((h + p).encode("utf-8"))
        d = digest.finalize()
        return h + base64url_encode(d[0:33]).decode("utf-8")


class V3Public(NISTKey):
    """
    The key object for v3.public.
    """

    _VERSION = 3
    _TYPE = "public"

    def __init__(self, key: Any):
        super().__init__(key)

        self._sig_size = 96
        if not isinstance(self._key, (EllipticCurvePublicKey, EllipticCurvePrivateKey)):
            raise ValueError("The key is not ECDSA key.")

        if isinstance(self._key, EllipticCurvePublicKey):
            self._is_secret = False
        return

    @classmethod
    def from_public_bytes(cls, key: bytes):
        try:
            k = EllipticCurvePublicKey.from_encoded_point(ec.SECP384R1(), key)
        except Exception as err:
            raise ValueError("Invalid bytes for the key.") from err
        return cls(k)

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
        if frags[0] != "k3":
            raise ValueError(f"Invalid PASERK version: {frags[0]}.")

        if wrapping_key:
            # secret-wrap
            if len(frags) != 4:
                raise ValueError("Invalid PASERK format.")
            if frags[2] != "pie":
                raise ValueError(f"Unknown wrapping algorithm: {frags[2]}.")

            if frags[1] == "secret-wrap":
                h = "k3.secret-wrap.pie."
                k = cls._decode_pie(h, wrapping_key, frags[3])
                priv = ec.derive_private_key(int.from_bytes(k, byteorder="big"), ec.SECP384R1())
                return cls(priv)
            raise ValueError(f"Invalid PASERK type: {frags[1]}.")

        if len(frags) != 3:
            raise ValueError("Invalid PASERK format.")

        if password:
            # secret-pw
            if frags[1] == "secret-pw":
                h = "k3.secret-pw."
                k = cls._decode_pbkw(h, password, frags[2])
                priv = ec.derive_private_key(int.from_bytes(k, byteorder="big"), ec.SECP384R1())
                return cls(priv)
            raise ValueError(f"Invalid PASERK type: {frags[1]}.")

        # public
        k = base64url_decode(frags[2])
        if frags[1] == "public":
            pub = EllipticCurvePublicKey.from_encoded_point(ec.SECP384R1(), k)
            return cls(pub)

        # secret
        if frags[1] == "secret":
            priv = ec.derive_private_key(int.from_bytes(k, byteorder="big"), ec.SECP384R1())
            return cls(priv)
        if frags[1] == "secret-wrap":
            raise ValueError(f"{frags[1]} needs wrapping_key.")
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
            # secret-wrap
            if not isinstance(self._key, EllipticCurvePrivateKey):
                raise ValueError("Public key cannot be wrapped.")

            bkey = wrapping_key if isinstance(wrapping_key, bytes) else wrapping_key.encode("utf-8")
            h = "k3.secret-wrap.pie."
            k = self._key.private_numbers().private_value.to_bytes(48, byteorder="big")
            return h + self._encode_pie(h, bkey, k)

        if password:
            # secret-pw
            if not isinstance(self._key, EllipticCurvePrivateKey):
                raise ValueError("Public key cannot be wrapped.")

            bpw = password if isinstance(password, bytes) else password.encode("utf-8")
            h = "k3.secret-pw."
            k = self._key.private_numbers().private_value.to_bytes(48, byteorder="big")
            return h + self._encode_pbkw(h, bpw, k, iteration)

        # public
        if isinstance(self._key, EllipticCurvePublicKey):
            k = ec_public_key_compress(self._key.public_numbers().x, self._key.public_numbers().y)
            return "k3.public." + base64url_encode(k).decode("utf-8")

        # private
        k = self._key.private_numbers().private_value.to_bytes(48, byteorder="big")
        return "k3.secret." + base64url_encode(k).decode("utf-8")

    def to_paserk_id(self) -> str:
        p = self.to_paserk()
        h = "k3.pid." if isinstance(self._key, EllipticCurvePublicKey) else "k3.sid."
        digest = hashes.Hash(hashes.SHA384())
        digest.update((h + p).encode("utf-8"))
        d = digest.finalize()
        return h + base64url_encode(d[0:33]).decode("utf-8")

    def to_peer_paserk_id(self) -> str:
        if not self._is_secret:
            return ""

        pub_key = self._key.public_key()
        k = ec_public_key_compress(pub_key.public_numbers().x, pub_key.public_numbers().y)
        p = "k3.public." + base64url_encode(k).decode("utf-8")

        h = "k3.pid."
        digest = hashes.Hash(hashes.SHA384())
        digest.update((h + p).encode("utf-8"))
        d = digest.finalize()
        return h + base64url_encode(d[0:33]).decode("utf-8")

    def sign(self, payload: bytes, footer: bytes = b"", implicit_assertion: bytes = b"") -> bytes:
        if isinstance(self._key, EllipticCurvePublicKey):
            raise ValueError("A public key cannot be used for signing.")
        pk = ec_public_key_compress(
            self._key.private_numbers().public_numbers.x,
            self._key.private_numbers().public_numbers.y,
        )
        m2 = pae([pk, self.header, payload, footer, implicit_assertion])
        try:
            sig = self._key.sign(m2, ec.ECDSA(hashes.SHA384()))
            return self._der_to_os(self._key.curve.key_size, sig)
        except Exception as err:
            raise SignError("Failed to sign.") from err

    def verify(self, payload: bytes, footer: bytes = b"", implicit_assertion: bytes = b""):
        if len(payload) <= self._sig_size:
            raise ValueError("Invalid payload.")

        sig = payload[-self._sig_size :]
        m = payload[: len(payload) - self._sig_size]
        k = self._key if isinstance(self._key, EllipticCurvePublicKey) else self._key.public_key()
        pk = ec_public_key_compress(k.public_numbers().x, k.public_numbers().y)
        m2 = pae([pk, self.header, m, footer, implicit_assertion])
        try:
            der_sig = self._os_to_der(self._key.curve.key_size, sig)
            k.verify(der_sig, m2, ec.ECDSA(hashes.SHA384()))
        except Exception as err:
            raise VerifyError("Failed to verify.") from err
        return m

    def _der_to_os(self, key_size: int, sig: bytes) -> bytes:
        num_bytes = (key_size + 7) // 8
        r, s = decode_dss_signature(sig)
        return i2osp(r, num_bytes) + i2osp(s, num_bytes)

    def _os_to_der(self, key_size: int, sig: bytes) -> bytes:
        num_bytes = (key_size + 7) // 8
        if len(sig) != 2 * num_bytes:
            raise ValueError("Invalid signature.")
        r = os2ip(sig[:num_bytes])
        s = os2ip(sig[num_bytes:])
        return encode_dss_signature(r, s)
