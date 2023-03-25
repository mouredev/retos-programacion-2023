#!/usr/bin/env python3
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

# Define character ASCII range for possible combinations
range_upper_letter = (65, 90)
range_lower_letter = (97, 122)
range_number = (48, 57)
range_simbols = ([33, 47], [58, 64], [91, 96], [123, 126])


def getRandomUpperLetter():
    '''Return a random character of upper case letters'''
    return random.randint(range_upper_letter[0], range_upper_letter[1])


def getRandomLowerLetter():
    '''Return a random character of lower case letters'''
    return random.randint(range_lower_letter[0], range_lower_letter[1])


def getRandomNumber():
    '''Return a random character of numbers'''
    return random.randint(range_number[0], range_number[1])


def getRandomSimbol():
    '''Return a random character of simbols'''
    random_segment = random.choice(range_simbols)
    return random.randint(random_segment[0], random_segment[1])


def generateRandomPassword(password_lenght=8, with_upper_case=False, with_number=False, with_simbols=False):
    '''Generate a random password'''
    if password_lenght < 8 or password_lenght > 16:
        print("Debe inrgesar una longitud entre 8 y 16 caracteres")
        return None

    password = ''
    options = [getRandomLowerLetter]

    if with_upper_case:
        options.append(getRandomUpperLetter)
    if with_number:
        options.append(getRandomNumber)
    if with_simbols:
        options.append(getRandomSimbol)

    while len(password) < password_lenght:
        char_code = random.choice(options)()
        password += chr(char_code)

    return password


print(generateRandomPassword(8, True, True, True))
print(generateRandomPassword(20, True, True, True))
print(generateRandomPassword(16, True, True, True))
