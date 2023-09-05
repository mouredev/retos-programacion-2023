"""
This module contains the implementation of the `permutations`
function using different integrated libraries.
"""
import itertools
from typing import TypeAlias
import numpy as np


PermutationList: TypeAlias = list[str]


def permutations(word: str) -> PermutationList:
    """
    Generate a list of all possible permutations of a given
    word using the itertools library.
    """
    word_list = list(word)
    permutations_list = ["".join(word)
                         for word in itertools.permutations(word_list)]
    return permutations_list


def random_permutation(word: str) -> str:
    """
    Generate  a random  permutation of a given word using
    the numpy library.
    """
    word_array = np.array(list(word))
    rand_permutation = np.random.permutation(word_array)

    return "".join(rand_permutation)


def main() -> None:
    """
    Entry point of the application
    """
    print(permutations(word="sol"))
    print(random_permutation(word="sol"))


if __name__ == "__main__":
    main()
