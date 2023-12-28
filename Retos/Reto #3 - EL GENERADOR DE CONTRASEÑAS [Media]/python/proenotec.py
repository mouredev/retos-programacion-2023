#!/usr/bin/python3
# -*- coding: utf-8 -*-
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
import random
import argparse
import string

def generaListaAscii(mayusculas=False, numeros=False, simbolos=False):
    lista = list(string.ascii_lowercase)
    if mayusculas:
        lista += list(string.ascii_uppercase)
    if numeros:
        lista += list(string.digits)
    if simbolos:
        lista += list(string.punctuation)
    return lista


def dimePass (NElementos=8,mayusculas=False, numeros=False, simbolos=False):
    elementos = generaListaAscii(mayusculas, numeros, simbolos)
    MiPwd = ""
    for nElemento in range(NElementos):
        MiPwd += random.choice(elementos)
    return MiPwd

if __name__ == "__main__":
    parser = argparse.ArgumentParser()
    parser.add_argument("-l", "--longitud", help="Longitud de la contraseña, por defecto será de 8.", type=int, default=8,choices=range(8,17))
    parser.add_argument("-m", "--mayusculas", help="Usar letras mayúsculas.", action="store_true", default=False)
    parser.add_argument("-n", "--numeros", help="Usar números.", action="store_true", default=False)
    parser.add_argument("-s", "--simbolos", help="Usar símbolos.", action="store_true", default=False)
    argumentos = parser.parse_args()

    random.seed()
    print(dimePass(argumentos.longitud, argumentos.mayusculas, argumentos.numeros, argumentos.simbolos))
