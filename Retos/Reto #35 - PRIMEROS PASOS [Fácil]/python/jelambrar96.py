#!/usr/bin/python3

"""
# Reto #35: Primeros pasos
/*
 * Como cada año, el día 256 se celebra el "Día de la Programación".
 * En nuestra comunidad siempre hacemos una gran fiesta donde repartirmos 
 * 256 regalos para seguir aprendiendo programación:
 * https://diadelaprogramacion.com
 *
 * Para seguir ayudando, te propongo este reto:
 * Mostrar la sintaxis de los principales elementos de un lenguaje
 * en TODOS los lenguajes de programación que podamos. ¿Llegaremos a 50?
 *
 * En un fichero, haz lo siguiente (si el lenguaje lo soporta),
 * y comenta cada bloque para identificar con qué se corresponde:
 * - Haz un "Hola, mundo!"
 * - Crea variables de tipo String, numéricas (enteras y decimales)
 *   y Booleanas (o cualquier tipo de dato primitivo).
 * - Crea una constante.
 * - Usa un if, else if y else.
 * - Crea estructuras como un array, lista, tupla, set y diccionario.
 * - Usa un for, foreach y un while.
 * - Crea diferentes funciones (con/sin parámetros y con/sin retorno).
 * - Crea una clase.
 * - Muestra el control de excepciones.
 *
 * Así, cualquier persona podrá consultar rápidamente diferentes ejemplos
 * de sintaxis básica de muchos lenguajes.
 *
 * ¡Muchas gracias!
 */
"""

__author__ = "Jorge Lambraño - jelambrar96"
__copyright__ = "Copyright 2024, retos-programacion-2023"
__credits__ = ["Brais Moure - mouredev"]
__license__ = "GPL"
__version__ = "1.0.1"
__maintainer__ = "Jorge Lambraño"
__email__ = "jelambrar@gmail.com"
__status__ = "Production"


# Imprimir Hola mundo
print("Hola mundo!")

# Variables
variable_cadena = "Esta es una variable de tipo cadena"
otra_cadena = "Esta es otra variable de tipo cadena"

numero_entero = 12
otro_numero_entero = 1

variable_bool = True

CONSTANTE_PI = 3.14159265

if numero_entero > 4:
	print("la variable 'numero entero' es mayor que 4")
	print("pero no te voy a decir que valor tiene")
else: 
	print("la variable 'numero entero' es menor o igual a 4")
	print("pero no te voy a decir que valor tiene")

# LISTAS
lista_de_supermercado = ["tomate", "cebolla", "ajo", "arroz"]

# TUPLAS 
tupla_colores = ("rojo", "naranja", "amarillo", "verde", "azul", "morado", "violeta")

# SET
primos_menores_10 = {2, 3, 5, 7}

# DICCIONARIO 
traduccion = {"hola": "hello", "adios": "goodbye"}

# BUCLE
print()
print("imprimir la lista de supermercado")
for item in lista_de_supermercado:
	print(item)
print()


print("mientras que el contador sea menor a pi, lo mostramos en pantalla")
contador = 0
while contador < CONSTANTE_PI:
	print("el valor del contador es ", contador)
	contador += 1


def es_primo(numero):
	if numero < 2:
		return False
	if numero == 3 or numero == 3:
		return True
	if numero % 2 == 0 or numero % 3 == 0:
		return False
	for i in range(5, numero // 3, 2):
		if numero % i == 0:
			return False
	return True


print("verificamos si los numeros dentro del conjunto primos_menores_10 son primos")
for item in primos_menores_10:
	print(item, "-", "" if es_primo(item) else "no", "es primo")


class Libro:
	def __init__(self, nombre, autor="desconocido"):
		self.nombre = nombre
		self.autor = autor
	def __str__(self):
		return f"Libro: '{self.nombre}' Author: {self.autor}" 

libro = Libro("La Odisea", "Homero")
print(libro)


try: 
	print(lista_de_supermercado[10])
except IndexError:
	print("lo siento, tu lista de supermercado no tiene tantos elementos")


print("Eso es todo por ahora!!!!")	

