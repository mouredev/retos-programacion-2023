#!/usr/bin/python3

"""
# Reto #32: La Columna de Excel
/*
 * Crea una función que calcule el número de la columna de una hoja de Excel
 * teniendo en cuenta su nombre.
 * - Las columnas se designan por letras de la "A" a la "Z" de forma infinita.
 * - Ejemplos: A = 1, Z = 26, AA = 27, CA = 79.
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


CADENA_CARACTERES = "ABCDEFGHIJKLMNOPQRSTUVWXYZ"
LEN = len(CADENA_CARACTERES)


def numero_columna(columna: str):
    valores_caracteres = [ CADENA_CARACTERES.index(c) + 1 for c in reversed(columna) ]
    if 0 in valores_caracteres:
        raise ValueError(f"No se puede convertir la columna con nombre {columna}")
    numero_columna = sum([ (LEN ** i) * item for i, item in enumerate(valores_caracteres) ])
    return numero_columna

if __name__ == '__main__':

    print("columna: A:", "value: ", numero_columna('A'))
    assert numero_columna('A') == 1, "ERROR: numero_columna('A')"

    print("columna: Z:", "value: ", numero_columna('Z'))
    assert numero_columna('Z') == 26, "ERROR: numero_columna('Z')"

    print("columna: AA:", "value: ", numero_columna('AA'))
    assert numero_columna('AA') == 27, "ERROR: numero_columna('AA')"

    print("columna: CA:", "value: ", numero_columna('CA'))
    assert numero_columna('CA') == 79, "ERROR: numero_columna('CA')"

