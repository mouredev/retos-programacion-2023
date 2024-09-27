# /*
#  * Escribe un programa que sea capaz de generar contraseñas de forma aleatoria.
#  * Podrás configurar generar contraseñas con los siguientes parámetros:
#  * - Longitud: Entre 8 y 16.
#  * - Con o sin letras mayúsculas.
#  * - Con o sin números.
#  * - Con o sin símbolos.
#  * (Pudiendo combinar todos estos parámetros entre ellos)
#  */

import random

def generate_password():
    long = int(input('Escoja una longitud entre 8 y 16 caracteres: '))

    caracters = 'abcdefghijklmnopqrstuvwxyz'
    uppers = 'ABCDEFGHIJKLMNOPQRSTUVWXYZ'
    numbers = '0123456789'
    symbols = '!@#$%^&*()_+[]|;:,.<>?'
    password = ''

    if 8 < long < 16:
        contains_uppers = input('¿La contraseña contendra mayusculas? y/n: ')
        constains_numbers = input('¿La contraseña contendra numeros? y/n: ')
        contains_symbols = input('¿La contraseña contedra simbolos especiales? y/n: ')

        if contains_uppers == 'y':
            caracters += uppers
        if constains_numbers == 'y':
            caracters += numbers
        if contains_symbols == 'y':
            caracters += symbols

        for _ in range(long):
            password += random.choice(caracters)
        return password
    print('La cantidad de caracteres debe estar entre 8 y 16 de longitud')


print(generate_password())