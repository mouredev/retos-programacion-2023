"""
Crea una función que reciba dos parámetros para crear una cuenta atrás.
- El primero, representa el número en el que comienza la cuenta.
- El segundo, los segundos que tienen que transcurrir entre cada cuenta.
- Sólo se aceptan números enteros positivos.
- El programa finaliza al llegar a cero.
- Debes imprimir cada número de la cuenta atrás.
"""

import time

def countdown(start: int, delay: int) -> None:
    """
    Prints a countdown from a given starting number down to zero, pausing
    for a specified number of seconds between each printed value.

    Args:
        start (int): Positive integer that specifies where the countdown begins.
        delay (int): Positive integer indicating the number of seconds to wait
                    between each printed number.

    Raises:
        TypeError: If `start` or `delay` is not an integer.
        ValueError: If `start` or `delay` is less than or equal to zero.

    Returns:
        None
    """
    if not isinstance(start, int) or not isinstance(delay, int):
        raise TypeError("Error. Solo se aceptan valores enteros para el inicio o el tiempo.")

    if start <= 0 or delay <= 0:
        raise ValueError("Error. El numero de inicio o espera debe ser mayor a 0.")

    for i in range(start, -1, -1):
        print(i)
        time.sleep(delay)


if __name__ == "__main__":
    countdown(10, 2)
