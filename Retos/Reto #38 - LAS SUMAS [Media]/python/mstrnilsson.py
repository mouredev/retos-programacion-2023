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

import itertools

def combination(num: list, target: int):
    sumlist = ()
    comb = 0
    for ele in range(len(num)+1):
        for iterable in itertools.combinations(num, ele):
            for i in iterable:
                if iterable[:-1] == ():
                    next
                else:
                    if target == sum(list(iterable)) and list(iterable) != sumlist:
                        sumlist = (list(iterable))
                        print(sumlist)
                        comb += 1
    if comb == 0:
        print(list(sumlist))
               

if __name__ == "__main__":
    combination([1, 5, 3, 2], 6)
    
    