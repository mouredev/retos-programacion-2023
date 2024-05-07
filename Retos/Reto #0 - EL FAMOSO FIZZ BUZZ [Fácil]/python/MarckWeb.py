""" 
/*
 * Escribe un programa que muestre por consola (con un print) los
 * números de 1 a 100 (ambos incluidos y con un salto de línea entre
 * cada impresión), sustituyendo los siguientes:
 * - Múltiplos de 3 por la palabra "fizz".
 * - Múltiplos de 5 por la palabra "buzz".
 * - Múltiplos de 3 y de 5 a la vez por la palabra "fizzbuzz".
*/ 
"""

# Ejercicio con condicion ternario


def fizzBuzz():
    for i in range(101):
        result = 'Fizz' * (i % 3 == 0) + 'Buzz' * (i % 5 == 0)
        print(result if result else i)


fizzBuzz()

# Ejercicio con condicion if, elif


def fizzBuzz():
    for i in range(101):
        output = ''
        divisibleForTHree = i % 3 == 0
        divisibleForFive = i % 5 == 0
        if divisibleForTHree and divisibleForFive:
            output = 'FizzBuzz'
        elif divisibleForTHree:
            output = 'Fizz'
        elif divisibleForFive:
            output = 'Buzz'
        else:
            output = i
        print(output)


fizzBuzz()
