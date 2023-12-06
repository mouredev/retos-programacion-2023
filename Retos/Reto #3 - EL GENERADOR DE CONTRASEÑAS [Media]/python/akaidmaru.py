"""/*
 * Escribe un programa que sea capaz de generar contraseñas de forma aleatoria.
 * Podrás configurar generar contraseñas con los siguientes parámetros:
 * - Longitud: Entre 8 y 16.
 * - Con o sin letras mayúsculas.
 * - Con o sin números.
 * - Con o sin símbolos.
 * (Pudiendo combinar todos estos parámetros entre ellos)
 */"""

import string
import random

def create_password(length, uppercase=True, numbers=True, punctuations=True):
    characters = string.ascii_lowercase
    if uppercase:
        characters += string.ascii_uppercase
    if numbers:
        characters += string.digits
    if punctuations:
        characters += string.punctuation

    if len(characters) == 0:
        raise ValueError("Debes seleccionar al menos un tipo de carácter para generar la contraseña.")
    
    password = ''.join([random.choice(characters) for _ in range(length)])
    return password

def main():
    try:
        length = int(input("¡Vamos a generar una contraseña! Selecciona una longitud de caracteres entre 8 y 16:\n>"))

        if length < 8 or length > 16:
            return print("La longitud debe ser entre 8 y 16.")
        
        uppercase = input("¿Con o sin letras mayúsculas? 'y' para sí, 'n' para no:\n>").lower()
        numbers = input("¿Con o sin números? 'y' para sí, 'n' para no:\n>").lower()
        punctuations = input("¿Con o sin símbolos? 'y' para sí, 'n' para no:\n>").lower()

        new_password = create_password(length, uppercase == 'y', numbers == 'y', punctuations == 'y')
        return print(f"Contraseña generada: {new_password}")
    except ValueError as e:
        print(f"Error: {e}")

if __name__ == "__main__":
    main()
