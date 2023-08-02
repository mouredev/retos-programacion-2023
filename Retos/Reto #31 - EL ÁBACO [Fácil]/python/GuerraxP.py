"""/*
 * Crea una función que sea capaz de leer el número representado por el ábaco.
 * - El ábaco se representa por un array/lista con 7 elementos.
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
 */"""

a=["O---OOOOOOOO",
   "OOO---OOOOOO",
   "---OOOOOOOOO",
   "OO---OOOOOOO",
   "OOOOOOO---OO",
   "OOOOOOOOO---",
   "---OOOOOOOOO"]

def abaco(a):
   
    result=0
    
    for i in a:
        cont=0
        for j in i:
            if j =="O":
                cont=cont+1
            else:
                if j =="-":
                    result= (result*10) +cont 
                break

    return result

print(abaco(a))
