#!/usr/bin/env python3

def calculate_string_diff(str1, str2):
    if len(str1) != len(str2):
        return []

    diff = []
    for index in range(len(str1)):
        if str1[index] != str2[index]:
            diff.append(str2[index])

    return diff

if __name__ == "__main__":
    print(calculate_string_diff("hola", "heqa"))
    print(calculate_string_diff("Me llamo mouredev", "Me llemo mouredov"))
    print(calculate_string_diff("Me llamo.Brais Moure", "Me llamo brais moure"))
