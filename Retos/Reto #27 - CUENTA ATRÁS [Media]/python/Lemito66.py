"""
 * Crea una función que reciba dos parámetros para crear una cuenta atrás.
 * - El primero, representa el número en el que comienza la cuenta.
 * - El segundo, los segundos que tienen que transcurrir entre cada cuenta.
 * - Sólo se aceptan números enteros positivos.
 * - El programa finaliza al llegar a cero.
 * - Debes imprimir cada número de la cuenta atrás. 
"""

import time

def count_down(start: int, seconds: int):
    numbers = []
    if isinstance(start, int) and isinstance(seconds, int) and  start > 0 and seconds > 0:
        for i in range(start, 0, -1):
            numbers.append(i)
        return numbers
    else:
        raise Exception("Los parámetros tienen que ser enteros positivos")

print("Cuenta atrás")

for number in count_down(10, 1):
    print(number)
    time.sleep(1)