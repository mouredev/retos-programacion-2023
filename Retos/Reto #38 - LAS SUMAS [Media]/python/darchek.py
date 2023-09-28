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
from typing import Tuple
import numpy as np


def sum(num_list: Tuple[int], target: int):
    num_result = []
    for i, number1 in enumerate(num_list):
        target_matrix = [[number1]]
        for j in range(i + 1, len(num_list)):
            target_len = len(target_matrix)
            for target_cnt in range(target_len):
                total_sum = np.sum(np.array(target_matrix[target_cnt]))
                target_sum = int(total_sum + num_list[j])
                if target_sum < target:
                    new_element = target_matrix[target_cnt] + [num_list[j]]
                    target_matrix.append(new_element)
                elif target_sum == target:
                    new_element = target_matrix[target_cnt] + [num_list[j]]
                    num_result.append(new_element)
    return num_result


n_list = [1, 9, 2, 3, 4, 5, 6]
num_target = 10

result = sum(n_list, num_target)
print(result)
