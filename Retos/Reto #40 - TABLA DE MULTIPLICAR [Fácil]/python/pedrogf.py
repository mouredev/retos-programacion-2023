#
# Crea un programa que sea capaz de solicitarte un número y se
# encargue de imprimir su tabla de multiplicar entre el 1 y el 10.
# - Debe visualizarse qué operación se realiza y su resultado.
#   Ej: 1 x 1 = 1
#       1 x 2 = 2
#       1 x 3 = 3
#       ...
#

tabla = int(input('Que tabla de multiplicar quieres ver:'))

def tablaDel(tabla:int):
    for num in range(11):
        print(f"{tabla} + {num} = {tabla * num}")

tablaDel(tabla)