#!/usr/bin/env python3

'''
/*
 * Crea un generador de números pseudoaleatorios entre 0 y 100.
 * - No puedes usar ninguna función "random" (o semejante) del lenguaje de programación seleccionado.
 *
 * Es más complicado de lo que parece...
 */
'''

# Xn+1​=(a⋅Xn​+c)mod m

# INPUT a c
# X0 = 0
# m = 100

import time
import os

class GeneradorPseudoaleatorio:

    def __init__(self,a,c,m):
        self.a = a
        self.c = c 
        self.m = m 
        self.no_pseudoaleatorios = []

    def limpiar_pantalla(self):
        if os.name == 'posix':
            os.system('clear')
        else:
            os.system('cls')        

    def get_seed(self):
        return time.time_ns()

    def generador(self,i):
        seed = self.get_seed() * i if i != 0 else self.get_seed() * self.get_seed()
        num_rand = ((self.a*seed)+self.c) % 101 
        return num_rand

    def mostrar_resultado(self):
        print('\n[+] Conjunto de 100 números aleatorios entre el 0 y el 100:')
        print(f'\n{self.no_pseudoaleatorios}\n')


    def start(self):
        for i in range(0,100):
            random = self.generador(i)
            self.no_pseudoaleatorios.append(random)
        
        self.mostrar_resultado()

if __name__ == '__main__':
    try:
        generador = GeneradorPseudoaleatorio(4,8,100)
        generador.limpiar_pantalla()
        generador.start()
    except KeyboardInterrupt:
        print('\n\n[+] Saliendo...\n')