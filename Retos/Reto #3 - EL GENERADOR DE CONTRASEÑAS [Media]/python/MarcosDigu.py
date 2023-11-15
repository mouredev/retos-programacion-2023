"""
 * Escribe un programa que sea capaz de generar contraseñas de forma aleatoria.
 * Podrás configurar generar contraseñas con los siguientes parámetros:
 * - Longitud: Entre 8 y 16.
 * - Con o sin letras mayúsculas.
 * - Con o sin números.
 * - Con o sin símbolos.
 * (Pudiendo combinar todos estos parámetros entre ellos)
"""
import string
import random
import os

os.system('cls')

def generate_password(length, use_uppercase, use_numbers, use_symbols):
    characters = ""

    if use_uppercase:
        characters += string.ascii_uppercase
    if use_numbers:
        characters += string.digits
    if use_symbols:
        characters += "!@#$%^&*()_-+=<>?/[]{}|"

    if not any([use_uppercase, use_numbers, use_symbols]):
        # If no character type is selected, default to lowercase letters
        characters = string.ascii_lowercase

    password = ''.join(random.choice(characters) for _ in range(length))
    return password

char = int(input("Number of characters (8-16): "))
uplo = input("U: Include uppercase - L: Lowercase only: ")
num = input("Include numbers (y/n): ")
sym = input("Include symbols (y/n): ")

# Validate input for the number of characters
char = max(8, min(char, 16))

password = generate_password(char, uplo == "U", num == "y", sym == "y")

print(f"Your password is: {password}")
