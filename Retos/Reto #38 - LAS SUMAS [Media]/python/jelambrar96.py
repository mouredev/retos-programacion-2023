#!/usr/bin/python3

# ```
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
# ```

__author__ = "Jorge Lambraño - jelambrar96"
__copyright__ = "Copyright 2024, retos-programacion-2023"
__credits__ = ["Brais Moure - mouredev"]
__license__ = "GPL"
__version__ = "1.0.1"
__maintainer__ = "Jorge Lambraño"
__email__ = "jelambrar@gmail.com"
__status__ = "Production"



from itertools import combinations

def suma_lista(lista, objetivo):
	soluciones = []
	len_lista = len(lista)
	for i in range(1, len_lista):
		for item in combinations(lista, i):
			if sum(item) == objetivo:
				soluciones.append(list(item))
	return soluciones


if __name__ == '__main__':
	lista = [1, 5, 3, 2]
	objetivo = 6
	soluciones = suma_lista(lista, objetivo)
	print("soluciones")
	for item in soluciones:
		print(item)
