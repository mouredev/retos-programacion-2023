def find_nums(numbers: list, target: int) -> list:

    def find_combinations(start: int, current_combination: list):
        if sum(current_combination) == target:
            result.append(current_combination[:])
            return

        if sum(current_combination) > target or start == len(numbers):
            return

        for i in range(start, len(numbers)):
            if i > start and numbers[i] == numbers[i - 1]:
                continue

            current_combination.append(numbers[i])
            find_combinations(i + 1, current_combination)
            current_combination.pop()

    numbers.sort()
    result = []
    find_combinations(0, [])
    return result



print(find_nums([1, 5, 3, 2], 6))
print(find_nums([1, 2, 1, 1, 1, 1, 2, 1,0,10], 16))