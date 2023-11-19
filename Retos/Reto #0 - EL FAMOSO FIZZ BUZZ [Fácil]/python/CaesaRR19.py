'''
 * Escribe un programa que muestre por consola (con un print) los
 * números de 1 a 100 (ambos incluidos y con un salto de línea entre
 * cada impresión), sustituyendo los siguientes:
 * - Múltiplos de 3 por la palabra "fizz".
 * - Múltiplos de 5 por la palabra "buzz".
 * - Múltiplos de 3 y de 5 a la vez por la palabra "fizzbuzz". 
'''
lista = [print('fizzbuzz') if numero % 15 == 0 else print('fizz') if numero % 3 == 0 else print('buzz') if numero % 5 == 0 else print(numero) for numero in range (1, 101)]
