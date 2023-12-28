#!/usr/bin/env python
'''
 - Crea un generador de números pseudoaleatorios entre 0 y 100.
No puedes usar ninguna función "random" (o semejante) del lenguaje de programación seleccionado.
Es más complicado de lo que parece...
 '''

import time
class Generador:
    def __init__(self, patron):
        self.patron = patron
        self.a = 1664525
        self.c = 1013904223
        self.m = 2**32
    
    def numero_aleatorio(self):
        self.patron = (self.a * self.patron + self.c) % self.m
        return self.patron % 101

cantidad = int(input("Cuantos numeros desea generar?"))

for i in range(cantidad):
        patron = int(time.time())
        generador = Generador(patron)
        num_aleatorio = generador.numero_aleatorio()
        print(num_aleatorio)
        time.sleep(1.1)
