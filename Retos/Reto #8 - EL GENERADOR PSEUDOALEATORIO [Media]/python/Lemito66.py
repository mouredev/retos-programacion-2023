""" 
* Crea un generador de números pseudoaleatorios entre 0 y 100.
 * - No puedes usar ninguna función "random" (o semejante) del lenguaje de programación seleccionado.
 *
 * Es más complicado de lo que parece...
"""
import time
def number_random():
    now_time = time.time()
    return int(now_time * 1000000) % 101

print(number_random())

