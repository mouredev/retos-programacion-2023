'''
	Reto #8: El generador pseudoaleatorio
/*
 * Crea un generador de números pseudoaleatorios entre 0 y 100.
 * - No puedes usar ninguna función "random" (o semejante) del lenguaje de programación seleccionado.
 *
 * Es más complicado de lo que parece...
*/
'''

from datetime import datetime

lista = []
def pseudo_random(start=0,finish=100, size=1):
	for i in range(0,size):
		a = datetime.now()
		lista.append(int(str(a)[-5:-3]))
		a = 2**(1000000 + i)	# Para ralentizar calculos y hacer que avance el tiempo

	print(lista)

randoms = int(input('Introduzca cuantos numeros aleatorios quiere. \n--> '))
pseudo_random(size=randoms)