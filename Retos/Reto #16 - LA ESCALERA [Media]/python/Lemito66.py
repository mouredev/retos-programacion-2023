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
    up_to_0 = ''
    down_to_0 = ''
    if number == 0:
        return '__'
    elif number > 0:
        up_to_0 += ' '*(number+1) + '_\n'
        for i in range(number):
            up_to_0 += ' '*(number-i-1) + '_|\n'
        return up_to_0
    else:
        for i in range(abs(number)):
            down_to_0 += ' '*i + '|_\n'
            # print(' '*i + '|_')
        down_to_0 += ' '*(i+2) + "|"
        return down_to_0


print(ladder(-3))

