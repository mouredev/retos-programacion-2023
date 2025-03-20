from itertools import combinations

def comb(list_numbers:list, target: int)-> list:
    return [com for i in range(2,len(list_numbers))
            for com in combinations(list_numbers, i) if sum(com) == target]
print(comb([1, 5, 3, 2], 6))