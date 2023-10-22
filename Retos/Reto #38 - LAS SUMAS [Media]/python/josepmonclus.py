'''
/*
Crea una función que encuentre todas las combinaciones de los números
de una lista que suman el valor objetivo.
- La función recibirá una lista de números enteros positivos
  y un valor objetivo.
- Para obtener las combinaciones sólo se puede usar
  una vez cada elemento de la lista (pero pueden existir
  elementos repetidos en ella).
- Ejemplo: Lista = [1, 5, 3, 2],  Objetivo = 6
  Soluciones: [1, 5] y [1, 3, 2] (ambas combinaciones suman 6)
  (Si no existen combinaciones, retornar una lista vacía)
'''

def find_sum(list: [], target: int):
    sums = _find_sum(list, [], target, [])
    # Ordenamos
    sorted_sums = [sorted(s) for s in sums]
    # Eliminamos diplicados
    set_sums = set(tuple(s) for s in sorted_sums)
    # Volvemos a lista de listas
    return [[t for t in tuple] for tuple in set_sums]

def _find_sum(list: [], source: [], target: int, sums: []):
    for i in range(len(list)):
        if sum(source) + list[i] == target:
          sums.append(source + [list[i]])
        else:
          _find_sum(list[:i] + list[i+1::], source + [list[i]], target, sums)
    
    return sums
                

print('[1, 5, 3, 2] - Possible sums: ', find_sum([1, 5, 3, 2], 6))
print('[8, 3, 7, 1] - Possible sums: ', find_sum([8, 3, 7, 1], 2))
print('[1, 2, 3, 4, 5, 6, 7, 8, 9] - Possible sums: ', find_sum([1, 2, 3, 4, 5, 6, 7, 8, 9], 12))