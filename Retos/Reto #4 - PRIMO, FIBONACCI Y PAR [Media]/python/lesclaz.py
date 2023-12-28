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

def check_number(n: int) -> None:
    """
    Comprueba si un número dado es primo, Fibonacci y par.

    Argumentos:
    n (int): El número a comprobar.

    Retorna:
    None: Esta función no devuelve nada, sino que imprime la salida por consola.

    Ejemplo:
    >>> check_number(2)
    2 es primo, fibonacci y es par
    >>> check_number(7)
    7 es primo, no es fibonacci y es impar
    """
    # Comprobar si es primo
    is_prime = True
    if n <= 1 or (n > 2 and n % 2 == 0) or (n > 3 and n % 3 == 0):
        is_prime = False
    i = 5
    while i * i <= n:
        if n % i == 0 or n % (i + 2) == 0:
            is_prime = False
            break
        i += 6

    # Comprobar si es par
    is_even = n % 2 == 0

    # Comprobar si es un número de Fibonacci
    a, b = 0, 1
    is_fibonacci = False
    while b <= n:
        if b == n:
            is_fibonacci = True
            break
        a, b = b, a + b

    # Imprimir la salida por consola
    output = f"{n} "
    output += "es primo, " if is_prime else "no es primo, "
    output += "es fibonacci, " if is_fibonacci else "no es fibonacci, "
    output += "y es par" if is_even else "y es impar"
    print(output)


if __name__ == '__main__':
    check_number(5)
    check_number(26)
