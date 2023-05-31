'''/*
 *	¡El nuevo "The Legend of Zelda: Tears of the Kingdom" ya está disponible! 
 *
 * Crea un programa que dibuje una Trifuerza de "Zelda"
 * formada por asteriscos.
 * - Debes indicarle el número de filas de los triángulos con un entero positivo (n).
 * - Cada triángulo calculará su fila mayor utilizando la fórmula 2n-1.
 *
 * Ejemplo: Trifuerza 2
 * 
 *    *
 *   ***
 *  *   *
 * *** ***
 *
 */'''
 
while True:
    try:
        tamaño = int(input("ingrese el tamaño: "))
        if tamaño > 0:
            break
        else:
            print("Intente con un numero positivo") 
    except ValueError:
        print("Intente con un numero")
        
base_ind = 2 * tamaño - 1
filas = tamaño * 2
base_total = base_ind * 2 + 1

for i in range(0,tamaño):
    print(" "*(base_ind - i) + "*"* (2*i+1))
for i in range(0,tamaño):
    print(" "*(tamaño - i-1) + "*"*(2*i+1) + " "*(base_ind  - 2*i) + "*"*(2*i+1))

