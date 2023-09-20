"""/*
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
 */"""
import sys

def get_number():
    
    try:
        steps = int(input("Numero de Escalones: "))
    except ValueError:
        sys.exit("Tienes que introducir un numero negativo,positivo o 0")
        
def main():
    number_steps = get_number()

if __name__ == "__main__":
    main()
    