'''
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
 '''

 
def main():
    
    steps = int(input("Introduce número de escalones: "))
    up = "_|"
    down = "|_"

    if steps>0:
        print("  "* (steps+1) + "_")
        for step in range(steps,0,-1):
            print("  "*step + up)
    elif steps<0:
        print(" _")
        for step in range(-1,steps-1,-1):
            print("  "*(-1*step) + down)
    else:
        print("__")

if __name__ == '__main__':
    main()
 