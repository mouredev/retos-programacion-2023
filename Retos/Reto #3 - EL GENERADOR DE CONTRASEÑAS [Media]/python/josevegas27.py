# Reto #3: EL GENERADOR DE CONTRASEÑAS
#### Dificultad: Media | Publicación: 16/01/23 | Corrección: 23/01/23

## Enunciado

'''
/*
 * Escribe un programa que sea capaz de generar contraseñas de forma aleatoria.
 * Podrás configurar generar contraseñas con los siguientes parámetros:
 * - Longitud: Entre 8 y 16.
 * - Con o sin letras mayúsculas.
 * - Con o sin números.
 * - Con o sin símbolos.
 * (Pudiendo combinar todos estos parámetros entre ellos)
 */
 '''
import numpy as np


def generador_contraseña(Longitud,mayus:bool,number:bool,symbol:bool):

	symbols = ['!','"','#','$','%','&','/','(',')','=','?','.','-','_']
	numeros = list(range(0,10))
	letras = ['a','b','c','d','e','f','g','h','i','j','k','l','m','n','o','p','q','r','s','t','u','v','w','x','y','z']
	Letras = [letter.upper() for letter in letras]

	if mayus == 'True':
		letras += Letras
	if number == 'True':
		letras += numeros
	if symbol == 'True':
		print(symbol)
		letras += symbols

	if Longitud <8  or Longitud >16:
		print('La contraseña debe tener una longitud entre 8 y 16 caracteres')
		return None
	else:
		char = ''
		for i in np.random.choice(letras,Longitud):
			char += str(i)
		return char


print('GENERADOR DE CONTRASEÑAS:\n')

longitud =  int(input('Longitud de la contraseña: '))
mayus = 	input('¿Incluye Mayusculas? (True/False): ')
numbers = 	input('¿Incluye Numeros? (True/False): ')
symbols = 	input('¿Incluye Simbolos? (True/False): ')

print('La contraseña es: ',generador_contraseña(longitud,mayus,numbers,symbols))
