# * Crea un generador de números pseudoaleatorios entre 0 y 100.
# * - No puedes usar ninguna función "random" (o semejante) del lenguaje de programación seleccionado.
# *
# * Es más complicado de lo que parece...

from datetime import datetime

def get_random():
    rand = datetime.now().microsecond / 10000
    return round(rand)

print("The random number is:",get_random())