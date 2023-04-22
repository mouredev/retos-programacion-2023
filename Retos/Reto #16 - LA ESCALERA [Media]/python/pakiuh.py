# Primer reto que subo

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
 */
"""

def funcion_escalera(escalones:int):
    if escalones>0:
        print(" "*escalones*2+"  _") # para que no queden amontonados los escalones los multiplicamos por 2
        for escalon in range(escalones*2,1,-2): # vamos a construi la escalera desde el más alto al más bajo
            print(" "*escalon+"_|")
    elif escalones<0:
        print("_")
        for escalon in range(1,(escalones*2)*-1,2): # para saber cuantos escalones son multiplicamos por -1 el número de escalones
           print(" "*escalon+"|_")
    else:
        print("__")


funcion_escalera(4)