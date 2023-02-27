#!/bin/python3

#/*
# * Crea un generador de números pseudoaleatorios entre 0 y 100.
# * - No puedes usar ninguna función "random" (o semejante) del 
# *   lenguaje de programación seleccionado.
# *
# * Es más complicado de lo que parece...
# */

# Nota; se puede utilizar la siguiente funcion 
# X(n+1) == ( ax(n) + c ) (mod m ) 
# donde x(n) + semilla 
# a  =  constante 
# c  =  constante
# m  = valor en que se encuentra el valor maximo de numeor aleatorios

from time import time
from math import trunc

class gen_random(object):
	'''
	Objeto generador pseudoaleatorio 
 
	Se utiliza la función Generador lineal congruencial (https://es.wikipedia.org/wiki/Generador_lineal_congruencial)
	definición : se utiliza la pseudo función X(n+1) = ( a*X(n) + c )(mod 101) 
			donde los valores a y c son constante que elegimos basado en el criterio de obtener un periodo igual a 100. Donde se cumple los siguientes criterios:
				. c y m son primos relativios. mcd(c,m)=1
				. a - 1 es múltiplo de todos los factores primos de m
				. Si m es multiplo de 4 entonces a -1 también.
			X(0) es una funcion que devuelve un valor, en nuestro caso utilizamos el reloj. 
			El modulo que se utiliza (101), es para poder obtener un valor de 0 a 100.
   	
	'''
	def __init__(self,intervalo = 101):
		self.constante_a = 3
		self.constante_c = 37
		self.semilla = trunc( time() * 10_000_000 ) % intervalo
		self.intervalo = intervalo
	
	def get_random(self)-> int:
		numero_random = ( ((self.constante_a * self.semilla) + self.constante_c) % self.intervalo)
		self.semilla = numero_random
		return numero_random


if __name__ == "__main__":
	generador  =  gen_random()
	for i in range(200):
		print( i , end='\t')
		print( generador.get_random() )
		