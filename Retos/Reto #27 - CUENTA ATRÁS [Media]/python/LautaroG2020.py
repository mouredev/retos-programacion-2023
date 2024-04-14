# /*
#  * Crea una función que reciba dos parámetros para crear una cuenta atrás.
#  * - El primero, representa el número en el que comienza la cuenta.
#  * - El segundo, los segundos que tienen que transcurrir entre cada cuenta.
#  * - Sólo se aceptan números enteros positivos.
#  * - El programa finaliza al llegar a cero.
#  * - Debes imprimir cada número de la cuenta atrás.
#  */

import time

def countdown(start: int, seconds: int):
    if not isinstance(start, int) or not isinstance(seconds, int) or start <= 0 or seconds <= 0:
        return print("Los parámetros tienen que ser enteros positivos")
    
    while start > 0:
        print(start)
        start -= 1
        time.sleep(seconds)

    print("Booooommmm 💥")

countdown(10, 1)