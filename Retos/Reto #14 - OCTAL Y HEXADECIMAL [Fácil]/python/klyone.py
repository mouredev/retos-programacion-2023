#!/usr/bin/env python3

hex_table = {
    "conversion" :
    {
        0 : "0",
        1 : "1",
        2 : "2",
        3 : "3",
        4 : "4",
        5 : "5",
        6 : "6",
        7 : "7",
        8 : "8",
        9 : "9",
        10 : "A",
        11 : "B",
        12 : "C",
        13 : "D",
        14 : "E",
        15 : "F",
    },
    "base" : 16,
    "prefix" : "0x",
}

octal_table = {
    "conversion" :
    {
        0 : "0",
        1 : "1",
        2 : "2",
        3 : "3",
        4 : "4",
        5 : "5",
        6 : "6",
        7 : "7",
    },
    "base" : 8,
    "prefix" : "0o",
}

def get_max_exponent(number, base):
    acc = 1
    exp = 0

    while acc <= number:
        exp = exp + 1
        acc = base ** exp

    if exp > 0:
        exp = exp - 1

    return exp

def convert_integer(number, conversion_table=hex_table):

    output = ""

    if number < 0:
        output = output + "-"
        number = -number

    output = output + conversion_table["prefix"]
    base = conversion_table["base"]

    exp = get_max_exponent(number, base)

    for e in range(exp, -1, -1):
        acc = base ** e
        mod = number % acc
        div = int(number / acc)
        output = output + conversion_table["conversion"][div]
        number = mod

    return output

def convert_integer_to_hex(number):
    return convert_integer(number, hex_table)

def convert_integer_to_oct(number):
    return convert_integer(number, octal_table)

print(convert_integer_to_hex(16))
print(convert_integer_to_hex(-32))
print(convert_integer_to_hex(-34))
print(convert_integer_to_hex(1234))
print(convert_integer_to_hex(344))
print(convert_integer_to_hex(123456789))
print(convert_integer_to_oct(16))
print(convert_integer_to_oct(-32))
print(convert_integer_to_oct(-34))
print(convert_integer_to_oct(1234))
print(convert_integer_to_oct(344))
print(convert_integer_to_oct(123456789))
