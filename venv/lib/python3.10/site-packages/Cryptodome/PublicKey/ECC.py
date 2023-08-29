# ===================================================================
#
# Copyright (c) 2015, Legrandin <helderijs@gmail.com>
# All rights reserved.
#
# Redistribution and use in source and binary forms, with or without
# modification, are permitted provided that the following conditions
# are met:
#
# 1. Redistributions of source code must retain the above copyright
#    notice, this list of conditions and the following disclaimer.
# 2. Redistributions in binary form must reproduce the above copyright
#    notice, this list of conditions and the following disclaimer in
#    the documentation and/or other materials provided with the
#    distribution.
#
# THIS SOFTWARE IS PROVIDED BY THE COPYRIGHT HOLDERS AND CONTRIBUTORS
# "AS IS" AND ANY EXPRESS OR IMPLIED WARRANTIES, INCLUDING, BUT NOT
# LIMITED TO, THE IMPLIED WARRANTIES OF MERCHANTABILITY AND FITNESS
# FOR A PARTICULAR PURPOSE ARE DISCLAIMED. IN NO EVENT SHALL THE
# COPYRIGHT HOLDER OR CONTRIBUTORS BE LIABLE FOR ANY DIRECT, INDIRECT,
# INCIDENTAL, SPECIAL, EXEMPLARY, OR CONSEQUENTIAL DAMAGES (INCLUDING,
# BUT NOT LIMITED TO, PROCUREMENT OF SUBSTITUTE GOODS OR SERVICES;
# LOSS OF USE, DATA, OR PROFITS; OR BUSINESS INTERRUPTION) HOWEVER
# CAUSED AND ON ANY THEORY OF LIABILITY, WHETHER IN CONTRACT, STRICT
# LIABILITY, OR TORT (INCLUDING NEGLIGENCE OR OTHERWISE) ARISING IN
# ANY WAY OUT OF THE USE OF THIS SOFTWARE, EVEN IF ADVISED OF THE
# POSSIBILITY OF SUCH DAMAGE.
# ===================================================================

from __future__ import print_function

import re
import struct
import binascii
from collections import namedtuple

from Cryptodome.Util.py3compat import bord, tobytes, tostr, bchr, is_string
from Cryptodome.Util.number import bytes_to_long, long_to_bytes

from Cryptodome.Math.Numbers import Integer
from Cryptodome.Util.asn1 import (DerObjectId, DerOctetString, DerSequence,
                              DerBitString)

from Cryptodome.Util._raw_api import (load_pycryptodome_raw_lib, VoidPointer,
                                  SmartPointer, c_size_t, c_uint8_ptr,
                                  c_ulonglong, null_pointer)

from Cryptodome.PublicKey import (_expand_subject_public_key_info,
                              _create_subject_public_key_info,
                              _extract_subject_public_key_info)

from Cryptodome.Hash import SHA512, SHAKE256

from Cryptodome.Random import get_random_bytes
from Cryptodome.Random.random import getrandbits


_ec_lib = load_pycryptodome_raw_lib("Cryptodome.PublicKey._ec_ws", """
typedef void EcContext;
typedef void EcPoint;
int ec_ws_new_context(EcContext **pec_ctx,
                      const uint8_t *modulus,
                      const uint8_t *b,
                      const uint8_t *order,
                      size_t len,
                      uint64_t seed);
void ec_free_context(EcContext *ec_ctx);
int ec_ws_new_point(EcPoint **pecp,
                    const uint8_t *x,
                    const uint8_t *y,
                    size_t len,
                    const EcContext *ec_ctx);
void ec_ws_free_point(EcPoint *ecp);
int ec_ws_get_xy(uint8_t *x,
                 uint8_t *y,
                 size_t len,
                 const EcPoint *ecp);
int ec_ws_double(EcPoint *p);
int ec_ws_add(EcPoint *ecpa, EcPoint *ecpb);
int ec_ws_scalar(EcPoint *ecp,
                 const uint8_t *k,
                 size_t len,
                 uint64_t seed);
int ec_ws_clone(EcPoint **pecp2, const EcPoint *ecp);
int ec_ws_cmp(const EcPoint *ecp1, const EcPoint *ecp2);
int ec_ws_neg(EcPoint *p);
""")

_ed25519_lib = load_pycryptodome_raw_lib("Cryptodome.PublicKey._ed25519", """
typedef void Point;
int ed25519_new_point(Point **out,
                      const uint8_t x[32],
                      const uint8_t y[32],
                      size_t modsize,
                      const void *context);
int ed25519_clone(Point **P, const Point *Q);
void ed25519_free_point(Point *p);
int ed25519_cmp(const Point *p1, const Point *p2);
int ed25519_neg(Point *p);
int ed25519_get_xy(uint8_t *xb, uint8_t *yb, size_t modsize, Point *p);
int ed25519_double(Point *p);
int ed25519_add(Point *P1, const Point *P2);
int ed25519_scalar(Point *P, const uint8_t *scalar, size_t scalar_len, uint64_t seed);
""")

_ed448_lib = load_pycryptodome_raw_lib("Cryptodome.PublicKey._ed448", """
typedef void EcContext;
typedef void PointEd448;
int ed448_new_context(EcContext **pec_ctx);
void ed448_context(EcContext *ec_ctx);
void ed448_free_context(EcContext *ec_ctx);
int ed448_new_point(PointEd448 **out,
                    const uint8_t x[56],
                    const uint8_t y[56],
                    size_t len,
                    const EcContext *context);
int ed448_clone(PointEd448 **P, const PointEd448 *Q);
void ed448_free_point(PointEd448 *p);
int ed448_cmp(const PointEd448 *p1, const PointEd448 *p2);
int ed448_neg(PointEd448 *p);
int ed448_get_xy(uint8_t *xb, uint8_t *yb, size_t len, const PointEd448 *p);
int ed448_double(PointEd448 *p);
int ed448_add(PointEd448 *P1, const PointEd448 *P2);
int ed448_scalar(PointEd448 *P, const uint8_t *scalar, size_t scalar_len, uint64_t seed);
""")


def lib_func(ecc_obj, func_name):
    if ecc_obj._curve.desc == "Ed25519":
        result = getattr(_ed25519_lib, "ed25519_" + func_name)
    elif ecc_obj._curve.desc == "Ed448":
        result = getattr(_ed448_lib, "ed448_" + func_name)
    else:
        result = getattr(_ec_lib, "ec_ws_" + func_name)
    return result

#
# _curves is a database of curve parameters. Items are indexed by their
# human-friendly name, suchas "P-256". Each item has the following fields:
# - p:              the prime number that defines the finite field for all modulo operations
# - b:              the constant in the Short Weierstrass curve equation
# - order:          the number of elements in the group with the generator below
# - Gx              the affine coordinate X of the generator point
# - Gy              the affine coordinate Y of the generator point
# - G               the generator, as an EccPoint object
# - modulus_bits    the minimum number of bits for encoding the modulus p
# - oid             an ASCII string with the registered ASN.1 Object ID
# - context         a raw pointer to memory holding a context for all curve operations (can be NULL)
# - desc            an ASCII string describing the curve
# - openssh         the ASCII string used in OpenSSH id files for public keys on this curve
# - name            the ASCII string which is also a valid key in _curves


_Curve = namedtuple("_Curve", "p b order Gx Gy G modulus_bits oid context desc openssh name")
_curves = {}


p192_names = ["p192", "NIST P-192", "P-192", "prime192v1", "secp192r1",
              "nistp192"]


def init_p192():
    p = 0xfffffffffffffffffffffffffffffffeffffffffffffffff
    b = 0x64210519e59c80e70fa7e9ab72243049feb8deecc146b9b1
    order = 0xffffffffffffffffffffffff99def836146bc9b1b4d22831
    Gx = 0x188da80eb03090f67cbf20eb43a18800f4ff0afd82ff1012
    Gy = 0x07192b95ffc8da78631011ed6b24cdd573f977a11e794811

    p192_modulus = long_to_bytes(p, 24)
    p192_b = long_to_bytes(b, 24)
    p192_order = long_to_bytes(order, 24)

    ec_p192_context = VoidPointer()
    result = _ec_lib.ec_ws_new_context(ec_p192_context.address_of(),
                                       c_uint8_ptr(p192_modulus),
                                       c_uint8_ptr(p192_b),
                                       c_uint8_ptr(p192_order),
                                       c_size_t(len(p192_modulus)),
                                       c_ulonglong(getrandbits(64))
                                       )
    if result:
        raise ImportError("Error %d initializing P-192 context" % result)

    context = SmartPointer(ec_p192_context.get(), _ec_lib.ec_free_context)
    p192 = _Curve(Integer(p),
                  Integer(b),
                  Integer(order),
                  Integer(Gx),
                  Integer(Gy),
                  None,
                  192,
                  "1.2.840.10045.3.1.1",    # ANSI X9.62 / SEC2
                  context,
                  "NIST P-192",
                  "ecdsa-sha2-nistp192",
                  "p192")
    global p192_names
    _curves.update(dict.fromkeys(p192_names, p192))


init_p192()
del init_p192


p224_names = ["p224", "NIST P-224", "P-224", "prime224v1", "secp224r1",
              "nistp224"]


def init_p224():
    p = 0xffffffffffffffffffffffffffffffff000000000000000000000001
    b = 0xb4050a850c04b3abf54132565044b0b7d7bfd8ba270b39432355ffb4
    order = 0xffffffffffffffffffffffffffff16a2e0b8f03e13dd29455c5c2a3d
    Gx = 0xb70e0cbd6bb4bf7f321390b94a03c1d356c21122343280d6115c1d21
    Gy = 0xbd376388b5f723fb4c22dfe6cd4375a05a07476444d5819985007e34

    p224_modulus = long_to_bytes(p, 28)
    p224_b = long_to_bytes(b, 28)
    p224_order = long_to_bytes(order, 28)

    ec_p224_context = VoidPointer()
    result = _ec_lib.ec_ws_new_context(ec_p224_context.address_of(),
                                       c_uint8_ptr(p224_modulus),
                                       c_uint8_ptr(p224_b),
                                       c_uint8_ptr(p224_order),
                                       c_size_t(len(p224_modulus)),
                                       c_ulonglong(getrandbits(64))
                                       )
    if result:
        raise ImportError("Error %d initializing P-224 context" % result)

    context = SmartPointer(ec_p224_context.get(), _ec_lib.ec_free_context)
    p224 = _Curve(Integer(p),
                  Integer(b),
                  Integer(order),
                  Integer(Gx),
                  Integer(Gy),
                  None,
                  224,
                  "1.3.132.0.33",    # SEC 2
                  context,
                  "NIST P-224",
                  "ecdsa-sha2-nistp224",
                  "p224")
    global p224_names
    _curves.update(dict.fromkeys(p224_names, p224))


init_p224()
del init_p224


p256_names = ["p256", "NIST P-256", "P-256", "prime256v1", "secp256r1",
              "nistp256"]


def init_p256():
    p = 0xffffffff00000001000000000000000000000000ffffffffffffffffffffffff
    b = 0x5ac635d8aa3a93e7b3ebbd55769886bc651d06b0cc53b0f63bce3c3e27d2604b
    order = 0xffffffff00000000ffffffffffffffffbce6faada7179e84f3b9cac2fc632551
    Gx = 0x6b17d1f2e12c4247f8bce6e563a440f277037d812deb33a0f4a13945d898c296
    Gy = 0x4fe342e2fe1a7f9b8ee7eb4a7c0f9e162bce33576b315ececbb6406837bf51f5

    p256_modulus = long_to_bytes(p, 32)
    p256_b = long_to_bytes(b, 32)
    p256_order = long_to_bytes(order, 32)

    ec_p256_context = VoidPointer()
    result = _ec_lib.ec_ws_new_context(ec_p256_context.address_of(),
                                       c_uint8_ptr(p256_modulus),
                                       c_uint8_ptr(p256_b),
                                       c_uint8_ptr(p256_order),
                                       c_size_t(len(p256_modulus)),
                                       c_ulonglong(getrandbits(64))
                                       )
    if result:
        raise ImportError("Error %d initializing P-256 context" % result)

    context = SmartPointer(ec_p256_context.get(), _ec_lib.ec_free_context)
    p256 = _Curve(Integer(p),
                  Integer(b),
                  Integer(order),
                  Integer(Gx),
                  Integer(Gy),
                  None,
                  256,
                  "1.2.840.10045.3.1.7",    # ANSI X9.62 / SEC2
                  context,
                  "NIST P-256",
                  "ecdsa-sha2-nistp256",
                  "p256")
    global p256_names
    _curves.update(dict.fromkeys(p256_names, p256))


init_p256()
del init_p256


p384_names = ["p384", "NIST P-384", "P-384", "prime384v1", "secp384r1",
              "nistp384"]


def init_p384():
    p = 0xfffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffeffffffff0000000000000000ffffffff
    b = 0xb3312fa7e23ee7e4988e056be3f82d19181d9c6efe8141120314088f5013875ac656398d8a2ed19d2a85c8edd3ec2aef
    order = 0xffffffffffffffffffffffffffffffffffffffffffffffffc7634d81f4372ddf581a0db248b0a77aecec196accc52973
    Gx = 0xaa87ca22be8b05378eb1c71ef320ad746e1d3b628ba79b9859f741e082542a385502f25dbf55296c3a545e3872760aB7
    Gy = 0x3617de4a96262c6f5d9e98bf9292dc29f8f41dbd289a147ce9da3113b5f0b8c00a60b1ce1d7e819d7a431d7c90ea0e5F

    p384_modulus = long_to_bytes(p, 48)
    p384_b = long_to_bytes(b, 48)
    p384_order = long_to_bytes(order, 48)

    ec_p384_context = VoidPointer()
    result = _ec_lib.ec_ws_new_context(ec_p384_context.address_of(),
                                       c_uint8_ptr(p384_modulus),
                                       c_uint8_ptr(p384_b),
                                       c_uint8_ptr(p384_order),
                                       c_size_t(len(p384_modulus)),
                                       c_ulonglong(getrandbits(64))
                                       )
    if result:
        raise ImportError("Error %d initializing P-384 context" % result)

    context = SmartPointer(ec_p384_context.get(), _ec_lib.ec_free_context)
    p384 = _Curve(Integer(p),
                  Integer(b),
                  Integer(order),
                  Integer(Gx),
                  Integer(Gy),
                  None,
                  384,
                  "1.3.132.0.34",   # SEC 2
                  context,
                  "NIST P-384",
                  "ecdsa-sha2-nistp384",
                  "p384")
    global p384_names
    _curves.update(dict.fromkeys(p384_names, p384))


init_p384()
del init_p384


p521_names = ["p521", "NIST P-521", "P-521", "prime521v1", "secp521r1",
              "nistp521"]


def init_p521():
    p = 0x000001ffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffff
    b = 0x00000051953eb9618e1c9a1f929a21a0b68540eea2da725b99b315f3b8b489918ef109e156193951ec7e937b1652c0bd3bb1bf073573df883d2c34f1ef451fd46b503f00
    order = 0x000001fffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffa51868783bf2f966b7fcc0148f709a5d03bb5c9b8899c47aebb6fb71e91386409
    Gx = 0x000000c6858e06b70404e9cd9e3ecb662395b4429c648139053fb521f828af606b4d3dbaa14b5e77efe75928fe1dc127a2ffa8de3348b3c1856a429bf97e7e31c2e5bd66
    Gy = 0x0000011839296a789a3bc0045c8a5fb42c7d1bd998f54449579b446817afbd17273e662c97ee72995ef42640c550b9013fad0761353c7086a272c24088be94769fd16650

    p521_modulus = long_to_bytes(p, 66)
    p521_b = long_to_bytes(b, 66)
    p521_order = long_to_bytes(order, 66)

    ec_p521_context = VoidPointer()
    result = _ec_lib.ec_ws_new_context(ec_p521_context.address_of(),
                                       c_uint8_ptr(p521_modulus),
                                       c_uint8_ptr(p521_b),
                                       c_uint8_ptr(p521_order),
                                       c_size_t(len(p521_modulus)),
                                       c_ulonglong(getrandbits(64))
                                       )
    if result:
        raise ImportError("Error %d initializing P-521 context" % result)

    context = SmartPointer(ec_p521_context.get(), _ec_lib.ec_free_context)
    p521 = _Curve(Integer(p),
                  Integer(b),
                  Integer(order),
                  Integer(Gx),
                  Integer(Gy),
                  None,
                  521,
                  "1.3.132.0.35",   # SEC 2
                  context,
                  "NIST P-521",
                  "ecdsa-sha2-nistp521",
                  "p521")
    global p521_names
    _curves.update(dict.fromkeys(p521_names, p521))


init_p521()
del init_p521


ed25519_names = ["ed25519", "Ed25519"]


def init_ed25519():
    p = 0x7fffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffed  # 2**255 - 19
    order = 0x1000000000000000000000000000000014def9dea2f79cd65812631a5cf5d3ed
    Gx = 0x216936d3cd6e53fec0a4e231fdd6dc5c692cc7609525a7b2c9562d608f25d51a
    Gy = 0x6666666666666666666666666666666666666666666666666666666666666658

    ed25519 = _Curve(Integer(p),
                     None,
                     Integer(order),
                     Integer(Gx),
                     Integer(Gy),
                     None,
                     255,
                     "1.3.101.112",     # RFC8410
                     None,
                     "Ed25519",         # Used throughout; do not change
                     "ssh-ed25519",
                     "ed25519")
    global ed25519_names
    _curves.update(dict.fromkeys(ed25519_names, ed25519))


init_ed25519()
del init_ed25519


ed448_names = ["ed448", "Ed448"]


def init_ed448():
    p = 0xfffffffffffffffffffffffffffffffffffffffffffffffffffffffeffffffffffffffffffffffffffffffffffffffffffffffffffffffff  # 2**448 - 2**224 - 1
    order = 0x3fffffffffffffffffffffffffffffffffffffffffffffffffffffff7cca23e9c44edb49aed63690216cc2728dc58f552378c292ab5844f3
    Gx = 0x4f1970c66bed0ded221d15a622bf36da9e146570470f1767ea6de324a3d3a46412ae1af72ab66511433b80e18b00938e2626a82bc70cc05e
    Gy = 0x693f46716eb6bc248876203756c9c7624bea73736ca3984087789c1e05a0c2d73ad3ff1ce67c39c4fdbd132c4ed7c8ad9808795bf230fa14

    ed448_context = VoidPointer()
    result = _ed448_lib.ed448_new_context(ed448_context.address_of())
    if result:
        raise ImportError("Error %d initializing Ed448 context" % result)

    context = SmartPointer(ed448_context.get(), _ed448_lib.ed448_free_context)

    ed448 = _Curve(Integer(p),
                   None,
                   Integer(order),
                   Integer(Gx),
                   Integer(Gy),
                   None,
                   448,
                   "1.3.101.113",       # RFC8410
                   context,
                   "Ed448",             # Used throughout; do not change
                   None,
                   "ed448")
    global ed448_names
    _curves.update(dict.fromkeys(ed448_names, ed448))


init_ed448()
del init_ed448


class UnsupportedEccFeature(ValueError):
    pass


class EccPoint(object):
    """A class to model a point on an Elliptic Curve.

    The class supports operators for:

    * Adding two points: ``R = S + T``
    * In-place addition: ``S += T``
    * Negating a point: ``R = -T``
    * Comparing two points: ``if S == T: ...`` or ``if S != T: ...``
    * Multiplying a point by a scalar: ``R = S*k``
    * In-place multiplication by a scalar: ``T *= k``

    :ivar x: The affine X-coordinate of the ECC point
    :vartype x: integer

    :ivar y: The affine Y-coordinate of the ECC point
    :vartype y: integer

    :ivar xy: The tuple with affine X- and Y- coordinates
    """

    def __init__(self, x, y, curve="p256"):

        try:
            self._curve = _curves[curve]
        except KeyError:
            raise ValueError("Unknown curve name %s" % str(curve))
        self._curve_name = curve

        modulus_bytes = self.size_in_bytes()

        xb = long_to_bytes(x, modulus_bytes)
        yb = long_to_bytes(y, modulus_bytes)
        if len(xb) != modulus_bytes or len(yb) != modulus_bytes:
            raise ValueError("Incorrect coordinate length")

        new_point = lib_func(self, "new_point")
        free_func = lib_func(self, "free_point")

        self._point = VoidPointer()
        try:
            context = self._curve.context.get()
        except AttributeError:
            context = null_pointer
        result = new_point(self._point.address_of(),
                           c_uint8_ptr(xb),
                           c_uint8_ptr(yb),
                           c_size_t(modulus_bytes),
                           context)

        if result:
            if result == 15:
                raise ValueError("The EC point does not belong to the curve")
            raise ValueError("Error %d while instantiating an EC point" % result)

        # Ensure that object disposal of this Python object will (eventually)
        # free the memory allocated by the raw library for the EC point
        self._point = SmartPointer(self._point.get(), free_func)

    def set(self, point):
        clone = lib_func(self, "clone")
        free_func = lib_func(self, "free_point")

        self._point = VoidPointer()
        result = clone(self._point.address_of(),
                       point._point.get())

        if result:
            raise ValueError("Error %d while cloning an EC point" % result)

        self._point = SmartPointer(self._point.get(), free_func)
        return self

    def __eq__(self, point):
        if not isinstance(point, EccPoint):
            return False

        cmp_func = lib_func(self, "cmp")
        return 0 == cmp_func(self._point.get(), point._point.get())

    # Only needed for Python 2
    def __ne__(self, point):
        return not self == point

    def __neg__(self):
        neg_func = lib_func(self, "neg")
        np = self.copy()
        result = neg_func(np._point.get())
        if result:
            raise ValueError("Error %d while inverting an EC point" % result)
        return np

    def copy(self):
        """Return a copy of this point."""
        x, y = self.xy
        np = EccPoint(x, y, self._curve_name)
        return np

    def _is_eddsa(self):
        return self._curve.name in ("ed25519", "ed448")

    def is_point_at_infinity(self):
        """``True`` if this is the *point-at-infinity*."""

        if self._is_eddsa():
            return self.x == 0
        else:
            return self.xy == (0, 0)

    def point_at_infinity(self):
        """Return the *point-at-infinity* for the curve."""

        if self._is_eddsa():
            return EccPoint(0, 1, self._curve_name)
        else:
            return EccPoint(0, 0, self._curve_name)

    @property
    def x(self):
        return self.xy[0]

    @property
    def y(self):
        return self.xy[1]

    @property
    def xy(self):
        modulus_bytes = self.size_in_bytes()
        xb = bytearray(modulus_bytes)
        yb = bytearray(modulus_bytes)
        get_xy = lib_func(self, "get_xy")
        result = get_xy(c_uint8_ptr(xb),
                        c_uint8_ptr(yb),
                        c_size_t(modulus_bytes),
                        self._point.get())
        if result:
            raise ValueError("Error %d while encoding an EC point" % result)

        return (Integer(bytes_to_long(xb)), Integer(bytes_to_long(yb)))

    def size_in_bytes(self):
        """Size of each coordinate, in bytes."""
        return (self.size_in_bits() + 7) // 8

    def size_in_bits(self):
        """Size of each coordinate, in bits."""
        return self._curve.modulus_bits

    def double(self):
        """Double this point (in-place operation).

        Returns:
            This same object (to enable chaining).
        """

        double_func = lib_func(self, "double")
        result = double_func(self._point.get())
        if result:
            raise ValueError("Error %d while doubling an EC point" % result)
        return self

    def __iadd__(self, point):
        """Add a second point to this one"""

        add_func = lib_func(self, "add")
        result = add_func(self._point.get(), point._point.get())
        if result:
            if result == 16:
                raise ValueError("EC points are not on the same curve")
            raise ValueError("Error %d while adding two EC points" % result)
        return self

    def __add__(self, point):
        """Return a new point, the addition of this one and another"""

        np = self.copy()
        np += point
        return np

    def __imul__(self, scalar):
        """Multiply this point by a scalar"""

        scalar_func = lib_func(self, "scalar")
        if scalar < 0:
            raise ValueError("Scalar multiplication is only defined for non-negative integers")
        sb = long_to_bytes(scalar)
        result = scalar_func(self._point.get(),
                             c_uint8_ptr(sb),
                             c_size_t(len(sb)),
                             c_ulonglong(getrandbits(64)))
        if result:
            raise ValueError("Error %d during scalar multiplication" % result)
        return self

    def __mul__(self, scalar):
        """Return a new point, the scalar product of this one"""

        np = self.copy()
        np *= scalar
        return np

    def __rmul__(self, left_hand):
        return self.__mul__(left_hand)


# Last piece of initialization
p192_G = EccPoint(_curves['p192'].Gx, _curves['p192'].Gy, "p192")
p192 = _curves['p192']._replace(G=p192_G)
_curves.update(dict.fromkeys(p192_names, p192))
del p192_G, p192, p192_names

p224_G = EccPoint(_curves['p224'].Gx, _curves['p224'].Gy, "p224")
p224 = _curves['p224']._replace(G=p224_G)
_curves.update(dict.fromkeys(p224_names, p224))
del p224_G, p224, p224_names

p256_G = EccPoint(_curves['p256'].Gx, _curves['p256'].Gy, "p256")
p256 = _curves['p256']._replace(G=p256_G)
_curves.update(dict.fromkeys(p256_names, p256))
del p256_G, p256, p256_names

p384_G = EccPoint(_curves['p384'].Gx, _curves['p384'].Gy, "p384")
p384 = _curves['p384']._replace(G=p384_G)
_curves.update(dict.fromkeys(p384_names, p384))
del p384_G, p384, p384_names

p521_G = EccPoint(_curves['p521'].Gx, _curves['p521'].Gy, "p521")
p521 = _curves['p521']._replace(G=p521_G)
_curves.update(dict.fromkeys(p521_names, p521))
del p521_G, p521, p521_names

ed25519_G = EccPoint(_curves['Ed25519'].Gx, _curves['Ed25519'].Gy, "Ed25519")
ed25519 = _curves['Ed25519']._replace(G=ed25519_G)
_curves.update(dict.fromkeys(ed25519_names, ed25519))
del ed25519_G, ed25519, ed25519_names

ed448_G = EccPoint(_curves['Ed448'].Gx, _curves['Ed448'].Gy, "Ed448")
ed448 = _curves['Ed448']._replace(G=ed448_G)
_curves.update(dict.fromkeys(ed448_names, ed448))
del ed448_G, ed448, ed448_names


class EccKey(object):
    r"""Class defining an ECC key.
    Do not instantiate directly.
    Use :func:`generate`, :func:`construct` or :func:`import_key` instead.

    :ivar curve: The name of the curve as defined in the `ECC table`_.
    :vartype curve: string

    :ivar pointQ: an ECC point representating the public component.
    :vartype pointQ: :class:`EccPoint`

    :ivar d: A scalar that represents the private component
             in NIST P curves. It is smaller than the
             order of the generator point.
    :vartype d: integer

    :ivar seed: A seed that representats the private component
                in EdDSA curves
                (Ed25519, 32 bytes; Ed448, 57 bytes).
    :vartype seed: bytes
    """

    def __init__(self, **kwargs):
        """Create a new ECC key

        Keywords:
          curve : string
            The name of the curve.
          d : integer
            Mandatory for a private key one NIST P curves.
            It must be in the range ``[1..order-1]``.
          seed : bytes
            Mandatory for a private key on the Ed25519 (32 bytes)
            or Ed448 (57 bytes) curve.
          point : EccPoint
            Mandatory for a public key. If provided for a private key,
            the implementation will NOT check whether it matches ``d``.

        Only one parameter among ``d``, ``seed`` or ``point`` may be used.
        """

        kwargs_ = dict(kwargs)
        curve_name = kwargs_.pop("curve", None)
        self._d = kwargs_.pop("d", None)
        self._seed = kwargs_.pop("seed", None)
        self._point = kwargs_.pop("point", None)
        if curve_name is None and self._point:
            curve_name = self._point._curve_name
        if kwargs_:
            raise TypeError("Unknown parameters: " + str(kwargs_))

        if curve_name not in _curves:
            raise ValueError("Unsupported curve (%s)" % curve_name)
        self._curve = _curves[curve_name]
        self.curve = self._curve.desc

        count = int(self._d is not None) + int(self._seed is not None)

        if count == 0:
            if self._point is None:
                raise ValueError("At lest one between parameters 'point', 'd' or 'seed' must be specified")
            return

        if count == 2:
            raise ValueError("Parameters d and seed are mutually exclusive")

        # NIST P curves work with d, EdDSA works with seed

        if not self._is_eddsa():
            if self._seed is not None:
                raise ValueError("Parameter 'seed' can only be used with Ed25519 or Ed448")
            self._d = Integer(self._d)
            if not 1 <= self._d < self._curve.order:
                raise ValueError("Parameter d must be an integer smaller than the curve order")
        else:
            if self._d is not None:
                raise ValueError("Parameter d can only be used with NIST P curves")
            # RFC 8032, 5.1.5
            if self._curve.name == "ed25519":
                if len(self._seed) != 32:
                    raise ValueError("Parameter seed must be 32 bytes long for Ed25519")
                seed_hash = SHA512.new(self._seed).digest()   # h
                self._prefix = seed_hash[32:]
                tmp = bytearray(seed_hash[:32])
                tmp[0] &= 0xF8
                tmp[31] = (tmp[31] & 0x7F) | 0x40
            # RFC 8032, 5.2.5
            elif self._curve.name == "ed448":
                if len(self._seed) != 57:
                    raise ValueError("Parameter seed must be 57 bytes long for Ed448")
                seed_hash = SHAKE256.new(self._seed).read(114)  # h
                self._prefix = seed_hash[57:]
                tmp = bytearray(seed_hash[:57])
                tmp[0] &= 0xFC
                tmp[55] |= 0x80
                tmp[56] = 0
            self._d = Integer.from_bytes(tmp, byteorder='little')

    def _is_eddsa(self):
        return self._curve.desc in ("Ed25519", "Ed448")

    def __eq__(self, other):
        if not isinstance(other, EccKey):
            return False

        if other.has_private() != self.has_private():
            return False

        return other.pointQ == self.pointQ

    def __repr__(self):
        if self.has_private():
            if self._is_eddsa():
                extra = ", seed=%s" % tostr(binascii.hexlify(self._seed))
            else:
                extra = ", d=%d" % int(self._d)
        else:
            extra = ""
        x, y = self.pointQ.xy
        return "EccKey(curve='%s', point_x=%d, point_y=%d%s)" % (self._curve.desc, x, y, extra)

    def has_private(self):
        """``True`` if this key can be used for making signatures or decrypting data."""

        return self._d is not None

    # ECDSA
    def _sign(self, z, k):
        assert 0 < k < self._curve.order

        order = self._curve.order
        blind = Integer.random_range(min_inclusive=1,
                                     max_exclusive=order)

        blind_d = self._d * blind
        inv_blind_k = (blind * k).inverse(order)

        r = (self._curve.G * k).x % order
        s = inv_blind_k * (blind * z + blind_d * r) % order
        return (r, s)

    # ECDSA
    def _verify(self, z, rs):
        order = self._curve.order
        sinv = rs[1].inverse(order)
        point1 = self._curve.G * ((sinv * z) % order)
        point2 = self.pointQ * ((sinv * rs[0]) % order)
        return (point1 + point2).x == rs[0]

    @property
    def d(self):
        if not self.has_private():
            raise ValueError("This is not a private ECC key")
        return self._d

    @property
    def seed(self):
        if not self.has_private():
            raise ValueError("This is not a private ECC key")
        return self._seed

    @property
    def pointQ(self):
        if self._point is None:
            self._point = self._curve.G * self._d
        return self._point

    def public_key(self):
        """A matching ECC public key.

        Returns:
            a new :class:`EccKey` object
        """

        return EccKey(curve=self._curve.desc, point=self.pointQ)

    def _export_SEC1(self, compress):
        if self._is_eddsa():
            raise ValueError("SEC1 format is unsupported for EdDSA curves")

        # See 2.2 in RFC5480 and 2.3.3 in SEC1
        #
        # The first byte is:
        # - 0x02:   compressed, only X-coordinate, Y-coordinate is even
        # - 0x03:   compressed, only X-coordinate, Y-coordinate is odd
        # - 0x04:   uncompressed, X-coordinate is followed by Y-coordinate
        #
        # PAI is in theory encoded as 0x00.

        modulus_bytes = self.pointQ.size_in_bytes()

        if compress:
            if self.pointQ.y.is_odd():
                first_byte = b'\x03'
            else:
                first_byte = b'\x02'
            public_key = (first_byte +
                          self.pointQ.x.to_bytes(modulus_bytes))
        else:
            public_key = (b'\x04' +
                          self.pointQ.x.to_bytes(modulus_bytes) +
                          self.pointQ.y.to_bytes(modulus_bytes))
        return public_key

    def _export_eddsa(self):
        x, y = self.pointQ.xy
        if self._curve.name == "ed25519":
            result = bytearray(y.to_bytes(32, byteorder='little'))
            result[31] = ((x & 1) << 7) | result[31]
        elif self._curve.name == "ed448":
            result = bytearray(y.to_bytes(57, byteorder='little'))
            result[56] = (x & 1) << 7
        else:
            raise ValueError("Not an EdDSA key to export")
        return bytes(result)

    def _export_subjectPublicKeyInfo(self, compress):
        if self._is_eddsa():
            oid = self._curve.oid
            public_key = self._export_eddsa()
            params = None
        else:
            oid = "1.2.840.10045.2.1"   # unrestricted
            public_key = self._export_SEC1(compress)
            params = DerObjectId(self._curve.oid)

        return _create_subject_public_key_info(oid,
                                               public_key,
                                               params)

    def _export_rfc5915_private_der(self, include_ec_params=True):

        assert self.has_private()

        # ECPrivateKey ::= SEQUENCE {
        #           version        INTEGER { ecPrivkeyVer1(1) } (ecPrivkeyVer1),
        #           privateKey     OCTET STRING,
        #           parameters [0] ECParameters {{ NamedCurve }} OPTIONAL,
        #           publicKey  [1] BIT STRING OPTIONAL
        #    }

        # Public key - uncompressed form
        modulus_bytes = self.pointQ.size_in_bytes()
        public_key = (b'\x04' +
                      self.pointQ.x.to_bytes(modulus_bytes) +
                      self.pointQ.y.to_bytes(modulus_bytes))

        seq = [1,
               DerOctetString(self.d.to_bytes(modulus_bytes)),
               DerObjectId(self._curve.oid, explicit=0),
               DerBitString(public_key, explicit=1)]

        if not include_ec_params:
            del seq[2]

        return DerSequence(seq).encode()

    def _export_pkcs8(self, **kwargs):
        from Cryptodome.IO import PKCS8

        if kwargs.get('passphrase', None) is not None and 'protection' not in kwargs:
            raise ValueError("At least the 'protection' parameter should be present")

        if self._is_eddsa():
            oid = self._curve.oid
            private_key = DerOctetString(self._seed).encode()
            params = None
        else:
            oid = "1.2.840.10045.2.1"  # unrestricted
            private_key = self._export_rfc5915_private_der(include_ec_params=False)
            params = DerObjectId(self._curve.oid)

        result = PKCS8.wrap(private_key,
                            oid,
                            key_params=params,
                            **kwargs)
        return result

    def _export_public_pem(self, compress):
        from Cryptodome.IO import PEM

        encoded_der = self._export_subjectPublicKeyInfo(compress)
        return PEM.encode(encoded_der, "PUBLIC KEY")

    def _export_private_pem(self, passphrase, **kwargs):
        from Cryptodome.IO import PEM

        encoded_der = self._export_rfc5915_private_der()
        return PEM.encode(encoded_der, "EC PRIVATE KEY", passphrase, **kwargs)

    def _export_private_clear_pkcs8_in_clear_pem(self):
        from Cryptodome.IO import PEM

        encoded_der = self._export_pkcs8()
        return PEM.encode(encoded_der, "PRIVATE KEY")

    def _export_private_encrypted_pkcs8_in_clear_pem(self, passphrase, **kwargs):
        from Cryptodome.IO import PEM

        assert passphrase
        if 'protection' not in kwargs:
            raise ValueError("At least the 'protection' parameter should be present")
        encoded_der = self._export_pkcs8(passphrase=passphrase, **kwargs)
        return PEM.encode(encoded_der, "ENCRYPTED PRIVATE KEY")

    def _export_openssh(self, compress):
        if self.has_private():
            raise ValueError("Cannot export OpenSSH private keys")

        desc = self._curve.openssh

        if desc is None:
            raise ValueError("Cannot export %s keys as OpenSSH" % self._curve.name)
        elif desc == "ssh-ed25519":
            public_key = self._export_eddsa()
            comps = (tobytes(desc), tobytes(public_key))
        else:
            modulus_bytes = self.pointQ.size_in_bytes()

            if compress:
                first_byte = 2 + self.pointQ.y.is_odd()
                public_key = (bchr(first_byte) +
                              self.pointQ.x.to_bytes(modulus_bytes))
            else:
                public_key = (b'\x04' +
                              self.pointQ.x.to_bytes(modulus_bytes) +
                              self.pointQ.y.to_bytes(modulus_bytes))

            middle = desc.split("-")[2]
            comps = (tobytes(desc), tobytes(middle), public_key)

        blob = b"".join([struct.pack(">I", len(x)) + x for x in comps])
        return desc + " " + tostr(binascii.b2a_base64(blob))

    def export_key(self, **kwargs):
        """Export this ECC key.

        Args:
          format (string):
            The format to use for encoding the key:

            - ``'DER'``. The key will be encoded in ASN.1 DER format (binary).
              For a public key, the ASN.1 ``subjectPublicKeyInfo`` structure
              defined in `RFC5480`_ will be used.
              For a private key, the ASN.1 ``ECPrivateKey`` structure defined
              in `RFC5915`_ is used instead (possibly within a PKCS#8 envelope,
              see the ``use_pkcs8`` flag below).
            - ``'PEM'``. The key will be encoded in a PEM_ envelope (ASCII).
            - ``'OpenSSH'``. The key will be encoded in the OpenSSH_ format
              (ASCII, public keys only).
            - ``'SEC1'``. The public key (i.e., the EC point) will be encoded
              into ``bytes`` according to Section 2.3.3 of `SEC1`_
              (which is a subset of the older X9.62 ITU standard).
              Only for NIST P-curves.
            - ``'raw'``. The public key will be encoded as ``bytes``,
              without any metadata.

              * For NIST P-curves: equivalent to ``'SEC1'``.
              * For EdDSA curves: ``bytes`` in the format defined in `RFC8032`_.

          passphrase (byte string or string):
            The passphrase to use for protecting the private key.

          use_pkcs8 (boolean):
            Only relevant for private keys.

            If ``True`` (default and recommended), the `PKCS#8`_ representation
            will be used. It must be ``True`` for EdDSA curves.

          protection (string):
            When a private key is exported with password-protection
            and PKCS#8 (both ``DER`` and ``PEM`` formats), this parameter MUST be
            present and be a valid algorithm supported by :mod:`Cryptodome.IO.PKCS8`.
            It is recommended to use ``PBKDF2WithHMAC-SHA1AndAES128-CBC``.

          compress (boolean):
            If ``True``, the method returns a more compact representation
            of the public key, with the X-coordinate only.

            If ``False`` (default), the method returns the full public key.

            This parameter is ignored for EdDSA curves, as compression is
            mandatory.

        .. warning::
            If you don't provide a passphrase, the private key will be
            exported in the clear!

        .. note::
            When exporting a private key with password-protection and `PKCS#8`_
            (both ``DER`` and ``PEM`` formats), any extra parameters
            to ``export_key()`` will be passed to :mod:`Cryptodome.IO.PKCS8`.

        .. _PEM:        http://www.ietf.org/rfc/rfc1421.txt
        .. _`PEM encryption`: http://www.ietf.org/rfc/rfc1423.txt
        .. _OpenSSH:    http://www.openssh.com/txt/rfc5656.txt
        .. _RFC5480:    https://tools.ietf.org/html/rfc5480
        .. _SEC1:       https://www.secg.org/sec1-v2.pdf

        Returns:
            A multi-line string (for ``'PEM'`` and ``'OpenSSH'``) or
            ``bytes`` (for ``'DER'``, ``'SEC1'``, and ``'raw'``) with the encoded key.
        """

        args = kwargs.copy()
        ext_format = args.pop("format")
        if ext_format not in ("PEM", "DER", "OpenSSH", "SEC1", "raw"):
            raise ValueError("Unknown format '%s'" % ext_format)

        compress = args.pop("compress", False)

        if self.has_private():
            passphrase = args.pop("passphrase", None)
            if is_string(passphrase):
                passphrase = tobytes(passphrase)
                if not passphrase:
                    raise ValueError("Empty passphrase")
            use_pkcs8 = args.pop("use_pkcs8", True)

            if not use_pkcs8 and self._is_eddsa():
                raise ValueError("'pkcs8' must be True for EdDSA curves")

            if ext_format == "PEM":
                if use_pkcs8:
                    if passphrase:
                        return self._export_private_encrypted_pkcs8_in_clear_pem(passphrase, **args)
                    else:
                        return self._export_private_clear_pkcs8_in_clear_pem()
                else:
                    return self._export_private_pem(passphrase, **args)
            elif ext_format == "DER":
                # DER
                if passphrase and not use_pkcs8:
                    raise ValueError("Private keys can only be encrpyted with DER using PKCS#8")
                if use_pkcs8:
                    return self._export_pkcs8(passphrase=passphrase, **args)
                else:
                    return self._export_rfc5915_private_der()
            else:
                raise ValueError("Private keys cannot be exported "
                                 "in the '%s' format" % ext_format)
        else:  # Public key
            if args:
                raise ValueError("Unexpected parameters: '%s'" % args)
            if ext_format == "PEM":
                return self._export_public_pem(compress)
            elif ext_format == "DER":
                return self._export_subjectPublicKeyInfo(compress)
            elif ext_format == "SEC1":
                return self._export_SEC1(compress)
            elif ext_format == "raw":
                if self._curve.name in ('ed25519', 'ed448'):
                    return self._export_eddsa()
                else:
                    return self._export_SEC1(compress)
            else:
                return self._export_openssh(compress)


def generate(**kwargs):
    """Generate a new private key on the given curve.

    Args:

      curve (string):
        Mandatory. It must be a curve name defined in the `ECC table`_.

      randfunc (callable):
        Optional. The RNG to read randomness from.
        If ``None``, :func:`Cryptodome.Random.get_random_bytes` is used.
    """

    curve_name = kwargs.pop("curve")
    curve = _curves[curve_name]
    randfunc = kwargs.pop("randfunc", get_random_bytes)
    if kwargs:
        raise TypeError("Unknown parameters: " + str(kwargs))

    if _curves[curve_name].name == "ed25519":
        seed = randfunc(32)
        new_key = EccKey(curve=curve_name, seed=seed)
    elif _curves[curve_name].name == "ed448":
        seed = randfunc(57)
        new_key = EccKey(curve=curve_name, seed=seed)
    else:
        d = Integer.random_range(min_inclusive=1,
                                 max_exclusive=curve.order,
                                 randfunc=randfunc)
        new_key = EccKey(curve=curve_name, d=d)

    return new_key


def construct(**kwargs):
    """Build a new ECC key (private or public) starting
    from some base components.

    In most cases, you will already have an existing key
    which you can read in with :func:`import_key` instead
    of this function.

    Args:
      curve (string):
        Mandatory. The name of the elliptic curve, as defined in the `ECC table`_.

      d (integer):
        Mandatory for a private key and a NIST P-curve (e.g., P-256):
        the integer in the range ``[1..order-1]`` that represents the key.

      seed (bytes):
        Mandatory for a private key and an EdDSA curve.
        It must be 32 bytes for Ed25519, and 57 bytes for Ed448.

      point_x (integer):
        Mandatory for a public key: the X coordinate (affine) of the ECC point.

      point_y (integer):
        Mandatory for a public key: the Y coordinate (affine) of the ECC point.

    Returns:
      :class:`EccKey` : a new ECC key object
    """

    curve_name = kwargs["curve"]
    curve = _curves[curve_name]
    point_x = kwargs.pop("point_x", None)
    point_y = kwargs.pop("point_y", None)

    if "point" in kwargs:
        raise TypeError("Unknown keyword: point")

    if None not in (point_x, point_y):
        # ValueError is raised if the point is not on the curve
        kwargs["point"] = EccPoint(point_x, point_y, curve_name)

    new_key = EccKey(**kwargs)

    # Validate that the private key matches the public one
    # because EccKey will not do that automatically
    if new_key.has_private() and 'point' in kwargs:
        pub_key = curve.G * new_key.d
        if pub_key.xy != (point_x, point_y):
            raise ValueError("Private and public ECC keys do not match")

    return new_key


def _import_public_der(ec_point, curve_oid=None, curve_name=None):
    """Convert an encoded EC point into an EccKey object

    ec_point: byte string with the EC point (SEC1-encoded)
    curve_oid: string with the name the curve
    curve_name: string with the OID of the curve

    Either curve_id or curve_name must be specified

    """

    for _curve_name, curve in _curves.items():
        if curve_oid and curve.oid == curve_oid:
            break
        if curve_name == _curve_name:
            break
    else:
        if curve_oid:
            raise UnsupportedEccFeature("Unsupported ECC curve (OID: %s)" % curve_oid)
        else:
            raise UnsupportedEccFeature("Unsupported ECC curve (%s)" % curve_name)

    # See 2.2 in RFC5480 and 2.3.3 in SEC1
    # The first byte is:
    # - 0x02:   compressed, only X-coordinate, Y-coordinate is even
    # - 0x03:   compressed, only X-coordinate, Y-coordinate is odd
    # - 0x04:   uncompressed, X-coordinate is followed by Y-coordinate
    #
    # PAI is in theory encoded as 0x00.

    modulus_bytes = curve.p.size_in_bytes()
    point_type = bord(ec_point[0])

    # Uncompressed point
    if point_type == 0x04:
        if len(ec_point) != (1 + 2 * modulus_bytes):
            raise ValueError("Incorrect EC point length")
        x = Integer.from_bytes(ec_point[1:modulus_bytes+1])
        y = Integer.from_bytes(ec_point[modulus_bytes+1:])
    # Compressed point
    elif point_type in (0x02, 0x03):
        if len(ec_point) != (1 + modulus_bytes):
            raise ValueError("Incorrect EC point length")
        x = Integer.from_bytes(ec_point[1:])
        # Right now, we only support Short Weierstrass curves
        y = (x**3 - x*3 + curve.b).sqrt(curve.p)
        if point_type == 0x02 and y.is_odd():
            y = curve.p - y
        if point_type == 0x03 and y.is_even():
            y = curve.p - y
    else:
        raise ValueError("Incorrect EC point encoding")

    return construct(curve=_curve_name, point_x=x, point_y=y)


def _import_subjectPublicKeyInfo(encoded, *kwargs):
    """Convert a subjectPublicKeyInfo into an EccKey object"""

    # See RFC5480

    # Parse the generic subjectPublicKeyInfo structure
    oid, ec_point, params = _expand_subject_public_key_info(encoded)

    nist_p_oids = (
        "1.2.840.10045.2.1",        # id-ecPublicKey (unrestricted)
        "1.3.132.1.12",             # id-ecDH
        "1.3.132.1.13"              # id-ecMQV
    )
    eddsa_oids = {
        "1.3.101.112": ("Ed25519", _import_ed25519_public_key),     # id-Ed25519
        "1.3.101.113": ("Ed448",   _import_ed448_public_key)        # id-Ed448
    }

    if oid in nist_p_oids:
        # See RFC5480

        # Parameters are mandatory and encoded as ECParameters
        # ECParameters ::= CHOICE {
        #   namedCurve         OBJECT IDENTIFIER
        #   -- implicitCurve   NULL
        #   -- specifiedCurve  SpecifiedECDomain
        # }
        # implicitCurve and specifiedCurve are not supported (as per RFC)
        if not params:
            raise ValueError("Missing ECC parameters for ECC OID %s" % oid)
        try:
            curve_oid = DerObjectId().decode(params).value
        except ValueError:
            raise ValueError("Error decoding namedCurve")

        # ECPoint ::= OCTET STRING
        return _import_public_der(ec_point, curve_oid=curve_oid)

    elif oid in eddsa_oids:
        # See RFC8410
        curve_name, import_eddsa_public_key = eddsa_oids[oid]

        # Parameters must be absent
        if params:
            raise ValueError("Unexpected ECC parameters for ECC OID %s" % oid)

        x, y = import_eddsa_public_key(ec_point)
        return construct(point_x=x, point_y=y, curve=curve_name)
    else:
        raise UnsupportedEccFeature("Unsupported ECC OID: %s" % oid)


def _import_rfc5915_der(encoded, passphrase, curve_oid=None):

    # See RFC5915 https://tools.ietf.org/html/rfc5915
    #
    # ECPrivateKey ::= SEQUENCE {
    #           version        INTEGER { ecPrivkeyVer1(1) } (ecPrivkeyVer1),
    #           privateKey     OCTET STRING,
    #           parameters [0] ECParameters {{ NamedCurve }} OPTIONAL,
    #           publicKey  [1] BIT STRING OPTIONAL
    #    }

    private_key = DerSequence().decode(encoded, nr_elements=(3, 4))
    if private_key[0] != 1:
        raise ValueError("Incorrect ECC private key version")

    try:
        parameters = DerObjectId(explicit=0).decode(private_key[2]).value
        if curve_oid is not None and parameters != curve_oid:
            raise ValueError("Curve mismatch")
        curve_oid = parameters
    except ValueError:
        pass

    if curve_oid is None:
        raise ValueError("No curve found")

    for curve_name, curve in _curves.items():
        if curve.oid == curve_oid:
            break
    else:
        raise UnsupportedEccFeature("Unsupported ECC curve (OID: %s)" % curve_oid)

    scalar_bytes = DerOctetString().decode(private_key[1]).payload
    modulus_bytes = curve.p.size_in_bytes()
    if len(scalar_bytes) != modulus_bytes:
        raise ValueError("Private key is too small")
    d = Integer.from_bytes(scalar_bytes)

    # Decode public key (if any)
    if len(private_key) > 2:
        public_key_enc = DerBitString(explicit=1).decode(private_key[-1]).value
        public_key = _import_public_der(public_key_enc, curve_oid=curve_oid)
        point_x = public_key.pointQ.x
        point_y = public_key.pointQ.y
    else:
        point_x = point_y = None

    return construct(curve=curve_name, d=d, point_x=point_x, point_y=point_y)


def _import_pkcs8(encoded, passphrase):
    from Cryptodome.IO import PKCS8

    algo_oid, private_key, params = PKCS8.unwrap(encoded, passphrase)

    nist_p_oids = (
        "1.2.840.10045.2.1",        # id-ecPublicKey (unrestricted)
        "1.3.132.1.12",             # id-ecDH
        "1.3.132.1.13"              # id-ecMQV
    )
    eddsa_oids = {
        "1.3.101.112": "Ed25519",   # id-Ed25519
        "1.3.101.113": "Ed448",     # id-Ed448
    }

    if algo_oid in nist_p_oids:
        curve_oid = DerObjectId().decode(params).value
        return _import_rfc5915_der(private_key, passphrase, curve_oid)
    elif algo_oid in eddsa_oids:
        if params is not None:
            raise ValueError("EdDSA ECC private key must not have parameters")
        curve_oid = None
        seed = DerOctetString().decode(private_key).payload
        return construct(curve=eddsa_oids[algo_oid], seed=seed)
    else:
        raise UnsupportedEccFeature("Unsupported ECC purpose (OID: %s)" % algo_oid)


def _import_x509_cert(encoded, *kwargs):

    sp_info = _extract_subject_public_key_info(encoded)
    return _import_subjectPublicKeyInfo(sp_info)


def _import_der(encoded, passphrase):

    try:
        return _import_subjectPublicKeyInfo(encoded, passphrase)
    except UnsupportedEccFeature as err:
        raise err
    except (ValueError, TypeError, IndexError):
        pass

    try:
        return _import_x509_cert(encoded, passphrase)
    except UnsupportedEccFeature as err:
        raise err
    except (ValueError, TypeError, IndexError):
        pass

    try:
        return _import_rfc5915_der(encoded, passphrase)
    except UnsupportedEccFeature as err:
        raise err
    except (ValueError, TypeError, IndexError):
        pass

    try:
        return _import_pkcs8(encoded, passphrase)
    except UnsupportedEccFeature as err:
        raise err
    except (ValueError, TypeError, IndexError):
        pass

    raise ValueError("Not an ECC DER key")


def _import_openssh_public(encoded):
    parts = encoded.split(b' ')
    if len(parts) not in (2, 3):
        raise ValueError("Not an openssh public key")

    try:
        keystring = binascii.a2b_base64(parts[1])

        keyparts = []
        while len(keystring) > 4:
            lk = struct.unpack(">I", keystring[:4])[0]
            keyparts.append(keystring[4:4 + lk])
            keystring = keystring[4 + lk:]

        if parts[0] != keyparts[0]:
            raise ValueError("Mismatch in openssh public key")

        # NIST P curves
        if parts[0].startswith(b"ecdsa-sha2-"):

            for curve_name, curve in _curves.items():
                if curve.openssh is None:
                    continue
                if not curve.openssh.startswith("ecdsa-sha2"):
                    continue
                middle = tobytes(curve.openssh.split("-")[2])
                if keyparts[1] == middle:
                    break
            else:
                raise ValueError("Unsupported ECC curve: " + middle)

            ecc_key = _import_public_der(keyparts[2], curve_oid=curve.oid)

        # EdDSA
        elif parts[0] == b"ssh-ed25519":
            x, y = _import_ed25519_public_key(keyparts[1])
            ecc_key = construct(curve="Ed25519", point_x=x, point_y=y)
        else:
            raise ValueError("Unsupported SSH key type: " + parts[0])

    except (IndexError, TypeError, binascii.Error):
        raise ValueError("Error parsing SSH key type: " + parts[0])

    return ecc_key


def _import_openssh_private_ecc(data, password):

    from ._openssh import (import_openssh_private_generic,
                           read_bytes, read_string, check_padding)

    key_type, decrypted = import_openssh_private_generic(data, password)

    eddsa_keys = {
        "ssh-ed25519": ("Ed25519", _import_ed25519_public_key, 32),
    }

    # https://datatracker.ietf.org/doc/html/draft-miller-ssh-agent-04
    if key_type.startswith("ecdsa-sha2"):

        ecdsa_curve_name, decrypted = read_string(decrypted)
        if ecdsa_curve_name not in _curves:
            raise UnsupportedEccFeature("Unsupported ECC curve %s" % ecdsa_curve_name)
        curve = _curves[ecdsa_curve_name]
        modulus_bytes = (curve.modulus_bits + 7) // 8

        public_key, decrypted = read_bytes(decrypted)

        if bord(public_key[0]) != 4:
            raise ValueError("Only uncompressed OpenSSH EC keys are supported")
        if len(public_key) != 2 * modulus_bytes + 1:
            raise ValueError("Incorrect public key length")

        point_x = Integer.from_bytes(public_key[1:1+modulus_bytes])
        point_y = Integer.from_bytes(public_key[1+modulus_bytes:])

        private_key, decrypted = read_bytes(decrypted)
        d = Integer.from_bytes(private_key)

        params = {'d': d, 'curve': ecdsa_curve_name}

    elif key_type in eddsa_keys:

        curve_name, import_eddsa_public_key, seed_len = eddsa_keys[key_type]

        public_key, decrypted = read_bytes(decrypted)
        point_x, point_y = import_eddsa_public_key(public_key)

        private_public_key, decrypted = read_bytes(decrypted)
        seed = private_public_key[:seed_len]

        params = {'seed': seed, 'curve': curve_name}
    else:
        raise ValueError("Unsupport SSH agent key type:" + key_type)

    _, padded = read_string(decrypted)  # Comment
    check_padding(padded)

    return construct(point_x=point_x, point_y=point_y, **params)


def _import_ed25519_public_key(encoded):
    """Import an Ed25519 ECC public key, encoded as raw bytes as described
    in RFC8032_.

    Args:
      encoded (bytes):
        The Ed25519 public key to import. It must be 32 bytes long.

    Returns:
      :class:`EccKey` : a new ECC key object

    Raises:
      ValueError: when the given key cannot be parsed.

    .. _RFC8032: https://datatracker.ietf.org/doc/html/rfc8032
    """

    if len(encoded) != 32:
        raise ValueError("Incorrect length. Only Ed25519 public keys are supported.")

    p = Integer(0x7fffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffed)  # 2**255 - 19
    d = 37095705934669439343138083508754565189542113879843219016388785533085940283555

    y = bytearray(encoded)
    x_lsb = y[31] >> 7
    y[31] &= 0x7F
    point_y = Integer.from_bytes(y, byteorder='little')
    if point_y >= p:
        raise ValueError("Invalid Ed25519 key (y)")
    if point_y == 1:
        return 0, 1

    u = (point_y**2 - 1) % p
    v = ((point_y**2 % p) * d + 1) % p
    try:
        v_inv = v.inverse(p)
        x2 = (u * v_inv) % p
        point_x = Integer._tonelli_shanks(x2, p)
        if (point_x & 1) != x_lsb:
            point_x = p - point_x
    except ValueError:
        raise ValueError("Invalid Ed25519 public key")
    return point_x, point_y


def _import_ed448_public_key(encoded):
    """Import an Ed448 ECC public key, encoded as raw bytes as described
    in RFC8032_.

    Args:
      encoded (bytes):
        The Ed448 public key to import. It must be 57 bytes long.

    Returns:
      :class:`EccKey` : a new ECC key object

    Raises:
      ValueError: when the given key cannot be parsed.

    .. _RFC8032: https://datatracker.ietf.org/doc/html/rfc8032
    """

    if len(encoded) != 57:
        raise ValueError("Incorrect length. Only Ed448 public keys are supported.")

    p = Integer(0xfffffffffffffffffffffffffffffffffffffffffffffffffffffffeffffffffffffffffffffffffffffffffffffffffffffffffffffffff)  # 2**448 - 2**224 - 1
    d = 0xfffffffffffffffffffffffffffffffffffffffffffffffffffffffeffffffffffffffffffffffffffffffffffffffffffffffffffff6756

    y = encoded[:56]
    x_lsb = bord(encoded[56]) >> 7
    point_y = Integer.from_bytes(y, byteorder='little')
    if point_y >= p:
        raise ValueError("Invalid Ed448 key (y)")
    if point_y == 1:
        return 0, 1

    u = (point_y**2 - 1) % p
    v = ((point_y**2 % p) * d - 1) % p
    try:
        v_inv = v.inverse(p)
        x2 = (u * v_inv) % p
        point_x = Integer._tonelli_shanks(x2, p)
        if (point_x & 1) != x_lsb:
            point_x = p - point_x
    except ValueError:
        raise ValueError("Invalid Ed448 public key")
    return point_x, point_y


def import_key(encoded, passphrase=None, curve_name=None):
    """Import an ECC key (public or private).

    Args:
      encoded (bytes or multi-line string):
        The ECC key to import.
        The function will try to automatically detect the right format.

        Supported formats for an ECC **public** key:

        * X.509 certificate: binary (DER) or ASCII (PEM).
        * X.509 ``subjectPublicKeyInfo``: binary (DER) or ASCII (PEM).
        * SEC1_ (or X9.62), as ``bytes``. NIST P curves only.
          You must also provide the ``curve_name`` (with a value from the `ECC table`_)
        * OpenSSH line, defined in RFC5656_ and RFC8709_ (ASCII).
          This is normally the content of files like ``~/.ssh/id_ecdsa.pub``.

        Supported formats for an ECC **private** key:

        * A binary ``ECPrivateKey`` structure, as defined in `RFC5915`_ (DER).
          NIST P curves only.
        * A `PKCS#8`_ structure (or the more recent Asymmetric Key Package, RFC5958_): binary (DER) or ASCII (PEM).
        * `OpenSSH 6.5`_ and newer versions (ASCII).

        Private keys can be in the clear or password-protected.

        For details about the PEM encoding, see `RFC1421`_/`RFC1423`_.

      passphrase (byte string):
        The passphrase to use for decrypting a private key.
        Encryption may be applied protected at the PEM level (not recommended)
        or at the PKCS#8 level (recommended).
        This parameter is ignored if the key in input is not encrypted.

      curve_name (string):
        For a SEC1 encoding only. This is the name of the curve,
        as defined in the `ECC table`_.

    .. note::

        To import EdDSA private and public keys, when encoded as raw ``bytes``, use:

        * :func:`Cryptodome.Signature.eddsa.import_public_key`, or
        * :func:`Cryptodome.Signature.eddsa.import_private_key`.

    Returns:
      :class:`EccKey` : a new ECC key object

    Raises:
      ValueError: when the given key cannot be parsed (possibly because
        the pass phrase is wrong).

    .. _RFC1421: https://datatracker.ietf.org/doc/html/rfc1421
    .. _RFC1423: https://datatracker.ietf.org/doc/html/rfc1423
    .. _RFC5915: https://datatracker.ietf.org/doc/html/rfc5915
    .. _RFC5656: https://datatracker.ietf.org/doc/html/rfc5656
    .. _RFC8709: https://datatracker.ietf.org/doc/html/rfc8709
    .. _RFC5958: https://datatracker.ietf.org/doc/html/rfc5958
    .. _`PKCS#8`: https://datatracker.ietf.org/doc/html/rfc5208
    .. _`OpenSSH 6.5`: https://flak.tedunangst.com/post/new-openssh-key-format-and-bcrypt-pbkdf
    .. _SEC1: https://www.secg.org/sec1-v2.pdf
    """

    from Cryptodome.IO import PEM

    encoded = tobytes(encoded)
    if passphrase is not None:
        passphrase = tobytes(passphrase)

    # PEM
    if encoded.startswith(b'-----BEGIN OPENSSH PRIVATE KEY'):
        text_encoded = tostr(encoded)
        openssh_encoded, marker, enc_flag = PEM.decode(text_encoded, passphrase)
        result = _import_openssh_private_ecc(openssh_encoded, passphrase)
        return result

    elif encoded.startswith(b'-----'):

        text_encoded = tostr(encoded)

        # Remove any EC PARAMETERS section
        # Ignore its content because the curve type must be already given in the key
        ecparams_start = "-----BEGIN EC PARAMETERS-----"
        ecparams_end = "-----END EC PARAMETERS-----"
        text_encoded = re.sub(ecparams_start + ".*?" + ecparams_end, "",
                              text_encoded,
                              flags=re.DOTALL)

        der_encoded, marker, enc_flag = PEM.decode(text_encoded, passphrase)
        if enc_flag:
            passphrase = None
        try:
            result = _import_der(der_encoded, passphrase)
        except UnsupportedEccFeature as uef:
            raise uef
        except ValueError:
            raise ValueError("Invalid DER encoding inside the PEM file")
        return result

    # OpenSSH
    if encoded.startswith((b'ecdsa-sha2-', b'ssh-ed25519')):
        return _import_openssh_public(encoded)

    # DER
    if len(encoded) > 0 and bord(encoded[0]) == 0x30:
        return _import_der(encoded, passphrase)

    # SEC1
    if len(encoded) > 0 and bord(encoded[0]) in b'\x02\x03\x04':
        if curve_name is None:
            raise ValueError("No curve name was provided")
        return _import_public_der(encoded, curve_name=curve_name)

    raise ValueError("ECC key format is not supported")


if __name__ == "__main__":

    import time

    d = 0xc51e4753afdec1e6b6c6a5b992f43f8dd0c7a8933072708b6522468b2ffb06fd

    point = _curves['p256'].G.copy()
    count = 3000

    start = time.time()
    for x in range(count):
        pointX = point * d
    print("(P-256 G)", (time.time() - start) / count * 1000, "ms")

    start = time.time()
    for x in range(count):
        pointX = pointX * d
    print("(P-256 arbitrary point)", (time.time() - start) / count * 1000, "ms")
