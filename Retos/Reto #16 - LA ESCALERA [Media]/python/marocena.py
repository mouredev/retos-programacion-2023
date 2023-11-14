'''
/*
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
 */
'''

def draw_stairs(n):
    if n > 0:
        i = 0
        start_position = (n*2)+1
        while i < start_position:
            position = f"{{:>{start_position-i}s}}"
            if i == 0:
                print(f"{position}".format('_'))
            else:
                print(f"{position}".format('_|'))
                i += 1

            i += 1
    elif n < 0:
        i = 1
        final_position = (abs(n)*2)+1
        while i <=  final_position:
            position = f"{{:>{i}s}}"
            if i == 1:
                print(f"{position}".format('_'))
            else:
                print(f"{position}".format('|_'))

            i += 2
    else:
        print("__")


n_stairs = eval(input("Enter number of stairs: "))

draw_stairs(n_stairs)