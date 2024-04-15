# Reto #40: Tabla de multiplicar
#### Dificultad: Fácil | Publicación: 09/10/23 | Corrección: 16/10/23

## Enunciado

"""
/*
 * Crea un programa que sea capaz de solicitarte un número y se
 * encargue de imprimir su tabla de multiplicar entre el 1 y el 10.
 * - Debe visualizarse qué operación se realiza y su resultado.
 *   Ej: 1 x 1 = 1
 *       1 x 2 = 2
 *       1 x 3 = 3
 *       ... 
 */
"""


def multiply(number):
   
    for i in range(1, 11):
        print(f"{number} x {i} = {number * i}")

def error_handling():
    try:
        number = int(input("Ingrese un número entero: "))
        
    except ValueError:
        print("ValueError: No es un número entero.")
        error_handling()
        
    else:
        multiply(number)
            
error_handling()
