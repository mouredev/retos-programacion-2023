"""
Reto #27: CUENTA ATRÁS
MEDIA | Publicación: 03/07/23 | Resolución: 10/07/23
/*
 * Crea una función que reciba dos parámetros para crear una cuenta atrás.
 * - El primero, representa el número en el que comienza la cuenta.
 * - El segundo, los segundos que tienen que transcurrir entre cada cuenta.
 * - Sólo se aceptan números enteros positivos.
 * - El programa finaliza al llegar a cero.
 * - Debes imprimir cada número de la cuenta atrás.
 */
"""

import time


def countdown(number, second):

    if number <= 0 or type(number)== float:
        print("\nError. El numero debe ser un entero positivo\n")
    else:
        for i in range(number, -1,-1):
            print(i)
            time.sleep(second)
        print("Boom!!! 💥")
        

countdown(8,2)