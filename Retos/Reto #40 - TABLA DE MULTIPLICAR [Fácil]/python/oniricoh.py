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

Tabla = int(input("¿Que tabla quieres aprender?:"))

print(f"\n\nLa tabla del {Tabla} es la siguiente:", end = '\n\n')

sol = 0
for i in range(0, 11):
    sol = i * Tabla
    print(Tabla, "*", i, "=", sol)
