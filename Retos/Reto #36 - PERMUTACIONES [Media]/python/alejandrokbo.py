# /*
# * Crea un programa que sea capaz de generar e imprimir todas las
# * permutaciones disponibles formadas por las letras de una palabra.
# * - Las palabras generadas no tienen por qué existir.
# * - Deben usarse todas las letras en cada permutación.
# * - Ejemplo: sol, slo, ols, osl, los, lso
# */
import itertools

if __name__ == '__main__':
    word = input("Enter a word: ")
    permuted = list(itertools.permutations(word))
    result: set = set()
    for item in permuted:
        result.add("".join(item))
    result_list = list(result)
    print("The permutations of the word", word, "are:", len(result_list))
    for i in range(len(result)):
        print(i + 1, "->\t", result_list.pop())
