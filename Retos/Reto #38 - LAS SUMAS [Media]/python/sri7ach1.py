'''
 * Crea una función que encuentre todas las combinaciones de los números
 * de una lista que suman el valor objetivo.
 * - La función recibirá una lista de números enteros positivos
 *   y un valor objetivo.
 * - Para obtener las combinaciones sólo se puede usar
 *   una vez cada elemento de la lista (pero pueden existir
 *   elementos repetidos en ella).
 * - Ejemplo: Lista = [1, 5, 3, 2],  Objetivo = 6
 *   Soluciones: [1, 5] y [1, 3, 2] (ambas combinaciones suman 6)
 *   (Si no existen combinaciones, retornar una lista vacía)
'''


def searchCombo(list,objetive):
    def rev(remaining, currentCombo, startIndex):
        if remaining == 0:
            result.append(currentCombo[:])
            return
        if remaining < 0:
            return
        for i in range(startIndex, len(list)):
            currentCombo.append(list[i])
            rev(remaining - list[i], currentCombo, i + 1)
            currentCombo.pop()

    result = []
    rev(objetive, [], 0)
    return result

list=[1,5,3,2,-1]
objetive=11
print(searchCombo(list, objetive))
# Debería imprimir: [[1, 5, 3, 2]]