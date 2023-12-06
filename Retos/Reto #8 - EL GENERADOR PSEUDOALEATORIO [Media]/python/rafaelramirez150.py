'''
 /*
 * Crea un generador de números pseudoaleatorios entre 0 y 100.
 * - No puedes usar ninguna función "random" (o semejante) del lenguaje de programación seleccionado.
 *
 * Es más complicado de lo que parece...
 */
 '''

class PseudoRandomGenerator: 
    def __init__(self, seed): 
        self.seed = seed 

    def generate(self):
        self.seed = (self.seed * 32719 + 3) % 32749 
        return self.seed % 101  # Genera números entre 0 y 100

# Ejemplo de uso
generator = PseudoRandomGenerator(5)  # Selecciona una semilla inicial

for _ in range(10):
    random_number = generator.generate()
    print(random_number)

