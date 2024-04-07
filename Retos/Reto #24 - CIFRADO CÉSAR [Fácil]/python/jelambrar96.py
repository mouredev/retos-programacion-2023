#!/usr/bin/python3

"""
# Reto #24: Cifrado César
/*
 * Crea un programa que realize el cifrado César de un texto y lo imprima.
 * También debe ser capaz de descifrarlo cuando así se lo indiquemos.
 *
 * Te recomiendo que busques información para conocer en profundidad cómo
 * realizar el cifrado. Esto también forma parte del reto.
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


import random


def cifrar_cesar(cadena: str, diccionario: dict):
    string_out = [ item if not item in diccionario.keys() else diccionario[item] 
                for item in cadena ]
    string_out = "".join(string_out)
    return string_out


def descifrar_cesar(cadena: str, diccionario: dict):
    string_out = [ item if not item in diccionario.keys() else diccionario[item] 
                for item in cadena ]
    string_out = "".join(string_out)
    return string_out


def crear_diccionario(llave: int):
    ord_a = ord('a')
    ord_z = ord('z')
    delta = ord_z - ord_a + 1
    return dict([ (chr(i), chr((i + llave - ord_a) % delta + ord_a)) for i in range(ord_a, ord_z + 1)])


def invertir_diccionario(llave: int):
    return crear_diccionario(-1 * llave)



if __name__ == '__main__':
    
    ord_a = ord('a')
    ord_z = ord('z')
    delta = ord_z - ord_a + 1

    llave_aleatoria = random.randint(1, delta)
    diccionario = crear_diccionario(llave_aleatoria)
    diccionario_invertido = invertir_diccionario(llave_aleatoria)

    print("Texto original:")
    texto = "El veloz murciélago hindú comía feliz cardillo y kiwi. La cigüeña tocaba el saxofón detrás del palenque de paja"
    texto = texto.lower()
    print(texto)
    print()
    
    print("Texto cifrado")
    texto_cifrado = cifrar_cesar(texto, diccionario)
    print(texto_cifrado)
    print()

    print("Texto descrifrado")
    texto_descifrado = descifrar_cesar(texto_cifrado, diccionario_invertido)
    print(texto_descifrado)
    print()



