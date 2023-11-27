""" /*
 * Crea un programa que sea capaz de solicitarte un número y se
 * encargue de imprimir su tabla de multiplicar entre el 1 y el 10.
 * - Debe visualizarse qué operación se realiza y su resultado.
 *   Ej: 1 x 1 = 1
 *       1 x 2 = 2
 *       1 x 3 = 3
 *       ... 
 */ """

def tabla(num : int):
    print("La tabla de multiplicar del número",num, "es:")
    for index in range(1,11):
        resultado = num * index
        print(num,"x",index,"=",resultado)

try:
    numero = int(input("Introduce un número: "))
    tabla(numero)
except ValueError:
    print("Por favor, ingresa un número entero válido.")