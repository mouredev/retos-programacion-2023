"""
* Crea una función que reciba un número decimal y lo trasforme a Octal
 * y Hexadecimal.
 * - No está permitido usar funciones propias del lenguaje de programación que
 * realicen esas operaciones directamente. 
"""

def to_hexadecimal(number: int):
    list_response = []
    response = ''
    while number > 0:
        list_response.append(number % 16)
        number = number // 16
    for i in list_response:
        response += str(i)
    return int(response[::-1])

def to_octal(number: int):
    list_response = []
    response = ''
    while number > 0:
        list_response.append(number % 8)
        number = number // 8
    for i in list_response:
        response += str(i)
    return int(response[::-1])

def to_hexadecimal_and_to_octal(number: int):
    return f'Hexadecimal: {to_hexadecimal(number)}, Octal: {to_octal(number)}'


print(to_hexadecimal_and_to_octal(500))