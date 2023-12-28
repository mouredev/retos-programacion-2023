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
def draw_stairs(stairs):
    if stairs > 0:              # upward direction
        for stair in range(stairs + 1):
            if stair == 0: print((" " * stairs * 2) + "_")
            else: print(" " * ((stairs - stair) * 2) + "_|")

    elif stairs < 0:            # downward direction
        for stair in range(abs(stairs) + 1):
            if stair == 0: print("_")
            else: print(" " * (stair * 2 - 1) + "|_")

    elif stairs == 0:           # flat
        print("__")


draw_stairs(4)
draw_stairs(-4)
draw_stairs(0)