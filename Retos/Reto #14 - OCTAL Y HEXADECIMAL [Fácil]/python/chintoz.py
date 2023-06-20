def to_base(number, base, to_simple_digit):
    if number < base:
        return to_hexa_simple_digit(number)
    remainder = number % base
    divided = int(number / base)
    return to_base(divided, base, to_simple_digit) + to_simple_digit(remainder)


def to_hexa_simple_digit(number):
    if number < 10:
        return str(number)
    simple_hexa_map = {
        10: "a",
        11: "b",
        12: "c",
        13: "d",
        14: "e",
        15: "f"
    }
    return simple_hexa_map[number]


def to_oct_simple_digit(number):
    return str(number)


if __name__ == '__main__':
    inputNumber = int(input("Introduce el número en decimal para convertir: "))
    to_hexa = to_base(inputNumber, 16, to_hexa_simple_digit)
    to_octal = to_base(inputNumber, 8, to_oct_simple_digit)
    print("Hexadecimal: " + to_hexa)
    print("Octal: " + to_octal)
    print("Con correctos?? hexa: " + str("0x" + to_hexa == str(hex(inputNumber)))
          + " octal: " + str("0o" + to_octal == str(oct(inputNumber))))
