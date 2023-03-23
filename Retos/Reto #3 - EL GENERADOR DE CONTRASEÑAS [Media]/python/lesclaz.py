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

import random
import string


def generate_password(length=8, uppercase=True, numbers=True, specials=0):
    """
    Genera una contraseña aleatoria de la longitud especificada con opciones para incluir letras mayúsculas, números y caracteres especiales.

    Parámetros:
    length (int): La longitud de la contraseña. El valor por defecto es 8.
    uppercase (bool): Indica si la contraseña puede tener letras mayúsculas o no. El valor por defecto es True.
    numbers (bool): Indica si la contraseña puede tener números o no. El valor por defecto es True.
    specials (int): Indica el número exacto de caracteres especiales que debe tener la contraseña. El valor por defecto es 0.

    Retorna:
    str: Una contraseña aleatoria generada.

    Ejemplo:
    >>> generate_password(length=12, uppercase=True, numbers=True, specials=2)
    '#AZV[98LzCBW'
    """
    if length < 8 or length > 16:
        raise ValueError("La longitud debe estar entre 8 y 16 caracteres.")
    characters = string.ascii_lowercase
    if uppercase:
        characters += string.ascii_uppercase
    if numbers:
        characters += string.digits
    specials = min(specials, length)
    special_chars = random.sample(string.punctuation, specials)
    password_chars = random.sample(characters, length - specials)
    password_chars.extend(special_chars)
    random.shuffle(password_chars)
    password = "".join(password_chars)
    return password


if __name__ == '__main__':
    print(generate_password(
        length=12,
        specials=2
    ))
