#!/usr/bin/python3

"""
# Reto #4: PRIMO, FIBONACCI Y PAR
/*
 * Escribe un programa que, dado un número, compruebe y muestre si es primo, fibonacci y par.
 * Ejemplos:
 * - Con el número 2, nos dirá: "2 es primo, fibonacci y es par"
 * - Con el número 7, nos dirá: "7 es primo, no es fibonacci y es impar"
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


def esPar(number: int):
    return number % 2 == 0


def esPrimo(number: int):
    if number < 2:
        return False
    if esPar(number):
        return False
    for i in range(3, number//3, 2):
        if number % i == 0:
            return False
    return True


def esFibonacci(number: int):
    x = 1
    y = 1
    while True:
        if y == number:
            return True
        if y > number:
            return False
        y, x = x + y, y


def evaluarNumero(number: int):
    es_primo =  "es primo," if esPrimo(number) else "no es primo"
    es_fibonnaci = "es fibonacci y" if esFibonacci(number) else "no es fibonacci y"
    es_par = "es par" if esPar(number) else "no es par"
    print(number, es_primo, es_fibonnaci, es_par)


if __name__ == '__main__':
    numero = int(input("ingrese un numero: "))
    evaluarNumero(numero)

