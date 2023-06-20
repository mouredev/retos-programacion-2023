# Reto #14: Octal y Hexadecimal
#### Dificultad: Fácil | Publicación: 03/04/23 | Corrección: 10/04/23

## Enunciado

#
# Crea una función que reciba un número decimal y lo trasforme a Octal
# y Hexadecimal.
# - No está permitido usar funciones propias del lenguaje de programación que
# realicen esas operaciones directamente.
#


class OctalHexadecimal:
    def __init__(self, decimal_number):
        self.decimal_number = decimal_number

    def decimal_to_octal(self):
        cocient = self.decimal_number
        octal = ""

        while cocient > 0:
            rest = cocient % 8
            cocient = cocient // 8
            octal = str(rest) + octal

        return octal

    def decimal_to_hexadecimal(self):
        cocient = self.decimal_number
        hexadecimal = ""
        hex_digits = "0123456789ABCDEF"

        while cocient > 0:
            rest = cocient % 16
            cocient = cocient // 16
            hexadecimal = hex_digits[rest] + hexadecimal

        return hexadecimal

    def print_results(self):
        octal_number = self.decimal_to_octal()
        hexadecimal_number = self.decimal_to_hexadecimal()
        print(f"Decimal: {self.decimal_number}")
        print(f"Octal: {octal_number}")
        print(f"Hexadecimal: {hexadecimal_number}")


if __name__ == "__main__":
    decimal_number = 17
    convert = OctalHexadecimal(decimal_number)
    convert.print_results()
