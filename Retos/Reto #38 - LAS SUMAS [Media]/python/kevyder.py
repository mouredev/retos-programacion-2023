def combine(elements: list, length: int) -> list[list]:
    """
    Generate all combinations of a given length from a list of elements.

    Args:
        elements (list): A list of elements to generate combinations from.
        length (int): The desired length of the combinations to generate.

    Returns:
        list[list]: A list of lists containing all valid combinations of the specified length.
    """
    combinations = []

    def backtrack(current_index: int, combination: list) -> None:
        """
        Recursively build valid combinations.

        Args:
            current_index (int): The current index being considered in the 'elements' list.
            combination (list): The current combination being built.

        Returns:
            None
        """
        if len(combination) == length:
            combinations.append(combination.copy())
            return

        for index in range(current_index, len(elements)):
            combination.append(elements[index])
            backtrack(index + 1, combination)
            combination.pop()

    backtrack(0, list())
    return combinations


def sum_combinations(numbers: list[int], objetive: int) -> list[list[int]]:
    results = []
    numbers_len = len(numbers) + 1
    for length in range(2, numbers_len):
        numbers_combinations = combine(numbers, length)
        sum_results = filter(lambda x: (sum(x) == objetive), numbers_combinations)
        results.extend(list(sum_results))

    return results


if __name__ == "__main__":
    case_one_numbers = [1, 5, 3, 2]
    case_one_objetive = 6
    case_one_results = sum_combinations(
        numbers=case_one_numbers, objetive=case_one_objetive
    )
    print(case_one_results)

    case_two_numbers = [1, 3, 2, 4]
    case_two_objetive = 5
    case_two_results = sum_combinations(
        numbers=case_two_numbers, objetive=case_two_objetive
    )
    print(case_two_results)

    case_three_numbers = [100, 200, 300, 400]
    case_three_objetive = 700
    case_three_results = sum_combinations(
        numbers=case_three_numbers, objetive=case_three_objetive
    )
    print(case_three_results)
