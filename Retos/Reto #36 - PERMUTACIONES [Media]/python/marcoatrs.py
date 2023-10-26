import itertools
from typing import List


def permutaciones(word: str) -> List[str]:
    words = list()
    if len(word) <= 1:
        return [word]
    for i, letter in enumerate(word):
        for per in permutaciones(f"{word[:i]}{word[i+1:]}"):
            words.append(f"{letter}{per}")
    return words


word = "sol"

# Opcion 1
print(permutaciones("sol"))

# Opcion 2
print(["".join(per) for per in itertools.permutations(word)])
