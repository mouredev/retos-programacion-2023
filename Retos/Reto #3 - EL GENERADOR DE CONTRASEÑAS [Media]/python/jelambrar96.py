#!/usr/bin/python3
"""
/*
 * Escribe un programa que sea capaz de generar contraseñas de forma aleatoria.
 * Podrás configurar generar contraseñas con los siguientes parámetros:
 * - Longitud: Entre 8 y 16.
 * - Con o sin letras mayúsculas.
 * - Con o sin números.
 * - Con o sin símbolos.
 * (Pudiendo combinar todos estos parámetros entre ellos)
 */
"""
__author__ = "Jorge Lambraño - jelambrar96"
__copyright__ = "Copyright 2024, retos-programacion-2023"
__credits__ = ["Brais Moure - mouredev"]
__license__ = "GPL"
__version__ = "1.0.1"
__maintainer__ = "Jorge Lambraño"
__email__ = "jelambrar@gmail.com"
__status__ = "Production"

import random
import string


def check_number(password):
    for c in password:
        if c.isnumeric():
            return True
    return False


def check_uppercase(password):
    for c in password:
        if c.isupper():
            return True
    return False


def check_symbol(password):
    for c in password:
        if not c.isalpha():
            return True
    return False


def check_password(password, length, use_uppercase, use_numbers, use_symbols):
    if len(password) != length and length is not None:
        return False
    if use_numbers:
        if not check_number(password):
            return False
    if use_symbols:
        if not check_symbol(password):
            return False
    if use_uppercase:
        if not check_uppercase(password):
            return False
    return True


def password_generator(length=None, use_uppercase=True, use_numbers=True, use_symbols=True):

    length = length if length is not None else random.randint(8,16)
    list_parameters = list(string.ascii_lowercase)

    if use_uppercase:
        list_parameters.extend(list(string.ascii_uppercase))
    if use_numbers:
        list_parameters.extend(list(string.digits))
    if use_symbols:
        list_parameters.extend(list(string.punctuation))

    password_char_list = random.choices(list_parameters, k=length)
    return "".join(password_char_list)


def create_password(length=None, use_uppercase=True, use_numbers=True, use_symbols=True):
    while True:
        password = password_generator(length=length, use_uppercase=use_uppercase, 
                                        use_numbers=use_numbers, use_symbols=use_symbols)
        check_flag = check_password(password=password, length=length, 
                                        use_uppercase=use_uppercase, use_numbers=use_numbers, 
                                        use_symbols=use_symbols)
        if check_flag:
            break
    return password


if __name__ == '__main__':

    length=None
    use_uppercase=True 
    use_numbers=True
    use_symbols=True
    for i in range(8,17):
        password = create_password(length=i, use_uppercase=True, use_numbers=True, use_symbols=True)
        print(password)

