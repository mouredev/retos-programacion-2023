"""
/*
 * Crea una función que reciba dos parámetros para crear una cuenta atrás.
 * - El primero, representa el número en el que comienza la cuenta.
 * - El segundo, los segundos que tienen que transcurrir entre cada cuenta.
 * - Sólo se aceptan números enteros positivos.
 * - El programa finaliza al llegar a cero.
 * - Debes imprimir cada número de la cuenta atrás.
 */
"""
import time as t

def regresive_count (number: int, time: int):
    try:
        if isinstance(number, int) > 0 or isinstance(time, int) > 0:
            while number > -1:
                t.sleep(time)
                print(number)
                number -= 1
        if number < 0:
            print("funcion exitosa")
    except:
            print("Uno de los valores no es valido\nReinicie la funcion con valores enteros")

if __name__=="__main__":
    regresive_count(12,4)
