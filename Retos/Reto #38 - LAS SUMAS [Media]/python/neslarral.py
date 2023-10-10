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


def normalizar(numeros: list, limite: int) -> list:
    """
    Rearma la lista de numeros para no procesar innecesariamente.
    Ordeno la lista, elimino los valores > límite (no hay chance de que sumen)
    y apunto como resultado el valor igual al límite (tampoco tiene chance pero es un
    resultado válido).
    Si la suma de todos los elementos < limite, la lista queda vacía (sin chance por definición).
    Si el limite es impar pero no hay elementos impares, la lista queda vacía (tampoco tiene chace).
    """
    def paridad(numeros: list) -> bool:
        es_par = True
        for numero in set(numeros):
            if numero % 2 > 0:
                es_par = False
                break
        return es_par

    global resultado

    resultado.clear()

    numeros.sort()
    lista = [x for x in numeros if (limite > x > 0)]

    if sum(lista) < limite:
        print("No dan los números")
        lista = []

    if (not paridad([limite])) and paridad(lista):
        print("Con pares no se hacen impares")
        lista = []

    if numeros.__contains__(limite):
        print("Autocontenido")
        resultado.append([limite])

    return lista


def buscar(numeros: list, limite: int) -> None:
    """
    Armo una tabla de verdad y analizo que combinaciones suman el valor límite.
    Elimino las combinaciones duplicadas ([1, 2, 3] ~ [3, 2, 1] <= me quedo solo con una).
    """
    global resultado
    lista = normalizar(numeros, limite)

    if lista.__len__() > 0:
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
    else:
        print("Procesamiento evitado")

    return


resultado = []

testcases = [
    ([1, 5, 3, 6, 2, 7, 3], 6),
    ([1, 5, 1, 72, 1, 1, 7, 1, 1, 25, 18, 8, 1, 2, 9, 3, 2, 3, 4], 17),
    ([1, 5, 1, 1, 1, 1, 1, 7, 1, 2, 9, 3, 2, 3], 5),
    ([1, 6, 3], 6),
    ([1, 3], 6),
    ([2, 4, 2, 4, 2], 5),
    ([2, 4, 2, 5, 4, 2], 5),
]

for ind, tstc in enumerate(testcases):

    print(f"Caso {ind + 1} -----------------------------------------------------------------------------")
    buscar(tstc[0], tstc[1])
    print(f"{resultado.__len__()} combinaciones para el número {tstc[1]} =>\n\tlista original {tstc[0]}\n\t{resultado}")
