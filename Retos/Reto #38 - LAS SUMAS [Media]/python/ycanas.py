def findsums(numbers, target):
    def findsum(start, target, combination):
        if target == 0:
            result.append(combination.copy())
            return
        
        if target < 0 or start == len(numbers):
            return
        
        for i in range(start, len(numbers)):
            if i > start and numbers[i] == numbers[i - 1]:
                continue

            combination.append(numbers[i])
            findsum(i + 1, target - numbers[i], combination)
            combination.pop()
    
    numbers.sort()
    result = []
    findsum(0, target, [])
    
    return result


print(findsums([1, 1, 1, 1, 1, 1, 1, 2, 2], 7))
