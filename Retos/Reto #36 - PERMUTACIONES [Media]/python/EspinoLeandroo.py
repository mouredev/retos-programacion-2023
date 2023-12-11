def generate_permutations(word):
    def generate_permutations_helper(word, index, permutations):
        if index == len(word) - 1:
            permutations.append(''.join(word))
        else:
            for i in range(index, len(word)):
                word[index], word[i] = word[i], word[index]
                generate_permutations_helper(word, index + 1, permutations)
                word[index], word[i] = word[i], word[index]  # Deshacer el intercambio para volver al estado original

    permutations = []
    generate_permutations_helper(list(word), 0, permutations)
    return permutations

if __name__ == "__main__":
    word = "Leandro"
    permutations = generate_permutations(word)
    for permutation in permutations:
        print(permutation)
