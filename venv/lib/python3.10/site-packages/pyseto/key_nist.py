import hashlib
import hmac
from secrets import token_bytes
from typing import Any, Union

from cryptography.hazmat.primitives import hashes

# from cryptography.hazmat.primitives.asymmetric import ec
# from cryptography.hazmat.primitives.asymmetric.ec import EllipticCurvePublicKey
from cryptography.hazmat.primitives.ciphers import Cipher, algorithms, modes

# from cryptography.hazmat.primitives.kdf.hkdf import HKDF
from cryptography.hazmat.primitives.kdf.pbkdf2 import PBKDF2HMAC

from .exceptions import DecryptError, EncryptError
from .key_interface import KeyInterface
from .utils import base64url_decode, base64url_encode


class NISTKey(KeyInterface):
    """
    NIST (v1, v3) PASETO key.
    """

    # _VERSION = 1 or 3
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
            # local-wrap
            if len(frags) != 4:
                raise ValueError("Invalid PASERK format.")
            if frags[2] != "pie":
                raise ValueError(f"Unknown wrapping algorithm: {frags[2]}.")

            h = frags[0] + "." + frags[1] + ".pie."
            if frags[1] == "local-wrap":
                return cls(cls._decode_pie(h, wrapping_key, frags[3]))
            raise ValueError(f"Invalid PASERK type: {frags[1]}.")

        if len(frags) != 3:
            raise ValueError("Invalid PASERK format.")

        if password:
            # local-pw
            h = frags[0] + "." + frags[1] + "."
            if frags[1] == "local-pw":
                return cls(cls._decode_pbkw(h, password, frags[2]))
            raise ValueError(f"Invalid PASERK type: {frags[1]}.")

        # if unsealing_key:
        #     # seal
        #     h = frags[0] + "." + frags[1] + "."
        #     if frags[1] == "seal":
        #         return cls(cls._decode_pke(h, unsealing_key, frags[2]))
        #     raise ValueError(f"Invalid PASERK type: {frags[1]}.")

        # local
        k = base64url_decode(frags[2])
        if frags[1] == "local":
            return cls(k)
        if frags[1] == "local-wrap":
            raise ValueError(f"{frags[1]} needs wrapping_key.")
        if frags[1] == "local-pw":
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

        # local-wrap
        if wrapping_key:
            bkey = wrapping_key if isinstance(wrapping_key, bytes) else wrapping_key.encode("utf-8")
            h = f"k{self.version}.local-wrap.pie."
            return h + self._encode_pie(h, bkey, self._key)

        # seal
        # if sealing_key:
        #     bkey = (
        #         sealing_key
        #         if isinstance(sealing_key, bytes)
        #         else sealing_key.encode("utf-8")
        #     )
        #     h = f"k{self.version}.seal."
        #     return h + self._encode_pke(h, bkey, self._key)

        # local-pw
        if password:
            bpw = password if isinstance(password, bytes) else password.encode("utf-8")
            h = f"k{self.version}.local-pw."
            return h + self._encode_pbkw(h, bpw, self._key, iteration)

        # local
        h = f"k{self.version}.local."
        return h + base64url_encode(self._key).decode("utf-8")

    @classmethod
    def _encode_pie(cls, header: str, wrapping_key: bytes, ptk: bytes) -> str:
        h = header.encode("utf-8")
        n = token_bytes(32)
        x = cls._generate_hash(wrapping_key, b"\x80" + n)
        ek = x[0:32]
        n2 = x[32:]
        ak = cls._generate_hash(wrapping_key, b"\x81" + n, 32)
        c = cls._encrypt(ek, n2, ptk)
        t = cls._generate_hash(ak, h + n + c, 48)
        return base64url_encode(t + n + c).decode("utf-8")

    @classmethod
    def _decode_pie(cls, header: str, wrapping_key: bytes, data: str) -> bytes:
        h = header.encode("utf-8")
        d = base64url_decode(data)
        t = d[0:48]
        n = d[48:80]
        c = d[80:]
        ak = cls._generate_hash(wrapping_key, b"\x81" + n, 32)
        t2 = cls._generate_hash(ak, h + n + c, 48)
        if t != t2:
            raise DecryptError("Failed to unwrap a key.")
        x = cls._generate_hash(wrapping_key, b"\x80" + n)
        ek = x[0:32]
        n2 = x[32:]
        return cls._decrypt(ek, n2, c)

    @classmethod
    def _encode_pbkw(cls, header: str, password: bytes, ptk: bytes, iteration: int = 100000) -> str:
        h = header.encode("utf-8")

        s = token_bytes(32)
        k = PBKDF2HMAC(
            algorithm=hashes.SHA384(),
            length=32,
            salt=s,
            iterations=iteration,
        ).derive(password)
        ek = cls._digest(b"\xff" + k)[0:32]
        ak = cls._digest(b"\xfe" + k)
        n = token_bytes(16)
        edk = cls._encrypt(ek, n, ptk)
        bi = iteration.to_bytes(4, byteorder="big")
        t = cls._generate_hash(ak, h + s + bi + n + edk, 48)
        return base64url_encode(s + bi + n + edk + t).decode("utf-8")

    @classmethod
    def _decode_pbkw(cls, header: str, password: bytes, data: str) -> bytes:
        h = header.encode("utf-8")
        d = base64url_decode(data)

        s = d[0:32]
        bi = d[32:36]
        n = d[36:52]
        edk = d[52 : len(d) - 48]
        t = d[-48:]
        i = int.from_bytes(bi, byteorder="big")

        k = PBKDF2HMAC(
            algorithm=hashes.SHA384(),
            length=32,
            salt=s,
            iterations=i,
        ).derive(password)

        ak = cls._digest(b"\xfe" + k)
        t2 = cls._generate_hash(ak, h + s + bi + n + edk, 48)
        if t != t2:
            raise DecryptError("Failed to unwrap a key.")

        ek = cls._digest(b"\xff" + k)[0:32]
        return cls._decrypt(ek, n, edk)

    # @classmethod
    # def _encode_pke(cls, header: str, sealing_key: bytes, ptk: bytes) -> str:

    #     h = header.encode("utf-8")

    #     esk = ec.generate_private_key(ec.SECP384R1())
    #     epk = ec_public_key_compress(
    #         esk.private_numbers().public_numbers.x,
    #         esk.private_numbers().public_numbers.y,
    #     )
    #     pub = EllipticCurvePublicKey.from_encoded_point(ec.SECP384R1(), sealing_key)
    #     pk = ec_public_key_compress(
    #         pub.public_numbers().x,
    #         pub.public_numbers().y,
    #     )
    #     xk = esk.exchange(ec.ECDH(), pub)
    #     tmp = cls._digest(b"\x01" + h + xk + epk + pk)
    #     ek = tmp[0:32]
    #     n = tmp[32:]
    #     ak = cls._digest(b"\x01" + h + xk + epk + pk)
    #     edk = cls._encrypt(ek, n, ptk)
    #     t = cls._generate_hash(ak, h + epk + edk, 48)
    #     return base64url_encode(t + epk + edk).decode("utf-8")

    # @classmethod
    # def _decode_pke(cls, header: str, unsealing_key: bytes, data: str) -> bytes:

    #     h = header.encode("utf-8")
    #     d = base64url_decode(data)

    #     if cls._VERSION == 1:
    #         raise NotImplementedError("Not implemented.")

    #     t = d[0:48]
    #     epk = d[48:97]
    #     edk = d[97:]
    #     sk = ec.derive_private_key(
    #         int.from_bytes(unsealing_key, byteorder="big"), ec.SECP384R1()
    #     )
    #     pub = EllipticCurvePublicKey.from_encoded_point(ec.SECP384R1(), epk)

    #     xk = sk.exchange(ec.ECDH(), pub)
    #     # shared = sk.exchange(ec.ECDH(), pub)
    #     # xk = HKDF(algorithm=hashes.SHA384(), length=48, salt=None, info=b"").derive(shared)
    #     pk = ec_public_key_compress(
    #         sk.private_numbers().public_numbers.x,
    #         sk.private_numbers().public_numbers.y,
    #     )
    #     ak = cls._digest(b"\x01" + h + xk + epk + pk)
    #     t2 = cls._generate_hash(ak, h + epk + edk, 48)
    #     if t != t2:
    #         raise DecryptError("Failed to unseal a key.")

    #     tmp = cls._digest(b"\x01" + h + xk + epk + pk)
    #     ek = tmp[0:32]
    #     n = tmp[32:]
    #     return cls._decrypt(ek, n, edk)

    @staticmethod
    def _generate_hash(key: bytes, msg: bytes, size: int = 0) -> bytes:
        try:
            d = hmac.new(key, msg, hashlib.sha384).digest()
            return d[0:size] if size > 0 else d
        except Exception as err:
            raise EncryptError("Failed to generate hash.") from err

    @staticmethod
    def _digest(msg: bytes) -> bytes:
        return hashlib.sha384(msg).digest()

    @staticmethod
    def _encrypt(key: bytes, nonce: bytes, msg: bytes) -> bytes:
        try:
            encryptor = Cipher(algorithms.AES(key), modes.CTR(nonce)).encryptor()
            return encryptor.update(msg)
        except Exception as err:
            raise EncryptError("Failed to encrypt.") from err

    @staticmethod
    def _decrypt(key: bytes, nonce: bytes, msg: bytes) -> bytes:
        try:
            decryptor = Cipher(algorithms.AES(key), modes.CTR(nonce)).decryptor()
            return decryptor.update(msg)
        except Exception as err:
            raise DecryptError("Failed to decrypt.") from err
