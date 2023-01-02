"""
    Reto 0
    Escribe un programa que muestre por consola (con un print) los
    números de 1 a 100 (ambos incluidos y con un salto de línea entre
    cada impresión), sustituyendo los siguientes:
        - Múltiplos de 3 por la palabra "fizz".
        - Múltiplos de 5 por la palabra "buzz".
        - Múltiplos de 3 y de 5 a la vez por la palabra "fizzbuzz".
"""

isMultiple = lambda number, multiple: number % multiple == 0

for number in range(1, 101):
    if isMultiple(number, 3) and isMultiple(number, 5):
        print('fizzbuzz')
    elif isMultiple(number, 3):
        print('fizz')
    elif isMultiple(number, 5):
        print('buzz')
    else:
        print(number)