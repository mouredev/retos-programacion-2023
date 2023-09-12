import itertools


# It is used to check if the permutations of the permutations2 function are correct
def permutations(string):
    return list(itertools.permutations(string))


def permutations2(string):

    if len(string) == 0:
        return ['']

    first = string[0]
    rest = string[1:]

    words = permutations2(rest)
    new_words = []

    for word in words:
        for i in range(len(word) + 1):
            new_words.append(word[:i] + first + word[i:])

    return new_words


# Convert the permutations of the permutations functions to strings
def to_strings(permutations: list):
    permutation_list = []

    for permutation in permutations:

        word = ''.join(letter for letter in permutation)
        permutation_list.append(word)

    return permutation_list


# To compare the permutations of the permutations functions
def check_permutations(permutations1, permutations2):

    for permutation in permutations1:
        if permutation not in permutations2:
            return False

    return True


def main():
    permutations = to_strings(permutations2('sol'))

    for permutation in permutations:
        print(permutation)


if __name__ == '__main__':
    main()
