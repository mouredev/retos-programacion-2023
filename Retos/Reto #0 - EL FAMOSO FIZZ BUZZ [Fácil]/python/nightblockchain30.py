'''/*
 * Escribe un programa que muestre por consola (con un print) los
 * números de 1 a 100 (ambos incluidos y con un salto de línea entre
 * cada impresión), sustituyendo los siguientes:
 * - Múltiplos de 3 por la palabra "fizz".
 * - Múltiplos de 5 por la palabra "buzz".
 * - Múltiplos de 3 y de 5 a la vez por la palabra "fizzbuzz".
 */
'''

number=1
my_list = []

while number <=100:
    if number % 5 == 0 and number % 3 == 0:
        my_list.append('fizzbuzz')
        number += 1
    elif number % 5 == 0:
        my_list.append('buzz')
        number += 1
    elif number % 3 == 0:
        my_list.append('fizz')
        number += 1
    else:
        my_list.append(number)
        number += 1


for element in my_list:
    print(element)