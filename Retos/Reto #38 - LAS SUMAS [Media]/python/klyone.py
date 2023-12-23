#!/usr/bin/env python3

solutions = []

def _comb_sum(comb):
    s = 0
    for c in comb:
        s += c
    return s

def _sum(array, target, comb):
    if array == []:
        return

    for a in array:
        array2 = array.copy()
        array2.remove(a)
        comb.append(a)
        s = _comb_sum(comb)

        if s == target:
            sol = sorted(comb)
            if not sol in solutions:
                solutions.append(sol)
            comb.remove(a)
            continue
        if s > target:
            comb.remove(a)
            continue

        _sum(array2, target, comb)
        comb.remove(a)

def sum(array, target):
    global solutions
    solutions = []
    comb = []
    print(array)
    _sum(array, target, comb)
    print(solutions)

if __name__ == "__main__":
    sum([], 6)
    sum([4],6)
    sum([6],6)
    sum([5,6,1,3,4,3],6)
    sum([1, 5, 3, 2],6)
