""" /*
 * Crea un programa que sea capaz de solicitarte un número y se
 * encargue de imprimir su tabla de multiplicar entre el 1 y el 10.
 * - Debe visualizarse qué operación se realiza y su resultado.
 *   Ej: 1 x 1 = 1
 *       1 x 2 = 2
 *       1 x 3 = 3
 *       ... 
 */ """

def multiplication_table(number, stop):
    for numbers in range(0, stop + 1):
        print(f"{number} x {numbers} = {number * numbers}")
        
print("Multiplication table")
multiplication_table(5, 20)