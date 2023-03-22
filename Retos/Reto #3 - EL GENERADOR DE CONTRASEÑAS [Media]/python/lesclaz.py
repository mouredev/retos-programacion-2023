#!/usr/bin/env python3
# -*- coding: utf-8 -*-

# Copyright (c) 2023 Lesly Cintra Laza <a.k.a. lesclaz>

# Permission is hereby granted, free of charge, to any person obtaining a copy
# of this software and associated documentation files (the "Software"), to deal
# in the Software without restriction, including without limitation the rights
# to use, copy, modify, merge, publish, distribute, sublicense, and/or sell
# copies of the Software, and to permit persons to whom the Software is
# furnished to do so, subject to the following conditions:

# The above copyright notice and this permission notice shall be included in
# all copies or substantial portions of the Software.

# THE SOFTWARE IS PROVIDED "AS IS", WITHOUT WARRANTY OF ANY KIND, EXPRESS OR
# IMPLIED, INCLUDING BUT NOT LIMITED TO THE WARRANTIES OF MERCHANTABILITY,
# FITNESS FOR A PARTICULAR PURPOSE AND NONINFRINGEMENT. IN NO EVENT SHALL THE
# AUTHORS OR COPYRIGHT HOLDERS BE LIABLE FOR ANY CLAIM, DAMAGES OR OTHER
# LIABILITY, WHETHER IN AN ACTION OF CONTRACT, TORT OR OTHERWISE, ARISING FROM,
# OUT OF OR IN CONNECTION WITH THE SOFTWARE OR THE USE OR OTHER DEALINGS IN THE
# SOFTWARE.

import secrets
import string
import random


_characters = []


def __calculate_pws_lenght(
        spesific_lenght: int,
        lower_count: int,
        upper_count: int,
        digits_count: int,
        symbols_count: int
) -> int:
    count = 0
    if lower_count:
        count += lower_count
    if upper_count:
        count += upper_count
    if digits_count:
        count += digits_count
    if symbols_count:
        count += symbols_count
    
    return spesific_lenght if spesific_lenght and spesific_lenght > count else count


def main(
        lenght: int = 8,
        lower: tuple[bool, int] = (True, 2),
        upper: tuple[bool, int] = (True, 2),
        digits: tuple[bool, int] = (True, 2),
        symbols: tuple[bool, int] = (True, 2)
) -> str:
    _use_lower, _lower_count = lower
    pwd_content = []
    if _use_lower:
        _characters.extend(string.ascii_lowercase)
        if not _lower_count or type(_lower_count) != int:
            _lower_count = 2
        for _ in range(_lower_count):
            pwd_content.append(secrets.choice(string.ascii_lowercase))
    _use_upper, _upper_count = upper
    if _use_upper:
        _characters.extend(string.ascii_uppercase)
        if not _upper_count or type(_upper_count) != int:
            _upper_count = 2
        for _ in range(_upper_count):
            pwd_content.append(secrets.choice(string.ascii_uppercase))
    _use_digits, _digits_count = digits
    if _use_digits:
        _characters.extend(string.digits)
        if not _digits_count or type(_digits_count) != int:
            _digits_count = 2
        for _ in range(_digits_count):
            pwd_content.append(secrets.choice(string.digits))
    _use_symbols, _symbols_count = symbols
    if _use_symbols:
        _characters.extend(string.punctuation)
        if not _symbols_count or type(_symbols_count) != int:
            _symbols_count = 2
        for _ in range(_symbols_count):
            pwd_content.append(secrets.choice(string.punctuation))

    pwd_lenght = __calculate_pws_lenght(
        spesific_lenght=lenght,
        lower_count=_lower_count,
        upper_count=_upper_count,
        digits_count=_digits_count,
        symbols_count=_symbols_count
    )

    if len(pwd_content) < pwd_lenght:
        for _ in range(pwd_lenght - len(pwd_content)):
            pwd_content.append(secrets.choice(_characters))
    pwd = ''
    for _ in range(pwd_lenght):
        _index = random.randint(0, len(pwd_content) - 1)
        pwd += pwd_content[_index]
        pwd_content.pop(_index)

    return pwd


if __name__ == '__main__':
    print(main(lenght=12))
