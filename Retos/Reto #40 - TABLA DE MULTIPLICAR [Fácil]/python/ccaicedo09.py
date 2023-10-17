"""
 * Crea un programa que sea capaz de solicitarte un número y se
 * encargue de imprimir su tabla de multiplicar entre el 1 y el 10.
 * - Debe visualizarse qué operación se realiza y su resultado.
 *   Ej: 1 x 1 = 1
 *       1 x 2 = 2
 *       1 x 3 = 3
"""

def pedir_numero() -> int:
    n = int(input("Ingresa un número: "))
    return n
def tabla_de_multiplicar(n):
    for i in range(1, 11):
        print(f"{n} x {i} = {n * i}")

n = pedir_numero()
tabla_de_multiplicar(n)

