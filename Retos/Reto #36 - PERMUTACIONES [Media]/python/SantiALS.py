'''
/*
 * Crea un programa que sea capaz de generar e imprimir todas las 
 * permutaciones disponibles formadas por las letras de una palabra.
 * - Las palabras generadas no tienen por qué existir.
 * - Deben usarse todas las letras en cada permutación.
 * - Ejemplo: sol, slo, ols, osl, los, lso 
 */

'''

import itertools

def permutator(word)-> str:

    list_combinations = list(itertools.permutations(word))
    element = 0

    for combination in list_combinations:

        list_combinations[element] = ''.join(list_combinations[element])
        element += 1

    return ' '.join(list_combinations)



if __name__ == '__main__':

    print('\nCasos de prueba: \n')

    print(permutator('Sol'))
    print(permutator('Día'))
    print(permutator('Hilo'))