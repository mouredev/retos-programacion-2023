"""

 * Crea una función que dibuje una escalera según su número de escalones.
 * - Si el número es positivo, será ascendente de izquiera a derecha.
 * - Si el número es negativo, será descendente de izquiera a derecha.
 * - Si el número es cero, se dibujarán dos guiones bajos (__).
 * 
 * Ejemplo: 4
 *         _
 *       _|       
 *     _|
 *   _|
 * _|
 *  

"""


def ladder(number: int) -> str:
    """The objective of the ladder function is to draw a ladder according to the number of steps provided as input. The ladder can be ascending or descending, depending on whether the input number is positive or negative, respectively. If the input number is zero, the function will return two underscores.

    Args:
        number (int):  number: an integer representing the number of steps in the ladder.

    Returns:
        str: ladder: a string representing the ladder.
    """
    greather_than_0 = ''
    less_than_0 = ''
    if number == 0:
        return '__'
    elif number > 0:
        greather_than_0 += f"{' '*(number+2)}_\n"
        for i in range(number):
            greather_than_0 += ' '*(number-i) + '_|\n'
        return greather_than_0
    else:

        for i in range(abs(number)):
            less_than_0 += ' '*i + '|_\n'
        less_than_0 += f"{' '*(abs(number)+1)}|"
        return less_than_0


print(ladder(-3))
print(ladder(3))