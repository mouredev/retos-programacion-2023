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
        return int(input("Numero de Escalones: "))
    except ValueError:
        sys.exit("Tienes que introducir un numero negativo,positivo u 0")
        
def stair_constructor(number_steps):
    
    if number_steps != 0:
        print_matrix(number_steps)
    else:
        print("__")
        
def print_matrix(number_steps):
    if number_steps > 0:
        for step in range(number_steps):
            if step == 0:
                print((((number_steps-1)*2)-(step*2)+2)*" ","_")
            print((((number_steps-1)*2)-(step*2))*" ","_|")
    else:
        number_steps = abs(number_steps)
        for step in range(number_steps):
            if step == 0:
                print((((step-1)*2)-(number_steps*2)+2)*" ","_")
            print(((step*2)+1)*" ","|_")
        
def main():
    number_steps = get_number()
    stair_constructor(number_steps)

if __name__ == "__main__":
    main()
    