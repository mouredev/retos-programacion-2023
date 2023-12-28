"""
 * Crea una función que sea capaz de leer el número representado por el ábaco.
 * - El ábaco se representa por un array con 7 elementos.
 * - Cada elemento tendrá 9 "O" (aunque habitualmente tiene 10 para realizar
 *   operaciones) para las cuentas y una secuencia de "---" para el alambre.
 * - El primer elemento del array representa los millones, y el último las unidades.
 * - El número en cada elemento se representa por las cuentas que están a
 *   la izquierda del alambre.
 *
 * Ejemplo de array y resultado:
 * ["O---OOOOOOOO",1
 *  "OOO---OOOOOO",10
 *  "---OOOOOOOOO",100
 *  "OO---OOOOOOO",1000
 *  "OOOOOOO---OO",10000
 *  "OOOOOOOOO---",100000
 *  "---OOOOOOOOO"]1000000
 *  
 *  Resultado: 1.302.790
"""
"""nota: no lei el encabezado bien e hize un abaco funcional basandome en como funciona un abaco en la vida real"""

abaco =["O---OOOOOOOO",
        "OOO---OOOOOO",
        "---OOOOOOOOO",
        "OO---OOOOOOO",
        "OOOOOOO---OO",
        "OOOOOOOOO---",
        "---OOOOOOOOO"]


def abaco_f (abaco:list):
    val = 0
    multi = 1
    value_list = []
    
    for index in abaco:
        for vaule in index[::-1]:
            if vaule == "O":
                val += 1
            else:
                value_list.append(val*multi)
                if multi < 10:
                    multi += 9
                    val = 0
                    break
                else:
                    multi = multi * 10
                    val = 0
                    break
    vaule_sum = sum(value_list)
    print (vaule_sum)
abaco_f (abaco)
