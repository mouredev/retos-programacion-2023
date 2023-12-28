"""
 * Crea una función que sea capaz de leer el número representado por el ábaco.
 * - El ábaco se representa por un array con 7 elementos.
 * - Cada elemento tendrá 9 "O" para las cuentas y una secuencia de "---" para el alambre.
 * - El primer elemento del array representa los millones, y el último las unidades.
 * - El número en cada elemento se representa por las cuentas que están a la izquierda del alambre.
 """
import re

def abaco(cuentas):
#Verificoque solo haya cuentas "O" y alambre "---"
    if not all(re.match(r'^[O-]+$', cuenta) for cuenta in cuentas):
        return "El ábaco está roto."
        
    total=''
    for cuenta in cuentas:
        if len(cuenta) ==  12:
            trozos_cuenta = cuenta.split('---')
            total=total+str(len(trozos_cuenta[0]))
        else:
            return ("El ábaco está roto.")
    return int(total)



#1.302.790
alambritos = ["O---OOOOOOOO","OOO---OOOOOO","---OOOOOOOOO","OO---OOOOOOO","OOOOOOO---OO","OOOOOOOOO---","---OOOOOOOOO"]
print(abaco(alambritos))
#0
alambritos = ["---OOOOOOOOO","---OOOOOOOOO","---OOOOOOOOO","---OOOOOOOOO","---OOOOOOOOO","---OOOOOOOOO","---OOOOOOOOO"]
print(abaco(alambritos))
#faltan bolitas
alambritos = ["---OOOOOO","---OOOOOOOOO","---OOOOOOO","---OOOOOOOO","---OOOOOOO","---OOOOO","---OOOOOOO"]
print(abaco(alambritos))
#1
alambritos = ["---OOOOOOOOO","---OOOOOOOOO","---OOOOOOOOO","---OOOOOOOOO","---OOOOOOOOO","---OOOOOOOOO","O---OOOOOOOO"]
print(abaco(alambritos))
#CUENTAS con ZEROS
alambritos = ["0---00000000","000---000000","---000000000","00---0000000","0000000---00","000000000---","---000000000"]
print(abaco(alambritos))
