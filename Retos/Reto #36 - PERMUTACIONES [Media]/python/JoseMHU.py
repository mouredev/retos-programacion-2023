import itertools


def word_permutation(word: str) -> None:
    letters = [letter for letter in word]
    permutation_list = list(itertools.permutations(letters))
    for permutation in permutation_list:
        print("".join(permutation), end=", ")


if __name__ == "__main__":
    word_permutation("sol")
