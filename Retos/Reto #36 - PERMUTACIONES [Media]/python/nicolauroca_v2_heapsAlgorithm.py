#!/usr/bin/env python
# -*- coding: utf-8 -*-

#=========================================================#
#                      Información                        #
#=========================================================#

'''
/*
 * Crea un programa que sea capaz de generar e imprimir todas las 
 * permutaciones disponibles formadas por las letras de una palabra.
 * - Las palabras generadas no tienen por qué existir.
 * - Deben usarse todas las letras en cada permutación.
 * - Ejemplo: sol, slo, ols, osl, los, lso 
 */
'''

#=========================================================#
#                        Módulos                          #
#=========================================================#
# Ninguno

#=========================================================#
#                   Variables Globales                    #
#=========================================================#
# Ninguna

#=========================================================#
#                        Funciones                        #
#=========================================================#

def permutaciones(palabra):
    """
    Genera todas las permutaciones únicas de una cadena de caracteres dada utilizando el algoritmo de Heap.
    Esta función no la he creado de cero, se basa en la creada a mano (archivo v1)
    pero aplicando ejemplos de permutaciones con dicho algoritmo:
    https://www.geeksforgeeks.org/heaps-algorithm-for-generating-permutations/

    Args:
        palabra (str): La cadena de caracteres de entrada para la cual se generarán las permutaciones.

    Returns:
        set: Un conjunto que contiene todas las permutaciones únicas de la cadena de entrada.

    Ejemplo:
        >>> resultado = permutaciones("abcd")
    
    Un poco de info (créditos -> Google :D)
    El algoritmo de Heap, también conocido como Heap's algorithm,
    se utiliza para generar todas las permutaciones posibles
    de una secuencia de elementos en un orden específico.

    Este algoritmo es más eficiente en términos de tiempo y memoria que otros enfoques recursivos.

    El algoritmo funciona de la siguiente manera:
    
    1. Si la longitud de la secuencia es 1, se devuelve la secuencia como una permutación.
    2. De lo contrario, para cada elemento de la secuencia, se realiza lo siguiente:
        - Se generan todas las permutaciones de la secuencia restante.
        - Si la longitud de la secuencia es par, se intercambia el elemento actual con el último elemento.
        - Si la longitud de la secuencia es impar, se intercambia el primer elemento con el último elemento.
    3. Se repite el proceso recursivo hasta que se hayan generado todas las permutaciones posibles.

    Este algoritmo garantiza que todas las permutaciones únicas se generen de manera eficiente y sin duplicados.

    Referencias:
    - Explicación detallada del algoritmo de Heap: https://en.wikipedia.org/wiki/Heap%27s_algorithm
    - Implementación y explicación en Python: https://en.wikipedia.org/wiki/Heap%27s_algorithm#Example_Python_code
    """
    def heaps_algorithm(n, A):
        if n == 1:
            yield ''.join(A)
        else:
            for i in range(n - 1):
                yield from heaps_algorithm(n - 1, A)
                if n % 2 == 0:
                    A[i], A[n - 1] = A[n - 1], A[i]
                else:
                    A[0], A[n - 1] = A[n - 1], A[0]
            yield from heaps_algorithm(n - 1, A)

    palabra = list(palabra)
    return set(heaps_algorithm(len(palabra), palabra))


#=========================================================#
#                         Código                          #
#=========================================================#

if __name__ == '__main__':
    print(permutaciones('solasdasdasd'))