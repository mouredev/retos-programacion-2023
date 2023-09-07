"""
 * Crea un programa que sea capaz de generar e imprimir todas las 
 * permutaciones disponibles formadas por las letras de una palabra.
 * - Las palabras generadas no tienen por qué existir.
 * - Deben usarse todas las letras en cada permutación.
 * - Ejemplo: sol, slo, ols, osl, los, lso 
"""
import math, random


def permutacion (word:str):
    try:
        result = []
        long = len(word)
        total = math.factorial(long)
        
        while len(result) < total:
            permu = "".join(random.sample(word, len(word)))
            if permu in result:
                pass
            else:
                result.append(permu)
        return result
    except:
        return("ERROR")
print(permutacion("abc"))
