# Reto #14: Octal y Hexadecimal
#### Dificultad: Fácil | Publicación: 03/04/23 | Corrección: 10/04/23

## Enunciado



"""
 * Crea una función que reciba un número decimal y lo trasforme a Octal
 * y Hexadecimal.
 * - No está permitido usar funciones propias del lenguaje de programación que
 * realicen esas operaciones directamente.

"""
 


def main(numero: int):
    print(decimal_a_octal(numero))
    print(decimal_a_hexadecimal(numero))


def decimal_a_octal(numero):
    
    octal = ""
    while numero > 0:
        residuo = numero % 8
        octal = str(residuo) + octal
        numero //= 8
    return f'EL numero octal es: {octal} '


def decimal_a_hexadecimal(numero: int):
    hexadecimal = ""
    while numero > 0:
        residuo = numero % 16
        if residuo < 10:
            hexadecimal = str(residuo) + hexadecimal
        else:
            hexadecimal = chr(residuo + 55) + hexadecimal
        numero //= 16
    return f'EL numero octal es: {hexadecimal} '

    

if __name__ == 'main': 
    main(255)
