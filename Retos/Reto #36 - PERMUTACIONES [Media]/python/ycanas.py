def permute(word):
    if len(word) == 1:
        return word
    
    permutations = []

    for i in range(len(word)):
        current = word[i]
        rest = word[:i] + word[i + 1:]

        _permutations = permute(rest)

        for permut in _permutations:
            permutations.append(current + permut)

    return permutations


permutations = permute("sol")

for permut in permutations:
    print(permut)
