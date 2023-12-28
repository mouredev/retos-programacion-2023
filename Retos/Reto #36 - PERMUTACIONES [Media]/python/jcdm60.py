# Reto #36: Permutaciones
#### Dificultad: Media | Publicación: 04/09/23 | Corrección: 18/09/23

## Enunciado

#
# Crea un programa que sea capaz de generar e imprimir todas las
# permutaciones disponibles formadas por las letras de una palabra.
# - Las palabras generadas no tienen por qué existir.
# - Deben usarse todas las letras en cada permutación.
# - Ejemplo: sol, slo, ols, osl, los, lso
#


class WordPermuter:
    def __init__(self, word):
        self.word = word
        self.permutations = []

    def generate_permutations(self):
        word_list = list(self.word)
        word_list.sort()  # Ordeno la palabra para asegurar permutaciones únicas
        while True:
            permutation = "".join(word_list)
            self.permutations.append(permutation)
            word_list = self._generate_next_permutation(word_list)
            if word_list is None:
                break

    def _generate_next_permutation(self, word_list):
        n = len(word_list)
        i = n - 2
        while i >= 0 and word_list[i] >= word_list[i + 1]:
            i -= 1
        if i == -1:
            return None  # Ya se hicieron todas las permutaciones
        j = n - 1
        while word_list[j] <= word_list[i]:
            j -= 1
        word_list[i], word_list[j] = word_list[j], word_list[i]
        word_list[i + 1 :] = reversed(word_list[i + 1 :])  
        return word_list


    def print_permutations(self):
        self.generate_permutations()
        permutations = self.permutations
        total_permutations = len(permutations)
        print("Permutations:")
        for i, permutation in enumerate(permutations):
            print(f"{i + 1}: {permutation}")
        print(f"Total de permutaciones: {total_permutations}")
        print(f"Palabra ingresada: {word}")


if __name__ == "__main__":
    word = input("Ingrese la palabra: ")
    permuter = WordPermuter(word)
    permuter.print_permutations()
