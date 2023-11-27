'''
 * Crea un programa que sea capaz de solicitarte un número y se
 * encargue de imprimir su tabla de multiplicar entre el 1 y el 10.
 * - Debe visualizarse qué operación se realiza y su resultado.
 *   Ej: 1 x 1 = 1
 *       1 x 2 = 2
 *       1 x 3 = 3
 *       ... 
'''
# Primera solución, con bucle for.
def tabla(n):
    for i in range(1,11):
        print(f"{n} x {i} = {n * i}")

# Segunda solución, con bucle while.
def tabla2(n):
    i = 1
    while i < 11:
        print(f"{n} x {i} = {n * i}")
        i=i+1

tabla(9)
tabla2(5)