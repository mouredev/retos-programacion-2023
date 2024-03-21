#!/usr/bin/python3

"""
Reto #36: Permutaciones
/*
 * Crea un programa que sea capaz de generar e imprimir todas las 
 * permutaciones disponibles formadas por las letras de una palabra.
 * - Las palabras generadas no tienen por qué existir.
 * - Deben usarse todas las letras en cada permutación.
 * - Ejemplo: sol, slo, ols, osl, los, lso 
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


from itertools import permutations


def permutaciones_palabra(cadena: str):
    return [ "".join(item) for item in permutations(cadena) ]

def mostrar_permutaciones_palabra(cadena: str, sep=' - ', end='\n'):
    permutaciones = permutaciones_palabra(cadena)
    print(*permutaciones, sep=sep, end=end)


if __name__ == '__main__':
    palabras = ['hola', 'sol', 'love', 'roma']

    for p in palabras:
        print(p)
        mostrar_permutaciones_palabra(p)
        print()


