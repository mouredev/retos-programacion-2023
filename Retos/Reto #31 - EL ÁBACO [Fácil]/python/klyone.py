#!/usr/bin/env python3

MAX_EXP = 6

def calculate_number(pos, num):
    return 10**(MAX_EXP - pos) * num

def read_abacus_line(line):
    num = 0

    for l in line:
        if l == "-":
            break
        num = num + 1

    print(num)
    return num

def read_abacus(abacus):
    line = 0
    num = 0

    for a in abacus:
        n = read_abacus_line(a)
        num = num + calculate_number(line, n)
        line = line + 1
    return num

if __name__ == "__main__":
    abacus = [
    "O---OOOOOOOO",
    "OOO---OOOOOO",
    "---OOOOOOOOO",
    "OO---OOOOOOO",
    "OOOOOOO---OO",
    "OOOOOOOOO---",
    "---OOOOOOOOO"
    ]

    print(read_abacus(abacus))
