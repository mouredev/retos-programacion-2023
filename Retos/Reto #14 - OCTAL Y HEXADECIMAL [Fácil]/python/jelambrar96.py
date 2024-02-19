#!/usr/bin/python3

"""
# Reto #14: Octal y Hexadecimal
/*
 * Crea una función que reciba un número decimal y lo trasforme a Octal
 * y Hexadecimal.
 * - No está permitido usar funciones propias del lenguaje de programación que
 * realicen esas operaciones directamente.
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


HEX_DIGITS = [  '0', '1', '2', '3', '4', '5', '6', '7', '8', '9', 
                'A', 'B', 'C', 'D', 'F', 'G', 'H', 'I', 'J', 'K']


def number_to_base(number: int, base:int):
    if base > len(HEX_DIGITS):
        raise ValueError("No se puede convertir a esa base")
    if number == 0:
        return HEX_DIGITS[0]
    digitos_octal = []
    while number > 0:
        digitos_octal.append(HEX_DIGITS[number % base])
        number //= base
    return "".join(reversed(digitos_octal))


def number_to_hex(number: int):
    return number_to_base(number, 16)    


def number_to_octal(number: int):
    return number_to_base(number, 8)    



if __name__ == '__main__':
    numero = int(input("introduce un numero: "))
    print("En hexadecimal:", number_to_hex(numero))
    print("En octal:", number_to_octal(numero))

