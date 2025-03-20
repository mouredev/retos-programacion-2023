from itertools import permutations

def permutacion(word: str) -> list:
    return list(permutations(word))

for i, word in enumerate(permutacion('sol'),start= 1):
    print(f'{i}° {''.join(word)}')