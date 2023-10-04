def combinations(nums, target):
    res = solution(nums, target)
    if len(res) == 0:
        return [[]]
    return res


# O(2^n)
def solution(nums, target, actual=[], indice=0):
    if target == 0:
        return [actual]
    if target < 0 or indice == len(nums):
        return []

    one = solution(nums, target - nums[indice], actual + [nums[indice]], indice + 1)
    two = solution(nums, target, actual, indice + 1)

    return one + two


def main():
    print(*combinations([1, 5, 3, 2], 6))
    print(*combinations([2, 4, 6, 8, 10, 12, 14, 16], 15))
    print(*combinations([1, 2, 3, 4, 5, 6, 7, 8, 9, 10], 10))
    print(*combinations([2, 3, 2, 5, 4, 2, 6], 8))


if __name__ == "__main__":
    main()
