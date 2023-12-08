# /*
#  * Crea una función que encuentre todas las combinaciones de los números
#  * de una lista que suman el valor objetivo.
#  * - La función recibirá una lista de números enteros positivos
#  *   y un valor objetivo.
#  * - Para obtener las combinaciones sólo se puede usar
#  *   una vez cada elemento de la lista (pero pueden existir
#  *   elementos repetidos en ella).
#  * - Ejemplo: Lista = [1, 5, 3, 2],  Objetivo = 6
#  *   Soluciones: [1, 5] y [1, 3, 2] (ambas combinaciones suman 6)
#  *   (Si no existen combinaciones, retornar una lista vacía)
#  */

def encuentra_combinacion(lista, objetivo):
    def encontrar_combinaciones_actuales(índice, objetivo_actual, combinación_actual):
        if objetivo_actual == 0:
            combinaciones.append(combinación_actual)
            return
        if índice >= len(lista) or objetivo_actual < 0:
            return

        encontrar_combinaciones_actuales(índice + 1, objetivo_actual - lista[índice], combinación_actual + [lista[índice]])
        encontrar_combinaciones_actuales(índice + 1, objetivo_actual, combinación_actual)

    combinaciones = []
    encontrar_combinaciones_actuales(0, objetivo, [])
    return combinaciones

# Ejemplo de uso
lista = [1, 5, 8, 2, 7, 9, 3, 3]
objetivo = 6
resultados = encuentra_combinacion(lista, objetivo)
print(resultados)


