# /*
#  * Crea una función que reciba un número decimal y lo trasforme a Octal
#  * y Hexadecimal.
#  * - No está permitido usar funciones propias del lenguaje de programación que
#  * realicen esas operaciones directamente.
#  */

def decimal_to_octal(decimal):
    octal = ""
    while decimal > 0:
        octal = str(decimal % 8) + octal
        decimal = decimal // 8
    return octal

def decimal_to_hexadecimal(decimal):
    hexadecimal = ""
    while decimal > 0:
        resto = decimal % 16
        if resto < 10:
            hexadecimal = str(resto) + hexadecimal
        else:
            hexadecimal = chr(55 + resto) + hexadecimal
        decimal = decimal // 16
    return hexadecimal

def decimal_to_octal_and_hexadecimal(decimal):
    octal = decimal_to_octal(decimal)
    hexadecimal = decimal_to_hexadecimal(decimal)
    return octal, hexadecimal

print(decimal_to_octal_and_hexadecimal(10)) 
print(decimal_to_octal_and_hexadecimal(16)) 
print(decimal_to_octal_and_hexadecimal(23)) 