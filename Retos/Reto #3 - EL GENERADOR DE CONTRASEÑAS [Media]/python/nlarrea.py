"""
 * Escribe un programa que sea capaz de generar contraseñas de forma aleatoria.
 * Podrás configurar generar contraseñas con los siguientes parámetros:
 * - Longitud: Entre 8 y 16.
 * - Con o sin letras mayúsculas.
 * - Con o sin números.
 * - Con o sin símbolos.
 * (Pudiendo combinar todos estos parámetros entre ellos)
"""

import random

def password_generator(n, with_upper, with_num, with_symbol):
    lower_case = "abcdefghijklmnopqrstuvwxyz"
    upper_case = "ABCDEFGHIJKLMNOPQRSTUVWXYZ"
    numbers = "0123456789"
    symbols = "~`!@#$%^&*()_-+={[}]|\\:;\"'<,>.?/"

    choices = lower_case
    if with_upper: choices += upper_case
    if with_num: choices += numbers
    if with_symbol: choices += symbols

    password = ""
    for _ in range(0,n):
        password += choices[random.randint(0, len(choices))]

    return password

print(password_generator(16, True, True, True))
print(password_generator(8, False, False, False))
print(password_generator(10, True, True, False))