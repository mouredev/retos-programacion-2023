#!/usr/bin/python3

"""
# Reto #27: Cuenta atrás
/*
 * Crea una función que reciba dos parámetros para crear una cuenta atrás.
 * - El primero, representa el número en el que comienza la cuenta.
 * - El segundo, los segundos que tienen que transcurrir entre cada cuenta.
 * - Sólo se aceptan números enteros positivos.
 * - El programa finaliza al llegar a cero.
 * - Debes imprimir cada número de la cuenta atrás.
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

from time import sleep

def cuenta_atras(numero: int, delay: int):
    assert numero >= 0 and delay >= 0, "Error: MUST BE numero >= 0 and delay >= 0"
    # print(numero, end='\r')
    for i in range(numero, -1, -1):
        print(i, end='\r')
        sleep(delay)
    print("", end="")


if __name__ == '__main__':
    cuenta_atras(5, 1)

