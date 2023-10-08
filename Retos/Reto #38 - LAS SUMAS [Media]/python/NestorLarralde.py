"""
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
"""


def normalizar(lista: list, limite: int) -> list:
    """
    Ordeno la lista, elimino los valores > límite (no hay chance de que sumen)
    y apunto como resultado el valor igual al límite (tampoco tiene chance pero es un
    resultado válido).
    """
    global resultado

    lista.sort()
    lista = [x for x in lista if x > limite]
    if lista.__contains__(limite):
        resultado.append([limite])

    return lista


def buscar(lista: list, limite: int) -> list:
    """
    Armo una tabla de verdad y analizo que combinaciones suman el valor límite.
    Elimino las combinaciones duplicadas ([1, 2, 3] ~ [3, 2, 1] <= me quedo solo con una).
    """
    global resultado

    for row in range(0, pow(2, lista.__len__())):
        val = bin(row)[2:].zfill(lista.__len__())
        suma = 0
        for ind, digit in enumerate(val):
            suma += int(digit) * lista[ind]
        if suma == limite:
            arr = [lista[ind] for ind, digit in enumerate(val) if digit == '1']
            arr.sort()
            if not resultado.__contains__(arr):
                resultado.append(arr)

    return resultado


resultado = []
print(buscar([1, 5, 3, 6, 2, 7, 3], 6))
resultado = []
print(buscar([1, 5, 1, 1, 1, 7, 1, 1, 8, 1, 2, 9, 3, 2, 3, 4], 8))
resultado = []
print(buscar([1, 5, 1, 1, 1, 1, 1, 7, 1, 2, 9, 3, 2, 3], 5))
