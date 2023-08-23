'''/*
 * Escribe un programa que muestre por consola (con un print) los
 * números de 1 a 100 (ambos incluidos y con un salto de línea entre
 * cada impresión), sustituyendo los siguientes:
 * - Múltiplos de 3 por la palabra "fizz".
 * - Múltiplos de 5 por la palabra "buzz".
 * - Múltiplos de 3 y de 5 a la vez por la palabra "fizzbuzz".
 */'''
for i in range(0,101):
    if((i % 3 == 0) and (i % 5 == 0)):
        print("fizzbuzz")
        #print(i)
    elif(i % 3 == 0):
        print("fizz")
        #print(i)
    elif(i % 5 == 0):
        print("buzz")