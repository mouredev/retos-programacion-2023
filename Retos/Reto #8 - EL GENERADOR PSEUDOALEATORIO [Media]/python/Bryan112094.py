# Crea un generador de números pseudoaleatorios entre 0 y 100.
# - No puedes usar ninguna función "random" (o semejante) del lenguaje de programación seleccionado.
# Es más complicado de lo que parece...

import time
import math

def number_pseudo():
    tiempo_actual = time.time()
    valor, _ = math.modf(tiempo_actual)

    if int(valor * 1000) == 100:
        return 100
    else:
        return int(valor * 100)

print(number_pseudo())
