# /*
#  * Crea un programa que sea capaz de solicitarte un número y se
#  * encargue de imprimir su tabla de multiplicar entre el 1 y el 10.
#  * - Debe visualizarse qué operación se realiza y su resultado.
#  *   Ej: 1 x 1 = 1
#  *       1 x 2 = 2
#  *       1 x 3 = 3
#  *       ... 
#  */

def tabla10(num: int):
    try:
        num = int(num)
        
        for i in range(1, 11):
            print(f"{num} x {i} = {i*num}")
    except ValueError:
        print("El número introducido no es un valor entero")

tabla10(input("Introduce el número a multiplicar por la tabla del 10: "))