#!/usr/bin/python3

"""
# Reto #29: El carácter infiltrado
/*
 * Crea una función que reciba dos cadenas de texto casi iguales,
 * a excepción de uno o varios caracteres. 
 * La función debe encontrarlos y retornarlos en formato lista/array.
 * - Ambas cadenas de texto deben ser iguales en longitud.
 * - Las cadenas de texto son iguales elemento a elemento.
 * - No se pueden utilizar operaciones propias del lenguaje
 *   que lo resuelvan directamente.
 * 
 * Ejemplos:
 * - Me llamo mouredev / Me llemo mouredov -> ["e", "o"]
 * - Me llamo.Brais Moure / Me llamo brais moure -> [" ", "b", "m"]
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



def caracter_infiltrado(cadena_1, cadena_2):
    assert len(cadena_1) == len(cadena_2), "ERROR: las cadenas deben ser de igual longitud"
    caracteres_distintos = [ c2 for c1, c2 in zip(cadena_1, cadena_2) if c1 != c2 ]
    return caracteres_distintos

if __name__ == '__main__':
    
    cadena_1 = "Me llamo mouredev"
    cadena_2 = "Me llemo mouredov"
    print(cadena_1, cadena_2, sep=' - ')
    print(caracter_infiltrado(cadena_1, cadena_2))

    print()

    cadena_1 = "Me llamo.Brais Moure"
    cadena_2 = "Me llamo brais moure"
    print(cadena_1, cadena_2, sep=' - ')
    print(caracter_infiltrado(cadena_1, cadena_2))
