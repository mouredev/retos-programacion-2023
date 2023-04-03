"""
* Crea una función que reciba un número decimal y lo trasforme a Octal
 * y Hexadecimal.
 * - No está permitido usar funciones propias del lenguaje de programación que
 * realicen esas operaciones directamente. 
"""

def to_hexadecimal(number: int):
    response = []
    number_hexadecimal = []
    while number > 0:
        response.append(number % 16)
        number = number // 16
    return number_hexadecimal
    #return response[::-1]
print(to_hexadecimal(500))