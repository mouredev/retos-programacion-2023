# Reto #36: Permutaciones
#### Dificultad: Media | Publicación: 04/09/23 | Corrección: 18/09/23

## Enunciado

'''
 * Crea un programa que sea capaz de generar e imprimir todas las 
 * permutaciones disponibles formadas por las letras de una palabra.
 * - Las palabras generadas no tienen por qué existir.
 * - Deben usarse todas las letras en cada permutación.
 * - Ejemplo: sol, slo, ols, osl, los, lso 
'''


def permuta(word):
    if len(word)<=1: 
        return word
    else:
        lista=[word]
        operation=list(word)
        for i in range(len(word)):
            operation.append(operation.pop(0))
            if ''.join(operation) not in lista:
                lista.append(''.join(operation))
        lista.append(word[::-1])
        operation=list(word[::-1])
        for i in range(len(word)):
            operation.append(operation.pop(0))
            if ''.join(operation) not in lista:
                lista.append(''.join(operation))
        return lista
print(permuta('terco'))

        
