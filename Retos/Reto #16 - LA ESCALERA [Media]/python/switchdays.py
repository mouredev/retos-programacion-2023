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

print("Para salir introduzca: fin")
contador_str = ""

while contador_str != "fin":

    contador_str = input("Introduce el número de escaleras:")

    if contador_str != "fin":
        contador = int(contador_str)
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
