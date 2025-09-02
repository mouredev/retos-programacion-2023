"""
Crea una función que dibuje una escalera según su número de escalones.
- Si el número es positivo, será ascendente de izquierda a derecha.
- Si el número es negativo, será descendente de izquierda a derecha.
- Si el número es cero, se dibujarán dos guiones bajos (__).
Ejemplo: 4
 *         _
 *       _|
 *     _|
 *   _|
 * _|
"""

def stairs(num_steps: int) -> None:
    """
    Draws a staircase in the console based on the given number of steps.

    - Positive values create an ascending staircase (left to right).
    - Negative values create a descending staircase (left to right).
    - Zero prints two underscores (__).

    Args:
        num_steps (int): Number of steps in the staircase.
    """
    _validate_steps(num_steps)
    if num_steps == 0:
        print("__")
    elif num_steps > 0:
        print(f"{'_':>{(num_steps * 2) + 1}}")
        for i in range(num_steps * 2, 0, -2):
            print(f"{'_|':>{i}}")
    else:
        print("_")
        for i in range(1, abs(num_steps * 2) + 1, 2):
            print(f"{'|_':>{i + 2}}")

def _validate_steps(steps: int) -> None:
    """
    Validate that the given input is an integer.

    Args:
        steps (int): The number of steps to validate.

    Raises:
        TypeError: If the input is not an integer.
    """
    if not isinstance(steps, int):
        raise TypeError("Solo se aceptan enteros como datos.")


if __name__ == "__main__":
    stairs(-6)
    stairs(6)
