"""
 * Crea una función que reciba dos parámetros para crear una cuenta atrás.
 * - El primero, representa el número en el que comienza la cuenta.
 * - El segundo, los segundos que tienen que transcurrir entre cada cuenta.
 * - Sólo se aceptan números enteros positivos.
 * - El programa finaliza al llegar a cero.
 * - Debes imprimir cada número de la cuenta atrás.
"""

import time

def count_down(start, step=1):
    if start < 0 or step < 0 or type(start) is not int or type(step) is not int:
        print('Error: The function only takes two positive integers as parameters!')
        return

    count = start

    print(count)
    count -= 1

    if count >= 0:
        time.sleep(step)
        count_down(count, step)


count_down(5, 1)