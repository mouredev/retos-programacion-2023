#
#Crea un generador de números pseudoaleatorios entre 0 y 100.
#No puedes usar ninguna función "random" (o semejante) del lenguaje de programación seleccionado.
#
#

class PseudoRandomGenerator:
    def __init__(self, seed):
        self.seed = seed

    def random(self):
        self.seed = (self.seed * 1103515245 + 12345) & 0x7fffffff
        return (self.seed // 65536) % 100

# Ejemplo de uso
seed = 42  # Cambia la semilla según desees
prng = PseudoRandomGenerator(seed)

for _ in range(10):
    print(prng.random())
