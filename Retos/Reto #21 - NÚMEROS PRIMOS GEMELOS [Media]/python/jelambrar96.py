#!/usr/bin/python3

"""
# Reto #21: Números primos gemelos
/*
 * Crea un programa que encuentre y muestre todos los pares de números primos
 * gemelos en un rango concreto.
 * El programa recibirá el rango máximo como número entero positivo.
 * 
 * - Un par de números primos se considera gemelo si la diferencia entre
 *   ellos es exactamente 2. Por ejemplo (3, 5), (11, 13)
 *
 * - Ejemplo: Rango 14
 *   (3, 5), (5, 7), (11, 13)
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


def primes_in_range(n: int):
    """Aplica el algoritmo de la criba de eratosteles para encontrar de la forma
    mas eficiente los numeros primos dentro de un rango de 2 hasta n - 1

    Parameters:
    n (int): Limite por derecha del rango (no incluido)

    Returns:
    list_numbers (list): lista de numeros primos desde 2 hasta n - 1 ordenados 
    ascendentemente
    """
    list_numbers = list(range(2,n,1))
    list_index = 0
    while list_index < len(list_numbers):
        list_element = list_numbers[list_index]
        aux_index = list_index + 1
        while aux_index < len(list_numbers):
            if list_numbers[aux_index] % list_element == 0:
                list_numbers.pop(aux_index)
            else:
                aux_index += 1
        list_index += 1
    return list_numbers


def get_pairs(list_numbers):
    """De una lista de numeros ordenado ascendentemente retorna un lista de
    tuplas con aquellas parejas cuya diferencia es 2

    Parameters:
    list_numbers (list): lista de numeros ordenados ascendentemente

    Returns:
    list_out (list): lista de parejas encontradas en la lista de entrada
    """
    list_out = []
    for i, item in enumerate(list_numbers[0:-1:1]):
        if (item + 2) == list_numbers[i + 1]:
            list_out.append((item, item + 2))
    return list_out


def pairs_primes_in_range(n:int):
    return get_pairs(primes_in_range(n))


if __name__ == '__main__':

    n = 20
    print(f"para n = {n}")
    print(pairs_primes_in_range(n))

    n = 100
    print(f"para n = {n}")
    print(pairs_primes_in_range(n))

