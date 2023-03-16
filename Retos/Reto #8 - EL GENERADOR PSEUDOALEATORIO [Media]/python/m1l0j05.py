# Crea un generador de números pseudoaleatorios entre 0 y 100.
# - No puedes usar ninguna función "random" (o semejante) del lenguaje de programación seleccionado.
#
# Es más complicado de lo que parece...
 
import time

def pseudo_generator(min=0, max=100):
    semilla = time.time_ns()
    a = 19810324
    b = 20171125
    m = 2**32

    semilla = (a * semilla + b) % m

    number = (semilla + min) % (max + 1)

    return number



for _ in range(0, 100):
    print(pseudo_generator(0, 50))