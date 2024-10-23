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

 Usar una tabla de de Morgan parece menos eficiente que usar el backtrace (recursividad) pero, sorprendentemente (al menos para mí), no lo fue:
     para 10.000 iteraciones mejora la versión backtrace en 1 segundo (backtrace 6 y tabla de Morgan 5).
     para 100.000 iteraciones mejora la versión backtrace en 19 segundos (backtrace 65 y tabla de Morgan 46).
"""
from datetime import datetime


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
        # print("No dan los números")
        lista = []

    if (not paridad([limite])) and paridad(lista):
        # print("Con pares no se hacen impares")
        lista = []

    if numeros.__contains__(limite):
        # print("Autocontenido")
        resultado.append([limite])

    return set(lista)                           # si no devuelvo set uso los repetidos => más combinaciones => tarda más


def buscar(numeros: list, limite: int) -> None:
    """
    Normalizo la lista de entrada para sacar los elementos que NO aportan.
    Armo una tabla de verdad y analizo que combinaciones suman el valor límite.
    Elimino las combinaciones duplicadas ([1, 2, 3] ~ [3, 2, 1] <= me quedo solo con una).
    """
    global resultado
    lista = list(normalizar(numeros, limite))

    if lista.__len__() > 0:
        for decimal in range(0, pow(2, lista.__len__())):      # lista de combinaciones posibles en binario
            binario = bin(decimal)[2:].zfill(lista.__len__())  # numero pasado a binario (con ceros izquierdos)
            suma = 0
            for ind, digit in enumerate(binario):
                suma += int(digit) * lista[ind]                # los "1" suman
            if suma == limite:                                 # tomo la combinaciones que resulten en el nro limite
                arr = [lista[ind] for ind, digit in enumerate(binario) if digit == '1']  # tomo los nros con valor "1"
                arr.sort()                                     # ordeno para que [2, 1] se transforme en [1, 2]
                if not resultado.__contains__(arr):            # registro solo combinaciones distintas
                    resultado.append(arr)
    else:
        pass  # print("Procesamiento evitado")

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

print(datetime.now().strftime("%H:%M:%S"))
for i in range(0, 100000):
    for ind, tstc in enumerate(testcases):

        # print(f"Caso {ind + 1} -----------------------------------------------------------------------------")
        buscar(tstc[0], tstc[1])
        # print(f"{resultado.__len__()} combinaciones para el número {tstc[1]} =>\n\tlista original {tstc[0]}\n\t{resultado}")
print(datetime.now().strftime("%H:%M:%S"))
