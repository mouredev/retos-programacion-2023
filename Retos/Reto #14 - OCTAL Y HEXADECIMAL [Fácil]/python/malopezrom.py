# /*
# * Crea una función que reciba un número decimal y lo trasforme a Octal
# * y Hexadecimal.
# * - No está permitido usar funciones propias del lenguaje de programación que
# * realicen esas operaciones directamente.
# */

# Funcion que convierte un numero a octal
def to_octal(number):
    octal = 0
    decimal = int(number)
    i = 1
    while decimal != 0:
        octal += (decimal % 8) * i
        decimal //= 8
        i *= 10
    return octal

# Funcion que convierte un numero a hexadecimal
def to_hexadecimal(number):
    hexadecimal = ""
    decimal = int(number)
    while decimal != 0:
        value = decimal % 16
        if value < 10:
            hexadecimal = str(value) + hexadecimal
        else:
            hexadecimal = chr(value + 55) + hexadecimal
        decimal //= 16
    return hexadecimal


def main():
    number = 255255255
    print("Octal: " + str(to_octal(number)))
    print("Hexadecimal: " + str(to_hexadecimal(number)))


main()