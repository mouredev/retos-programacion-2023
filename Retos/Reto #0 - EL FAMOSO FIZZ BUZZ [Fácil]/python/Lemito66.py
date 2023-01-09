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
def fizz_buzz(limit):
    list_of_numbers_and_strings = []
    for item in range(1, limit +1):
        if item % 3 == 0 and item %5 == 0:
            list_of_numbers_and_strings.append('fizzbuzz')
        elif item % 3 == 0:
            list_of_numbers_and_strings.append('fizz')
        elif item % 5 == 0:
            list_of_numbers_and_strings.append('buzz')
        else:
            list_of_numbers_and_strings.append(item)
    return list_of_numbers_and_strings

for i in fizz_buzz(100):
    print(i)
    