#!/usr/bin/python3
# /*
#  * Escribe un programa que muestre por consola (con un print) los
#  * números de 1 a 100 (ambos incluidos y con un salto de línea entre
#  * cada impresión), sustituyendo los siguientes:
#  * - Múltiplos de 3 por la palabra "fizz".
#  * - Múltiplos de 5 por la palabra "buzz".
#  * - Múltiplos de 3 y de 5 a la vez por la palabra "fizzbuzz".
#  */

def revisarNumero(numero): # Función que remplaza un número múltiplo de 3 y 5 por "fizz", "buzz" y "fizzbuzz" según corresponda.
    if numero % 3 == 0 and numero % 5 == 0: # En caso de ser múltiplo de 3 y 5 a la vez, devuelve "fizzbuzz".
        return "fizzbuzz"
    elif numero % 3 == 0: # En caso de ser múltiplo de 3 devuelve "fizz".
        return "fizz"
    elif numero % 5 == 0: # En caso de ser múltiplo de 5 devuelve "buzz".
        return "buzz"
    else: # En caso de no cumplir ninguna condición, no modifica el número.
        return numero

for numero in range(1, 101):
    numero_revisado = revisarNumero(numero)
    print(numero_revisado)