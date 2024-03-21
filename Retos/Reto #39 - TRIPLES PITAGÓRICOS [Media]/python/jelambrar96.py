#!/usr/bin/python3

"""
# Reto #39: Triples pitagóricos
/*
 * Crea una función que encuentre todos los triples pitagóricos
 * (ternas) menores o iguales a un número dado.
 * - Debes buscar información sobre qué es un triple pitagórico.
 * - La función únicamente recibe el número máximo que puede
 *   aparecer en el triple.
 * - Ejemplo: Los triples menores o iguales a 10 están
 *   formados por (3, 4, 5) y (6, 8, 10).
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



def es_pitagorico(a: int, b: int, c: int):
    return a ** 2 + b ** 2 == c ** 2


def triples_pitagoricos(n: int):
    lista = []
    for i in range(1, n + 1):
        for j in range(1, i):
            for k in range(1, j + 1):
                 if i**2 == j**2 + k**2:
                     lista.append((k, j, i))
    return lista


if __name__ == '__main__':
    n = 100
    print("n:", n)
    for item in triples_pitagoricos(n):
        # power2 = tuple( x**2 for x in item )
        # print(item, power2)
        print(item)


