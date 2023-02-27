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
	Objeto generador de numeros aleatorios
	definición : se utiliza la pseudo función ( a* x() + c )(mod 101) 
			donde los valores a y c son constante que elegimos a nuestro criterio.
			x() es una funcion que devuelve un valor, en nuestro caso utilizamos el reloj. 
			al valor resultante utilizamos el modulo 101 para poder obtener un valor de 0 a 100.s
   
   La secuencia de números enteros X 1 , X 2 , X 3 , … {\displaystyle X_{1},X_{2},X_{3},\dots } está definida por la relación de recurrencia:

    X i = ( a X i − 1 + c ) mod m {\displaystyle X_{i}=\left(aX_{i-1}+c\right){\bmod {m}}}

con 0 ≤ X i ≤ m − 1 {\displaystyle 0\leq X_{i}\leq m-1} donde m m (el módulo), a a (el multiplicador), c c (el incremento) y X 0 {\displaystyle X_{0}} (la semilla o valor inicial) son números enteros no negativos.

Además a los números m , a , c {\displaystyle m,a,c} y X 0 {\displaystyle X_{0}} se les impone las condiciones m > 0 {\displaystyle m>0}, 0 < a < m {\displaystyle 0<a<m}, 0 ≤ c < m {\displaystyle 0\leq c<m} y 0 ≤ X 0 < m {\displaystyle 0\leq X_{0}<m}. 
   
		
	'''
	def __init__(self,intervalo = 101):
		self.constante_a = 1
		self.constante_c = 37
		self.semilla = trunc( time() * 10_000_000 ) % intervalo
		self.intervalo = intervalo
	
	def get_random(self)-> int:
		
  	    # desplazamos los decimales para utilzar el intervalos inferior a los segundos. 
		numero_random = ( ((self.constante_a * self.semilla) + self.constante_c) % self.intervalo)
		print(numero_random)
		self.semilla = numero_random
		return numero_random

	def get_sec_random(self, cantidad: int ) -> set:
		
		list_random = []
		for i in range(cantidad + 1 ):
			list_random.append(self.get_random())
   
		return set(list_random)


	def __str__(self):
		return ( 	str(self.constante_a) + '\t' +
					str(self.constante_c) + '\t' +
					str(self.semilla) + '\t' +
					str(self.intervalo)+ '\t'   )

		

if __name__ == "__main__":
	generador  =  gen_random()
	for i in range(101):
		print( i , end='\t')
		#print(generador)
		generador.get_random()
		#print( generador.get_random() , end=" ")
  
	#print( generador.get_sec_random(101))



" 
Teorema 3.1 (Hull y Dobell, 1962)

Un generador congruencial tiene período máximo p = m {\displaystyle p=m} si y sólo si:

    c c y m m son primos relativos, i.e. m . c . d . ⁡ ( c , m ) = 1 {\displaystyle \operatorname {m.c.d.} (c,m)=1}.
    a − 1 {\displaystyle a-1} es múltiplo de todos los factores primos de m m (i.e. a = 1 mod ⁡ m {\displaystyle a=1\operatorname {mod} m}, para todo q q factor primo de m m).
    Si m m es múltiplo de 4 {\displaystyle 4}, entonces a − 1 {\displaystyle a-1} también lo ha de ser (i.e. m≡0mod4⇒a≡1mod4).

Algunas consecuencias:

    Si m m primo entonces p = m ⟺ a = 1 {\displaystyle p=m\Longleftrightarrow a=1}
    Un generador multiplicativo no cumple la condición 1.

Teorema 3.2 Un generador multiplicativo tiene período máximo p = m − 1 {\displaystyle p=m-1} si:

    m m es primo.
    a a es una raíz primitiva de m m, es decir, el menor entero q q tal que a q = 1 mod ⁡ m {\displaystyle aq=1\operatorname {mod} m} es q = m − 1 {\displaystyle q=m-1}.

Además de preocuparse de la longitud del ciclo, las secuencias generadas deben aparentar muestras i.i.d. U ( 0 , 1 ) {\displaystyle U(0,1)}. Por ejemplo, los valores generados pueden mostrar una estructura reticular.

    Marsaglia (1968): k-uplas de generadores multiplicativos contenidas en a lo sumo (k!m)1/khiperplanos paralelos.
    Generador RANDU de IBM (70’s):

library(rgl)
system.time(u <- RANDCN(9999))  # Generar
xyz <- matrix(u, ncol = 3, byrow = TRUE)

plot3d(xyz) 
# rglwidget()

Se han propuesto diversas pruebas (ver sección siguiente) para determinar si un generador tiene problemas de este tipo y se han realizado numerosos estudios para determinadas familias (e.g. Park y Miller, 1988, m=231−1).

    En cualquier caso, se recomienda considerar un «periodo de seguridad» ≈√p para evitar este tipo de problemas.
    Aunque estos generadores tiene limitaciones en su capacidad para producir secuencias muy largas de números IID U ( 0 , 1 ) {\displaystyle \operatorname {IID} \;U(0,1)}, es un elemento básico en generadores más avanzados.
"

