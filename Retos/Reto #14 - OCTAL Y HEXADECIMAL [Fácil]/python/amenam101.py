"""
/*
 * Crea una función que reciba un número decimal y lo trasforme a Octal
 * y Hexadecimal.
 * - No está permitido usar funciones propias del lenguaje de programación que
 * realicen esas operaciones directamente.
 */
"""
def to_octal_and_hex(decimal: int):
    current_decimal = decimal

    #Octal
    octal=""
    while current_decimal > 0:
        octal = str(current_decimal % 8) + octal
        current_decimal //=8
    
    octal = 0 if octal == "" else octal
    print(f'{decimal} en octal es 0o{octal}')

    current_decimal = decimal

    #Hexadecimal
    current_decimal = decimal
    hexa=""
    hex_num = "0123456789ABCDEF"
    while current_decimal > 0:
        hexa = hex_num[current_decimal % 16] + hexa
        current_decimal //=16
    
    hexa = 0 if hexa == "" else hexa
    print(f'{decimal} en hexadecimal es 0x{hexa}')    


if __name__=='__main__':
    decimal = int(input("Ingresa un número: "))
    to_octal_and_hex(decimal)