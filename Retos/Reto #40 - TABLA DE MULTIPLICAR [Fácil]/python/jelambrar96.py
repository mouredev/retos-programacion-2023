#!/usr/bin/python3

"""
# Reto #40: Tabla de multiplicar
/*
 * Crea un programa que sea capaz de solicitarte un número y se
 * encargue de imprimir su tabla de multiplicar entre el 1 y el 10.
 * - Debe visualizarse qué operación se realiza y su resultado.
 *   Ej: 1 x 1 = 1
 *       1 x 2 = 2
 *       1 x 3 = 3
 *       ... 
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

def tabla_multiplicar(numero: int):
    for i in range(1, 11):
        print(f"{numero} x {i} = {numero * i}")


if __name__ == '__main__':

    print("Tablas del multiplicar del 1 al 10\n")

    for i in range(1,11):
        tabla_multiplicar(i)
        print()
