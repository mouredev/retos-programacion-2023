#!/usr/bin/env python3

N_ABC = 26

def get_code_length(code):
    return len(code)

def convert_to_int(elem):
    return (ord(elem) - ord("A")) + 1

def calculate_row_index(code):
    length = get_code_length(code)
    code = list(map(convert_to_int, list(code)))

    if length > 1:
        code[0] = code[0] * N_ABC

    row_index = sum(code)

    return row_index

if __name__ == "__main__":
    print(calculate_row_index("A"))
    print(calculate_row_index("AA"))
    print(calculate_row_index("CA"))
    print(calculate_row_index("ZA"))
    print(calculate_row_index("ZZ"))
    print(calculate_row_index("ZZB"))
