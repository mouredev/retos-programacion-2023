"""
Crea un generador de números pseudoaleatorios entre 0 y 100.
- No puedes usar ninguna función "random" (o semejante) del lenguaje de programación seleccionado.

Es más complicado de lo que parece...
"""
from datetime import datetime

if __name__ == '__main__':
    print(datetime.now().microsecond % 101)