"""
 * Crea un generador de números pseudoaleatorios entre 0 y 100.
 * - No puedes usar ninguna función "random" (o semejante) del 
 *   lenguaje de programación seleccionado.
 *
 * Es más complicado de lo que parece...
"""
import time
import math
 
ts = time.time()
parte_decimal, parte_entera = math.modf(ts)
 
print(round(parte_decimal * 100))
