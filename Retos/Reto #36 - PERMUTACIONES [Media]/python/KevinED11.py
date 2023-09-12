"""
This module contains the implementation of the `permutations`
function using different integrated libraries.
"""
import itertools
from typing import TypeAlias, Iterable
import numpy as np
import functools


StrList: TypeAlias = list[str]
PermutationList: TypeAlias = StrList
CharacterList: TypeAlias = StrList


@functools.lru_cache()
def generate_list_of_characters(word: str) -> CharacterList:
    """
    Generate a list of characters from a given word.
    """
    return list(word)


def join_characters(text: Iterable) -> str:
    """
    Join a list of characters into a single string.
    """
    return "".join(text)


@functools.lru_cache()
def permutations(word: str) -> PermutationList:
    """
    Generate a list of all possible permutations of a given
    word using the itertools library.
    """
    word_list = generate_list_of_characters(word=word)
    permutations_list = [
        join_characters(text=word) for word in itertools.permutations(word_list)
    ]
    return permutations_list


def random_permutation(word: str) -> str:
    """
    Generate  a random  permutation of a given word using
    the numpy library.
    """
    word_list = generate_list_of_characters(word=word)
    rand_permutation = np.random.permutation(word_list)

    return join_characters(text=rand_permutation)


def main() -> None:
    """
    Entry point of the application
    """
    print(permutations(word="sol"))
    print(random_permutation(word="sol"))


if __name__ == "__main__":
    main()
