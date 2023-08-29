import json
from datetime import datetime, timedelta, timezone
from typing import Any, List, Optional, Union

import iso8601

from .exceptions import VerifyError
from .key_interface import KeyInterface
from .token import Token
from .utils import base64url_encode


class Paseto(object):
    """
    A PASETO processor which can be used as a PASETO encoder/decoder.
    """

    def __init__(
        self,
        exp: int = 0,
        include_iat: bool = False,
        leeway: int = 0,
    ):
        self._exp = exp
        self._include_iat = include_iat
        self._leeway = leeway
        return

    @classmethod
    def new(
        cls,
        exp: int = 0,
        include_iat: bool = False,
        leeway: int = 0,
    ):
        """
        Constructor of PASETO processor.

        Args:
            exp (int): A default expiration time (seconds) of PASETO tokens.
                It will be set in the payload as the registered ``exp`` claim
                when calling ``encode()`` with serializer=``json`` and this
                value > ``0``. If the value <= ``0``, the ``exp`` claim will
                not be set. In addition, this value can be overwritten by the
                ``exp`` parameter of ``encode()``. The default value is ``0``.
            include_iat (bool): If this value is ``True``, PASETO tokens
                which are created through ``encode()`` include an ``iat`` claim
                when calling ``encode()`` with serializer=``json``. The default
                value is ``False``.
            leeway (int): The leeway in seconds for validating ``exp`` and
                ``nbf``. The default value is ``0``.
        Returns:
            bytes: A PASETO processor object.
        """
        return cls(exp, include_iat, leeway)

    def encode(
        self,
        key: KeyInterface,
        payload: Union[bytes, str, dict],
        footer: Union[bytes, str, dict] = b"",
        implicit_assertion: Union[bytes, str] = b"",
        nonce: bytes = b"",
        serializer: Any = json,
        exp: int = 0,
    ) -> bytes:
        """
        Encodes a message to a PASETO token with a key for encryption or signing.

        Args:
            key (KeyInterface): A key for encryption or signing.
            payload (Union[bytes, str, dict]): A message to be encrypted or signed.
            footer (Union[bytes, str, dict]): A footer.
            implicit_assertion (Union[bytes, str]): An implicit assertion. It is
                only used in ``v3`` or ``v4``.
            nonce (bytes): A nonce. If omitted(it's recommended), a nonce will be
                generated with ``secrets.token_bytes()`` internally. If you don't
                want ot use ``secrets.token_bytes()``, you can specify it via this
                parameter explicitly.
            serializer (Any): A serializer which is used when the type of
                ``payload`` and/or ``footer`` is ``dict``. It must have a
                ``dumps()`` function to serialize the payload. Typically, you
                can use ``json`` or ``cbor2``.
            exp (int): An expiration time (seconds) of the PASETO token. It will be
                set in the payload as the registered ``exp`` claim when serializer
                is ``json`` and this value > ``0``. If the value <= ``0``, the
                ``exp`` claim will not be set.
        Returns:
            bytes: A PASETO token.
        Raise:
            ValueError: Invalid arguments.
            EncryptError: Failed to encrypt the message.
            SignError: Failed to sign the message.
        """

        if not isinstance(payload, (bytes, str, dict)):
            raise ValueError("payload should be bytes, str or dict.")

        res: Union[bytes, str]
        bp: bytes
        if isinstance(payload, dict):
            if not serializer:
                raise ValueError("serializer should be specified for the payload object.")
            try:
                if not callable(serializer.dumps):
                    raise ValueError("serializer should have dumps().")
            except AttributeError:
                raise ValueError("serializer should have dumps().")
            except Exception:
                raise
            try:
                payload = self._set_registered_claims(payload, exp)
                res = serializer.dumps(payload)
                bp = res if isinstance(res, bytes) else res.encode("utf-8")
            except Exception as err:
                raise ValueError("Failed to serialize the payload.") from err
        else:
            bp = payload if isinstance(payload, bytes) else payload.encode("utf-8")

        bf: bytes
        if isinstance(footer, dict):
            if not serializer:
                raise ValueError("serializer should be specified for the footer object.")
            try:
                if not callable(serializer.dumps):
                    raise ValueError("serializer should have dumps().")
            except AttributeError:
                raise ValueError("serializer should have dumps().")
            except Exception:
                raise
            try:
                res = serializer.dumps(footer)
                bf = res if isinstance(res, bytes) else res.encode("utf-8")
            except Exception as err:
                raise ValueError("Failed to serialize the footer.") from err
        else:
            bf = footer if isinstance(footer, bytes) else footer.encode("utf-8")

        bi = implicit_assertion if isinstance(implicit_assertion, bytes) else implicit_assertion.encode("utf-8")

        if key.purpose == "local":
            return key.encrypt(bp, bf, bi, nonce)

        sig = key.sign(bp, bf, bi)
        token = key.header + base64url_encode(bp + sig)
        if bf:
            token += b"." + base64url_encode(bf)
        return token

    def decode(
        self,
        keys: Union[KeyInterface, List[KeyInterface]],
        token: Union[bytes, str],
        implicit_assertion: Union[bytes, str] = b"",
        deserializer: Optional[Any] = None,
        aud: str = "",
    ) -> Token:
        """
        Decodes a PASETO token with a key for decryption and/or verifying.

        Args:
            keys (KeyInterface): A key for decryption or verifying the signature in the token.
            token (Union[bytes, str]): A PASETO token to be decrypted or verified.
            implicit_assertion (Union[bytes, str]): An implicit assertion. It is
                only used in ``v3`` or ``v4``.
            deserializer (Optional[Any]): A deserializer which is used when you want to
                deserialize a ``payload`` attribute in the response object. It must have a
                ``loads()`` function to deserialize the payload. Typically, you can use
                ``json`` or ``cbor2``.
            aud (str): An audience claim value for the token verification.
                If ``deserializer=json`` and the payload of the token does not
                include an ``aud`` value that matches this value, the
                verification will fail.
        Returns:
            Token: A parsed PASETO token object.
        Raise:
            ValueError: Invalid arguments.
            DecryptError: Failed to decrypt the message.
            VerifyError: Failed to verify the message.
        """

        if deserializer:
            try:
                if not callable(deserializer.loads):
                    raise ValueError("deserializer should have loads().")
            except AttributeError:
                raise ValueError("deserializer should have loads().")
            except Exception:
                raise

        keys = keys if isinstance(keys, list) else [keys]
        bi = implicit_assertion if isinstance(implicit_assertion, bytes) else implicit_assertion.encode("utf-8")

        failed = None
        t = Token.new(token)
        for k in keys:
            if k.header != t.header:
                continue
            try:
                if k.purpose == "local":
                    t.payload = k.decrypt(t.payload, t.footer, bi)
                else:
                    t.payload = k.verify(t.payload, t.footer, bi)
                try:
                    if deserializer:
                        t.payload = deserializer.loads(t.payload)
                except Exception as err:
                    raise ValueError("Failed to deserialize the payload.") from err
                if deserializer:
                    try:
                        if t.footer:
                            t.footer = deserializer.loads(t.footer)
                    except Exception:
                        pass
                    self._verify_registered_claims(t.payload, aud)
                return t
            except Exception as err:
                failed = err
        if failed:
            raise failed
        raise ValueError("key is not found for verifying the token.")

    def _set_registered_claims(self, claims: dict, exp: int) -> dict:
        now = datetime.now(tz=timezone.utc)
        # exp
        if exp > 0:
            claims["exp"] = (now + timedelta(seconds=exp)).isoformat(timespec="seconds")
        elif self._exp > 0:
            claims["exp"] = (now + timedelta(seconds=self._exp)).isoformat(timespec="seconds")
        # iat
        if self._include_iat:
            claims["iat"] = now.isoformat(timespec="seconds")
        return claims

    def _verify_registered_claims(self, claims: dict, aud: str):
        now = iso8601.parse_date(datetime.now(tz=timezone.utc).isoformat(timespec="seconds"))
        # In Python 3.7 or later, the following code can be used:
        # now = datetime.fromisoformat(
        #     datetime.now(tz=timezone.utc).isoformat(timespec="seconds")
        # )
        if "exp" in claims:
            try:
                exp = iso8601.parse_date(claims["exp"])
            except Exception as err:
                raise VerifyError("Invalid exp.") from err
            if now > exp + timedelta(seconds=self._leeway):
                raise VerifyError("Token expired.")
        if "nbf" in claims:
            try:
                nbf = iso8601.parse_date(claims["nbf"])
            except Exception as err:
                raise VerifyError("Invalid nbf.") from err
            if now < nbf - timedelta(seconds=self._leeway):
                raise VerifyError("Token has not been activated yet.")
        if aud:
            if "aud" not in claims or aud != claims["aud"]:
                raise VerifyError("aud verification failed.")
        return
