# Reto #38: Las sumas
#### Dificultad: Media | Publicación: 25/09/23 | Corrección: 02/10/23

## Enunciado


#
# Crea una función que encuentre todas las combinaciones de los números
# de una lista que suman el valor objetivo.
# - La función recibirá una lista de números enteros positivos
#   y un valor objetivo.
# - Para obtener las combinaciones sólo se puede usar
#   una vez cada elemento de la lista (pero pueden existir
#   elementos repetidos en ella).
# - Ejemplo: Lista = [1, 5, 3, 2],  Objetivo = 6
#   Soluciones: [1, 5] y [1, 3, 2] (ambas combinaciones suman 6)
#   (Si no existen combinaciones, retornar una lista vacía)
#

class CombinationsFinder:
    def __init__(self, input_list, target_sum):
        self.input_list = input_list
        self.target_sum = target_sum
        self.result = []
        self.input_list.sort()

    def find_combinations(self):

        def backtrack(remain, comb, start):
            if remain == 0:
                self.result.append(list(comb))
                return
            elif remain < 0:
                return
            for i in range(start, len(self.input_list)):
                comb.append(self.input_list[i])
                backtrack(remain - self.input_list[i], comb, i + 1)
                comb.pop()

        self.result = []
        backtrack(self.target_sum, [], 0)
        return self.result

if __name__ == "__main__":
    input_list = [1, 5, 3, 2, 6, 4]
    target_sum = 8

    finder = CombinationsFinder(input_list, target_sum)
    solutions = finder.find_combinations()
    print(solutions)


