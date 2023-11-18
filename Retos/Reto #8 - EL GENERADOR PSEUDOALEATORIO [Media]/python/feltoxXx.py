# Reto #8: El generador pseudoaleatorio


#
# Crea un generador de números pseudoaleatorios entre 0 y 100.
# - No puedes usar ninguna función "random" (o semejante) del lenguaje de programación seleccionado.
# 
# Es más complicado de lo que parece...
# 

import time

def rand_val(x):

    random=int(time.time()*1000)

    random %= (x + 1)

    return random


for x in range(100):
    print(rand_val(x))
