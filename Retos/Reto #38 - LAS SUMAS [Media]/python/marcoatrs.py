from itertools import combinations
from typing import List


def get_sums(list_numbers: List[int], target: int):
    results = list()
    for size in range(1, len(list_numbers) + 1):
        for com in combinations(list_numbers, size):
            if sum(com) != target:
                continue
            results.append(list(com))
    return results

print(get_sums([1, 5, 3, 2], 6))
