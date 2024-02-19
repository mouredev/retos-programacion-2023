"""
Reto #40: TABLA DE MULTIPLICAR
FÁCIL | Publicación: 09/10/23 | Resolución: 16/10/23
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

def tabla(num):
    
    row = [f'{num} x {x} = {num * x}' for x in range(1,11)]

    return row


t = int(input("ingrese numero menor o igual a 10:   "))
#print(i for i in tabla(t))
print(tabla(t))
