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

def dibujarEscalon(posicion,escalon):    
    texto = " "*posicion+escalon
    print(texto)

escalones = None
while escalones is None:
    try:
        escalones = int(input("Ingresa el número de escalones: "))
    except ValueError:
        print('El valor ingresado no es un número entero')


if escalones == 0:
    print("__")
    
elif escalones > 0:
    print(" "*(escalones*2)+"_")
    for i in range(escalones,0,-1):
        dibujarEscalon(i*2-2,"_|")

else:
    print("_")
    for i in range(0,escalones*-1):
        dibujarEscalon(i*2+1,"|_")
