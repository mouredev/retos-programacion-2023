"""
 * Crea una función que reciba dos parámetros para crear una cuenta atrás.
 * - El primero, representa el número en el que comienza la cuenta.
 * - El segundo, los segundos que tienen que transcurrir entre cada cuenta.
 * - Sólo se aceptan números enteros positivos.
 * - El programa finaliza al llegar a cero.
 * - Debes imprimir cada número de la cuenta atrás.    
"""

import time

def countdown(total_time, split_time):
    if total_time <= 0 or split_time <= 0:
        raise ValueError("Los parámetros de entrada deben ser positivos")
    while total_time > 0:
        print(total_time)
        time.sleep(split_time)
        total_time -= split_time
    print("¡La cuenta ha llegado a 0!")


countdown(int(input("Introduce el tiempo total de la cuenta atrás: ")), int(input("Introduce los segundos que tienen que transcurrir entre cada cuenta: ")))
 