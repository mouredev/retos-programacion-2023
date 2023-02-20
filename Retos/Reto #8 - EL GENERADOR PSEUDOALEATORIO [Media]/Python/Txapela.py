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

# Existe el generador lineal congruencial (GLC), el método de congruencia lineal (LCG) que se basan
# en fórmulas matemáticas muy parecidas, por poner un ejemplo. Aquí he usado una mezcla del segundo
# combinado con la función "time", para usar el segundo del tiempo como parámetro aleatorio.
# También he puesto una función de espera de 1,1 segundos para poder generar la cantidad de números
# aleatorios introducidos por el usuario y que no se repitan al usar el mismo segundo.
