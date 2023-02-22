"""
 * Crea un generador de números pseudoaleatorios entre 0 y 100.
 * - No puedes usar ninguna función "random" (o semejante) del lenguaje de programación seleccionado.
 *
 * Es más complicado de lo que parece...
"""

from datetime import datetime

def random_number():
    now = datetime.now()
    return now.microsecond % 101


print(random_number())