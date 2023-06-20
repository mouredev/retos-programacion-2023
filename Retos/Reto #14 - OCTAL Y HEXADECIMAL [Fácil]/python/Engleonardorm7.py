# /*
#  * Crea una función que reciba un número decimal y lo trasforme a Octal
#  * y Hexadecimal.
#  * - No está permitido usar funciones propias del lenguaje de programación que
#  * realicen esas operaciones directamente.
#  */

def decimal_to_octal_hexadecimal(decimal_num):
    octal_num = ""
    while decimal_num > 0:
        remainder = decimal_num % 8
        octal_num = str(remainder) + octal_num
        decimal_num //= 8
    return octal_num


def decimal_to_hexadecimal(decimal_num):
    hexadecimal_num = ""
    hexadecimal_chars = "0123456789ABCDEF"
    while decimal_num > 0:
        remainder = decimal_num % 16
        hexadecimal_num = hexadecimal_chars[remainder] + hexadecimal_num
        decimal_num //= 16

    return hexadecimal_num


decimal=int(input("Type a number"))
print(decimal_to_octal_hexadecimal(decimal), decimal_to_hexadecimal(decimal))
