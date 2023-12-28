# /*
# * Crea un generador de números pseudoaleatorios entre 0 y 100.
# * - No puedes usar ninguna función "random" (o semejante) del lenguaje de programación seleccionado.
# *
# * Es más complicado de lo que parece...
# */

import time

# clase que genera numeros aleatorios usango la funcion lineal congruencial
# https://en.wikipedia.org/wiki/Linear_congruential_generator
# contiene un metodo estatico que devuelve un numero aleatorio
class CustomRandom:

    def _get_seed(self):
        # valores de la funcion lineal lcg
        multiplier = 1103515245
        increment = 12345
        bits = 2**31 - 1
        # obtenemos el tiempo actual en milisegundos
        time_actual = time.time_ns()
        return (multiplier * time_actual + increment) % bits
    @staticmethod
    def get_custom_random(min, max):
        random = CustomRandom()
        return min + (random._get_seed() % max)


# 10 numeros aleatorios entre 1 y 100
for i in range(10):
    print(CustomRandom.get_custom_random(1,100))