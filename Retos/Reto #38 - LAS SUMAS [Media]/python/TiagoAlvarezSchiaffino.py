def find_sums(numbers: list, target: int) -> list:
    """
    Find all combinations of numbers that sum up to the target value.

    Parameters:
    - numbers (list): A list of positive integers.
    - target (int): The target sum.

    Returns:
    - list: A list of combinations.
    """
    def backtracking(start: int, target: int, current_combination: list) -> None:
        """
        Recursive backtracking function to find combinations.

        Parameters:
        - start (int): The starting index for the current recursive call.
        - target (int): The remaining target sum.
        - current_combination (list): The current combination being formed.

        Returns:
        - None
        """
        if target == 0:
            combinations.append(current_combination[:])
            return
            
        for i in range(start, len(numbers)):
            if i > start and numbers[i] == numbers[i - 1]:
                continue
            if numbers[i] > target:
                break
            
            current_combination.append(numbers[i])
            backtracking(i + 1, target - numbers[i], current_combination)
            current_combination.pop()
                        
    numbers.sort()
    combinations = []
    backtracking(0, target, [])
    return combinations

def main():
    numbers = [1, 1, 2, 1, 1, 1, 2]
    target = 6
    combinations = find_sums(numbers, target)

    if combinations:
        print(f"Combinations that sum up to {target}:")
        for combo in combinations:
            print(combo)
    else:
        print("No combinations found that sum up to the target.")

if __name__ == "__main__":
    main()
