# Reto #8: El generador pseudoaleatorio
# Dificultad: Media | Publicación: 20/02/23 | Corrección: 27/02/23
#
# Enunciado
#
# Crea un generador de números pseudoaleatorios entre 0 y 100.
# - No puedes usar ninguna función "random" (o semejante) del lenguaje de programación seleccionado.
#
# Es más complicado de lo que parece...
#

import time

def random_number():

    seed = int(time.time())
    seed = (seed * 16807) % 2147483647
    seed = seed % 100
    
    return(seed + 1)

if __name__ == "__main__":
    print(random_number())