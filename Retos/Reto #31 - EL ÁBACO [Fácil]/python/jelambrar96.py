#!/usr/bin/python3

"""
# Reto #31: El ábaco
/*
 * Crea una función que sea capaz de leer el número representado por el ábaco.
 * - El ábaco se representa por un array con 7 elementos.
 * - Cada elemento tendrá 9 "O" (aunque habitualmente tiene 10 para realizar operaciones)
 *   para las cuentas y una secuencia de "---" para el alambre.
 * - El primer elemento del array representa los millones, y el último las unidades.
 * - El número en cada elemento se representa por las cuentas que están a la izquierda del alambre.
 *
 * Ejemplo de array y resultado:
 * ["O---OOOOOOOO",
 *  "OOO---OOOOOO",
 *  "---OOOOOOOOO",
 *  "OO---OOOOOOO",
 *  "OOOOOOO---OO",
 *  "OOOOOOOOO---",
 *  "---OOOOOOOOO"]
 *  
 *  Resultado: 1.302.790
 */
"""

import random


__author__ = "Jorge Lambraño - jelambrar96"
__copyright__ = "Copyright 2024, retos-programacion-2023"
__credits__ = ["Brais Moure - mouredev"]
__license__ = "GPL"
__version__ = "1.0.1"
__maintainer__ = "Jorge Lambraño"
__email__ = "jelambrar@gmail.com"
__status__ = "Production"


def abaco_a_numero(lista_string):
	lista_string = lista_string[::-1]
	digitos = [ abaco_a_digito(item) for item in lista_string ]
	return sum([ item * 10 ** i for i, item in enumerate(digitos) ])


def digito_a_abaco(numero: int):
	return "0" * numero + "---" + "0"*(10 - numero)


def abaco_a_digito(cadena: str):
	return len(cadena.split("---")[0])


def numero_a_abaco(numero: int):
	lista_cifras = []
	while numero > 0:
		cifra = numero % 10
		numero //= 10
		lista_cifras.append(cifra)
	lista_cifras = lista_cifras + (7 - len(lista_cifras)) * [0]
	lista_cifras = lista_cifras[::-1]
	return [ digito_a_abaco(item) for item in lista_cifras]


def dibujar_abaco(abaco: list):
	for item in abaco:
		print(item)


if __name__ == '__main__':

	for i in range(10):

		numero = random.randint(1, 9999999)
		print("Numero original:", numero)
		abaco = numero_a_abaco(numero)
		dibujar_abaco(abaco)
		numero_traducido = abaco_a_numero(abaco)
		print("Numero traducido: ", numero_traducido)

		print()

