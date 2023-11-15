'''
Crea un programa que sea capaz de solicitarte un número y se
 * encargue de imprimir su tabla de multiplicar entre el 1 y el 10.
 * - Debe visualizarse qué operación se realiza y su resultado.
 *   Ej: 1 x 1 = 1
 *       1 x 2 = 2
 *       1 x 3 = 3
 *       ... 
'''

def tabla_multiplicar(numero):
    for i in range(1, 11):
        total = numero * i
        print(f"{numero} x {i} = {total}")

numero = int(input("Ingrese un numero: "))
print("Tabla de multiplicar del numero:", numero)
tabla_multiplicar(numero)