'''
 * Escribe un programa que sea capaz de generar contraseñas de forma aleatoria.
 * Podrás configurar generar contraseñas con los siguientes parámetros:
 * - Longitud: Entre 8 y 16.
 * - Con o sin letras mayúsculas.
 * - Con o sin números.
 * - Con o sin símbolos.
 * (Pudiendo combinar todos estos parámetros entre ellos)
'''

import random
import string

def generate_password(length: int, include_uppercase: bool, include_numbers: bool, include_symbols: bool) -> str:
    characters = ''
    if length < 8 or length > 16:
        raise ValueError('Invalid Length (8-16)')

    if include_uppercase:
        characters += string.ascii_uppercase
    if include_numbers:
        characters += string.digits
    if include_symbols:
        characters += string.punctuation
    if not characters:
        characters = string.ascii_letters + string.digits + string.punctuation

    password = ''.join(random.sample(characters, length))
    return password


print(generate_password(12, True, True, True))
