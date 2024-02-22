'''
 * Crea un generador de números pseudoaleatorios entre 0 y 100.
 * - No puedes usar ninguna función "random" (o semejante) del lenguaje de programación seleccionado.
 *
 * Es más complicado de lo que parece...
'''

import time

class GeneradorPseudoaleatorio:
    def __init__(self):
        self.semilla = int(time.time() * 1000) % 1000  # Utiliza milisegundos actuales como semilla

    def pseudoaleatorio(self):
        a = 48271
        m = 2147483647  # 2^31 - 1

        self.semilla = (a * self.semilla) % m

        numero_aleatorio = self.semilla % 101

        return numero_aleatorio

generador = GeneradorPseudoaleatorio()
print(generador.pseudoaleatorio())
