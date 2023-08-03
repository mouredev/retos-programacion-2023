"""# Reto #8: El generador pseudoaleatorio
#### Dificultad: Media | Publicación: 20/02/23 | Corrección: 27/02/23

## Enunciado

 Crea un generador de números pseudoaleatorios entre 0 y 100.
 - No puedes usar ninguna función "random" (o semejante) del lenguaje de programación seleccionado.
 Es más complicado de lo que parece...

"""
import datetime 
import time

def random():
    return datetime.datetime.now().microsecond%101

for __ in range(100):
    print(random())