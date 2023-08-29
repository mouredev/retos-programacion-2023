import json
from typing import Any, List, Optional, Union

from .key_interface import KeyInterface
from .paseto import Paseto
from .token import Token

# export
_paseto = Paseto()


def encode(
    key: KeyInterface,
    payload: Union[bytes, str, dict],
    footer: Union[bytes, str] = b"",
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
        footer (Union[bytes, str]): A footer.
        implicit_assertion (Union[bytes, str]): An implicit assertion. It is
            only used in ``v3`` or ``v4``.
        nonce (bytes): A nonce. If omitted(it's recommended), a nonce will be
            generated with ``secrets.token_bytes()`` internally. If you don't
            want ot use ``secrets.token_bytes()``, you can specify it via this
            parameter explicitly.
        serializer (Any): A serializer which is used when the type of
            ``payload`` is ``object``. It must have a ``dumps()`` function to
            serialize the payload. Typically, you can use ``json`` or ``cbor2``.
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
    return _paseto.encode(key, payload, footer, implicit_assertion, nonce, serializer, exp)


def decode(
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
    return _paseto.decode(keys, token, implicit_assertion, deserializer, aud)
