'''
* Autor: Juan S. Casado
* Fecha: 29/09/2021
* Versión: 1.0
* Escribe un programa que muestre por consola (con un print) los
* números de 1 a 100 (ambos incluidos y con un salto de línea entre
* cada impresión), sustituyendo los siguientes:
* - Múltiplos de 3 por la palabra "fizz".
* - Múltiplos de 5 por la palabra "buzz".
* - Múltiplos de 3 y de 5 a la vez por la palabra "fizzbuzz".
'''
numbers = range(1, 101)
for n in numbers:
	if n % 3 == 0 and n % 5 == 0:
		print(f"{n} = fizzbuzz")
	elif n % 3 == 0:
		print(f"{n} = fizz")
	elif n % 5 == 0:
		print(f"{n} = buzz")
	else:
		print(n)
