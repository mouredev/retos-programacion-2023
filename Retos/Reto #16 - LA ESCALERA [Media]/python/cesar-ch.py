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


def Ladder(num):
    ladder = ''
    if num == 0:
        ladder = '__'
    elif num > 0:
        for i in range(num):
            if i == 0:
                ladder += ' ' * (num - i) * 2
                ladder += '_\n'
            ladder += ' ' * (num - i-1) * 2
            ladder += '_|\n'
    else:
        for i in range(abs(num)):
            if i == 0:
                ladder += '_\n'
            ladder += ' ' * ((i) * 2 + 1)
            ladder += '|_\n'

    return ladder


print(Ladder(7))
print(Ladder(-7))
