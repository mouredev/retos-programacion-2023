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

length = input("Longitud entre 8 y 16 caracteres: ")

if not int(length) in range(8, 17):
    print("Introduzca un valor válido")

uppercase = input("Contiene mayusculas (Y / N): ")
uppercase = True if uppercase.lower() == "y" else False

digits = input("Contiene números (Y / N): ")
digits = True if digits.lower() == "y" else False

symbols = input("Contiene símbolos (Y / N): ")
symbols = True if symbols.lower() == "y" else False

def generate_password(length, uppercase, digits, symbols):
    password_chars = ""
    if uppercase:
        password_chars += string.ascii_uppercase
    if digits:
        password_chars += string.digits
    if symbols:
        password_chars += string.punctuation
    if not uppercase and not digits and not symbols:
        password_chars += string.ascii_letters + string.digits + string.punctuation
    return ''.join(random.choice(password_chars) for _ in range(length))

# Ejemplo de uso
password = generate_password(int(length), uppercase, digits, symbols)
print(f"\nLa password generada es: {password}")