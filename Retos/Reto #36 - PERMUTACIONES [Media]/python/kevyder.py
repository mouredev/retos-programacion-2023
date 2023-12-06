def permutate(chars: list[str]) -> list[list[str]]:
    string_len = len(chars)
    result = []
    i = 0

    if string_len == 1:
        return [chars.copy()]

    while i < string_len:
        char = chars.pop(0)  # use backtracking
        permutations = permutate(chars)  # use recursion

        for permutation in permutations:
            permutation.append(char)

        result.extend(permutations)
        chars.append(char)
        i += 1

    return result


if __name__ == "__main__":
    word = "sol"
    chars = list(word)
    permutations = permutate(chars)
    result = ["".join(permutation) for permutation in reversed(permutations)]
    print(result)
