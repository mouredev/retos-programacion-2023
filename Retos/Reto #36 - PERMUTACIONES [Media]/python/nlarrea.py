"""
 * Crea un programa que sea capaz de generar e imprimir todas las 
 * permutaciones disponibles formadas por las letras de una palabra.
 * - Las palabras generadas no tienen por qué existir.
 * - Deben usarse todas las letras en cada permutación.
 * - Ejemplo: sol, slo, ols, osl, los, lso 
"""

from functools import reduce
from random import sample


def get_permutation_quantity(word: str) -> int:
    # Formula to get the number of permutations:
    #   factorial(n) / multiplication of the factorial of how many times is repeated each char

    def factorial(number: int) -> int:
        if number == 1: return 1
        return number * factorial(number-1)
    
    # Get how many times is repeated each char (without repetition)
    chars_qty = set((char, word.count(char)) for char in word)

    n = len(word)
    fact_of_chars_qty = reduce(
        lambda total, current: total * factorial(current[1]),
        chars_qty,
        1
    )

    return factorial(n) // fact_of_chars_qty


def word_permutations(word: str) -> None:
    # Get the quantity of permutations
    permutations_qty = get_permutation_quantity(word)

    # Generate the permutations
    permutations = {word}
    while len(permutations) < permutations_qty:
        for _ in range(len(word)):
            new_word = sample(list(word), len(word))

        permutations.add("".join(new_word))


    # Print the results
    print(f"\nPermutaciones de '{word}':")
    for index, permutation in enumerate(permutations):
        print(f"{index + 1}. {permutation}")


if __name__ == "__main__":
    word_permutations("sol")