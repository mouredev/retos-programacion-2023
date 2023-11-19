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
import time


def get_parameters():
    start_timer = int(input("Start Timer: "))
    interval = int(input("Intervalo: "))
    if start_timer > 0 and interval > 0:
        return (start_timer, interval)
    else:
        raise ValueError("Los numeros tienen que ser enteros positivos")


def timer(start_timer, interval):
    for i in range(start_timer):
        print(start_timer - i)
        time.sleep(interval)
    print("0! Cuenta Atras Terminada")


def main():
    timer(*get_parameters())


if __name__ == "__main__":
    main()
