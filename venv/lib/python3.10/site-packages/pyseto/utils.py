import base64
from typing import List


def i2osp(x: int, x_len: int) -> bytes:
    """
    Integer-to-Octet-String primitive
    """
    if x >= 256**x_len:
        raise ValueError("integer too large")
    digits = []
    while x:
        digits.append(int(x % 256))
        x //= 256
    for _ in range(x_len - len(digits)):
        digits.append(0)
    return bytes.fromhex("".join("%.2x" % x for x in digits[::-1]))


def os2ip(octet_string: bytes) -> int:
    """
    Octet-String-to-Integer primitive
    """
    x_len = len(octet_string)
    octet_string = octet_string[::-1]
    x = 0
    for i in range(x_len):
        x += octet_string[i] * 256**i
    return x


def base64url_decode(v: str) -> bytes:
    bv = v.encode("ascii")
    rem = len(bv) % 4
    if rem > 0:
        bv += b"=" * (4 - rem)
    return base64.urlsafe_b64decode(bv)


def base64url_encode(input: bytes) -> bytes:
    return base64.urlsafe_b64encode(input).replace(b"=", b"")


def _le64(n: int) -> bytes:
    s = bytearray(8)
    for i in range(8):
        if i == 7:
            n = n & 127
        s[i] = n & 255
        n = n >> 8
    return bytes(s)


def pae(pieces: List[bytes]) -> bytes:
    output = _le64(len(pieces))
    for i in range(len(pieces)):
        output += _le64(len(pieces[i]))
        output += pieces[i]
    return output


def ec_public_key_compress(x: int, y: int) -> bytes:
    bx = x.to_bytes(48, byteorder="big")
    by = y.to_bytes((y.bit_length() + 7) // 8, byteorder="big")
    s = bytearray(1)
    s[0] = 0x02 + (by[len(by) - 1] & 1)
    return bytes(s) + bx
