def permutations(word: str) -> list:
    """
    Generate and return all permutations of the given word.

    Parameters:
    - word (str): The input word.

    Returns:
    - list: A list containing all permutations.
    """
    if len(word) <= 1:
        return [word]

    result = []

    for index in range(len(word)):
        current_letter = word[index]
        rest_word = word[:index] + word[index + 1:]

        for permutation in permutations(rest_word):
            result.append(current_letter + permutation)

    return result

# Example usage
word_to_permute = "sol"
permutations_result = permutations(word_to_permute)

# Displaying the permutations
for index, permutation in enumerate(permutations_result):
    print(f"{index + 1}. {permutation}")
