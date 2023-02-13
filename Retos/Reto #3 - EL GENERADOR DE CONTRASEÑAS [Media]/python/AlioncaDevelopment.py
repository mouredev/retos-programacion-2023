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
import string

def generate_password(length=12, use_uppercase=True, use_numbers=True, use_symbols=True):
    # Validar la longitud de la contraseña
    if not 8 <= length <= 16:
        Print("Error: la longitud de la contraseña debe estar entre 8 y 16")
        return
    # Crear una lista de caracteres permitidos
    characters = ''
    if use_uppercase:
        characters += string.ascii_uppercase
    if use_numbers:
        characters += string.digits
    if use_symbols:
        characters += string.punctuation
    if not (use_uppercase or use_numbers or use_symbols):
        characters += string.ascii_lowercase
    # Generar una contraseña aleatoria utilizando los caracteres permitidos
    password = ''.join(random.choice(characters) for _ in range(length))
    return password

# Ejemplo de uso
password = generate_password()
print(password)
