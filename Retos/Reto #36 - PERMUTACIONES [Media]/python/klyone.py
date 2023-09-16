#!/usr/bin/env python3

def generate_permutations(symbols, permutation, permutations_list, size):
    for i in range(len(symbols)):
        current_symbols = symbols.copy()
        current_symbols.pop(i)
        s = symbols[i]
        permutation.append(s)
        if len(permutation) == size:
            p = "".join(permutation)

            if not p in permutations_list:
                permutations_list.append(p)

            permutation.pop(-1)
            return
        generate_permutations(current_symbols, permutation, permutations_list, size)
        permutation.pop(-1)

def calculate_permutations(text):
    permutations = []
    generate_permutations(list(text), [], permutations, len(text))
    print(permutations)
    print(len(permutations))

if __name__ == "__main__":
    calculate_permutations("sol")
    calculate_permutations("abczd")
