'''
* Crea una función que sea capaz de leer el número representado por el ábaco.
 * - El ábaco se representa por un array con 7 elementos.
 * - Cada elemento tendrá 9 "O" (aunque habitualmente tiene 10 para realizar operaciones)
 *   para las cuentas y una secuencia de "---" para el alambre.
 * - El primer elemento del array representa los millones, y el último las unidades.
 * - El número en cada elemento se representa por las cuentas que están a la izquierda del alambre.
 *
 * Ejemplo de array y resultado:
 * ["O---OOOOOOOO",
 *  "OOO---OOOOOO",
 *  "---OOOOOOOOO",
 *  "OO---OOOOOOO",
 *  "OOOOOOO---OO",
 *  "OOOOOOOOO---",
 *  "---OOOOOOOOO"]
 *  
 *  Resultado: 1.302.790
'''
import sys
import signal
import time

def terminar(sig,frame):
    print("\n\n[!]Saliendo...\n")
    sys.exit(1)


signal.signal(signal.SIGINT,terminar)

def abaco(abaco):
    number = []
    c = 0
    for row in abaco:
        temp = row.split("---")
        temp = temp[0]
        number.append(str(len(temp)))

    num = int("".join(number))

    # Formatea el número con puntos para representar miles, millones, etc.
    formatted_num = "{:,}".format(num).replace(",", ".")

    print("Resultado:", formatted_num)
if __name__ == '__main__':

    abacoo = ["OOOOOOOOO---",
            "OOOOOOOOO---",
            "OOOOOOOOO---",
            "OOOOOOOOO---",
            "OOOOOOOOO---",
            "OOOOOOOOO---",
            "OOOOOOOOO---"]
    
    abaco(abacoo)
