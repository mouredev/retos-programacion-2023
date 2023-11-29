"""
Reto #36: PERMUTACIONES
MEDIA | Publicación: 04/09/23 | Resolución: 18/09/23
/*
 * Crea un programa que sea capaz de generar e imprimir todas las 
 * permutaciones disponibles formadas por las letras de una palabra.
 * - Las palabras generadas no tienen por qué existir.
 * - Deben usarse todas las letras en cada permutación.
 * - Ejemplo: sol, slo, ols, osl, los, lso 
 */
 """
from itertools import permutations

def generar_permutaciones(word):

    todas_permutaciones = permutations(word)


    for permutacion in todas_permutaciones:
        print(''.join(permutacion))


w = 'hola'
generar_permutaciones(w)

