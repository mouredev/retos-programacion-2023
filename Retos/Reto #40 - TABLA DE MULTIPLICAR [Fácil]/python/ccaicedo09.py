"""
 * Crea un programa que sea capaz de solicitarte un número y se
 * encargue de imprimir su tabla de multiplicar entre el 1 y el 10.
 * - Debe visualizarse qué operación se realiza y su resultado.
 *   Ej: 1 x 1 = 1
 *       1 x 2 = 2
 *       1 x 3 = 3
 *       ... 
"""

def main():
    number = int(input("Ingresa el número del que deseas saber su tabla de multiplicar ---> "))
    for i in range(1,11):
        print(f"{number} x {i} = {number*i}")
    
main()