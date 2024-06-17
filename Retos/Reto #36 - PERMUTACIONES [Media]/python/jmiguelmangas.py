"""
 * Crea un programa que sea capaz de generar e imprimir todas las 
 * permutaciones disponibles formadas por las letras de una palabra.
 * - Las palabras generadas no tienen por qué existir.
 * - Deben usarse todas las letras en cada permutación.
 * - Ejemplo: sol, slo, ols, osl, los, lso 
 */
"""
import itertools
def permutaciones (string):
    long = len(string)
    lista = list(string)
    perm = list(itertools.permutations(lista))
    lista_palabras =[]
    for element in perm:
        word = "".join(element)
        lista_palabras.append(word)
    print(len(lista_palabras),lista_palabras)
permutaciones("cadaver")
permutaciones("gorrino")
permutaciones("casa")