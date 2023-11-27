# Reto #40: Tabla de multiplicar
#### Dificultad: Fácil | Publicación: 09/10/23 | Corrección: 16/10/23

## Enunciado

'''
/*
 * Crea un programa que sea capaz de solicitarte un número y se
 * encargue de imprimir su tabla de multiplicar entre el 1 y el 10.
 * - Debe visualizarse qué operación se realiza y su resultado.
 *   Ej: 1 x 1 = 1
 *       1 x 2 = 2
 *       1 x 3 = 3
 *       ... 
 */
'''

numero = 0

while True:
    numero = int(input("Introduce un número del 1 al 10: "))
    if numero < 1 or numero > 10:
        print(f"El numero ", numero, " no esta comprendido entre 1 y 10")
    else:
        break

for i in range(10):
    resultado = numero * (i+1)
    print (numero," x ", i+1 ,"=", resultado)

