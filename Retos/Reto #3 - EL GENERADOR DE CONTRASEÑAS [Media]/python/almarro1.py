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
import sys

arguments = sys.argv[1:]

lowercaseAlphabet = 'abcdefghijklmnopqrstuvwxyz'
uppercaseAlphabet = lowercaseAlphabet.upper()
numbers = '1234567890'
symbols = '\\!|"@·#$%&/()=?¿\'¡<>,;.:-_ç`+^*¨}{[]'


def password_generator(length: int = 8, with_numbers: bool = False, with_upper: bool = False, with_symbols: bool = False) -> str:
    alphabet = lowercaseAlphabet
    if with_numbers:
        alphabet += numbers
    if with_upper:
        alphabet += uppercaseAlphabet
    if with_symbols:
        alphabet += symbols

    characters = [letter for letter in alphabet]
    random.shuffle(characters)
    password = "".join(characters[0:length])
    # TODO: falta verificar que se cumplan las especificaciones
    while not verify_specs(password, with_numbers, with_upper, with_symbols):
        random.shuffle(characters)
        password = "".join(characters[0:length])
    return password


def verify_specs(password: str, with_numbers: bool, with_upper: bool, with_symbols: bool):
    _lower = [letter for letter in lowercaseAlphabet]
    for letter in password:
        if letter in _lower:
            break
    else:
        # print('Sin minúsculas')
        return False
    if with_numbers:
        _numbers = [number for number in numbers]
        for letter in password:
            if letter in _numbers:
                break
        else:
            # print('Sin números')
            return False
    if with_upper:
        _upper = [letter for letter in uppercaseAlphabet]
        for letter in password:
            if letter in _upper:
                break
        else:
            # print('Sin mayúsculas')
            return False
    if with_symbols:
        _symbols = [symbol for symbol in symbols]
        for letter in password:
            if letter in _symbols:
                break
        else:
            # print('Sin símbolos')
            return False

    return True


with_upper = False
with_symbols = False
with_numbers = False
length = 8

if '-h' in arguments:
    print('''\
  comando -h -s -n -u N
      -h  Muestra esta ayuda
      -s  Inserta símbolos
      -n  Inserta números
      -u  Inserta mayúsculas
       N  Número de caracteres. Debe ser un número entre 8 y 16
    ''')
    sys.exit(0)

if '-u' in arguments:
    with_upper = True
    arguments.remove('-u')

if '-s' in arguments:
    with_symbols = True
    arguments.remove('-s')

if '-n' in arguments:
    with_numbers = True
    arguments.remove('-n')

if len(arguments) > 1:
    print('Demasiados parámetros')
    sys.exit(-1)
try:
    length = int(arguments[0]) if len(arguments) == 1 else 8
    if length < 8 or length > 16:
        print(
            f'La longitud debe ser un número entre 8 y 16. Especificaste {length}')
        sys.exit(-1)
except Exception:
    print(f'Longitud errónea {arguments[0]}')
    sys.exit(-1)

print(
    f'Ejecutando con longitud={length}, números={with_numbers}, mayúsculas={with_upper}, símbolos={with_symbols}')
print(password_generator(length, with_numbers, with_upper, with_symbols))
