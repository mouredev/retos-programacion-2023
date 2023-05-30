"""
 * Crea una función que reciba un número decimal y lo trasforme a Octal
 * y Hexadecimal.
 * - No está permitido usar funciones propias del lenguaje de programación que
 * realicen esas operaciones directamente.
"""

def SystemChange(number):
    octal = OctalSystem(number)
    hexadecimal = HexadecimalSystem(number)

    return f"Sistema Octal: {octal} - Sistema Hexadecimal: {hexadecimal}"

def OctalSystem(number):
    arr = []
    a = number
    b = 8

    while a > b:
        arr.insert(0, a % b)
        a = a // b
    arr.insert(0, a)
    return ''.join(map(str, arr))

def HexadecimalSystem(number):
    obj = {10: 'A', 11: 'B', 12: 'C', 13: 'D', 14: 'E', 15: 'F'}
    arr = []
    a = number
    b = 16

    while a > b:
        if a % b >= 10:
            arr.insert(0, obj[a % b])
        else:
            arr.insert(0, a % b)
        a = a // b

    if a >= 10:
        arr.insert(0, obj[a % b])
    else:
        arr.insert(0, a)
    return ''.join(map(str, arr))

print(SystemChange(10))
print(SystemChange(20))
print(SystemChange(30))
