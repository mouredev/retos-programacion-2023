# Reto #8: El generador pseudoaleatorio
# Crea un generador de números pseudoaleatorios entre 0 y 100.
# -No puedes usar ninguna función "random" (o semejante) del lenguaje de programación seleccionado.
import datetime

def pseudoaleatorio():
    hora_actual = datetime.datetime.now()
    return hora_actual.microsecond%101
    
    
print(pseudoaleatorio())



