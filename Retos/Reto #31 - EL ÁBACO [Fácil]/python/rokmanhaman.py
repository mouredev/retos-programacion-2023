"""
Reto #31: EL ÁBACO
FÁCIL | Publicación: 31/07/23 | Resolución: 07/08/23
/*
 * Crea una función que sea capaz de leer el número representado por el ábaco.
 * - El ábaco se representa por un array con 7 elementos.
 * - Cada elemento tendrá 9 "O" (aunque habitualmente tiene 10 para realizar
 *   operaciones) para las cuentas y una secuencia de "---" para el alambre.
 * - El primer elemento del array representa los millones, y el último las unidades.
 * - El número en cada elemento se representa por las cuentas que están a
 *   la izquierda del alambre.
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
 */
"""



def abaco(array):

    num = ""
    for n in array:
        num += str(len(n.split("-")[0]))

    return num 


n = ["O---0OOOOOOO", "OOO---OOOOOO", "---OOOOOOOOO", "OO---OOOOOOO","OOOOOOO---OO","OOOOOOOOO---","---OOOOOOOOO"]

numero = abaco(n)

print(numero)
