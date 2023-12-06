"""
 * Crea un generador de números pseudoaleatorios entre 0 y 100.
 * - No puedes usar ninguna función "random" (o semejante) del 
 *   lenguaje de programación seleccionado.
 * Es más complicado de lo que parece...
"""
import time 

def pseudoaleatorio():
    n=str(time.monotonic_ns())              #ejecutamos time.monotonic_ns() para obtener un valor basado en la fechay hora
    n=n[-3:len(n)+1]                        #nos quedamos con los 3 últimos dígitos
    if n=="100":
        return int(n)                       #si tengo 100 y me voy
    else:
        n=n[-2:len(n)+1]                    #cualquier otro valor le saco un carácter por la izquierda y lo devuelvo como int
    return int(n)

print(pseudoaleatorio())
