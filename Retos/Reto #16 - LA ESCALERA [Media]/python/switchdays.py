""""
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

def crear_escaleras(contador_str0):

    contador = int(contador_str0)
    espacios = 0

    if contador == 0:
        print("__")

    elif contador > 0:
        espacios = contador * 2
        print((espacios + 2) * " " +"_")
        while contador != 0:
            print(espacios * " " + "_|")
            contador -= 1
            espacios -= 2

    elif contador < 0:
        print("_")
        espacios = 1
        while contador != 0:
            print(espacios * " " + "|_")
            contador += 1
            espacios += 2

print("Para salir introduzca: fin")
contador_str1 = ""

while contador_str1 != "fin":

    contador_str1 = input("Introduce el número de escaleras:")
    if contador_str1 != "fin":
        crear_escaleras(contador_str1)
