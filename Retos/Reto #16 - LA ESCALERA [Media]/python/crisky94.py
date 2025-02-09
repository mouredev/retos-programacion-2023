# /*
#  * Crea una función que dibuje una escalera según su número de escalones.
#  * - Si el número es positivo, será ascendente de izquiera a derecha.
#  * - Si el número es negativo, será descendente de izquiera a derecha.
#  * - Si el número es cero, se dibujarán dos guiones bajos (__).
#  * 
#  * Ejemplo: 4
#  *         _
#  *       _|       
#  *     _|
#  *   _|
#  * _|
#  * 
#  */

n = int(input("Ingrese el número de escalones: "))

def escaleras(n):
    if n >0:
        for i in range(n):
           print(" " * (n - i) + " " + "_" + "|"  )
    elif n < 0:
        for i in range(abs(n)):
            print(" " * (i + 1) + " " + "|" + "_")
    else:
        print("__")

escaleras(n)