def decimal_to_hex(decimal):
    hexadecimales = [
        "0",
        "1",
        "2",
        "3",
        "4",
        "5",
        "6",
        "7",
        "8",
        "9",
        "A",
        "B",
        "C",
        "D",
        "E",
        "F",
    ]

    hexadecimal = ""
    while decimal > 0:
        resto = decimal % 16
        hexadecimal = hexadecimales[resto] + hexadecimal
        decimal = decimal // 16
    return hexadecimal


def decimal_to_oct(decimal):
    octales = [
        "0",
        "1",
        "2",
        "3",
        "4",
        "5",
        "6",
        "7",
    ]

    octal = ""
    while decimal > 0:
        resto = decimal % 8
        octal = octales[resto] + octal
        decimal = decimal // 8
    return octal


if __name__ == "__main__":
    decimal = int(input("Por favor ingrese un entero: "))
    print(decimal_to_hex(decimal))
    print(decimal_to_oct(decimal))
