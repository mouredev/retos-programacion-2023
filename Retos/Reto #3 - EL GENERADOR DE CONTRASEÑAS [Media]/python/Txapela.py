#!/usr/bin/env python

'''
 * Escribe un programa que sea capaz de generar contraseñas de forma aleatoria.
 * Podrás configurar generar contraseñas con los siguientes parámetros:
 * - Longitud: Entre 8 y 16.
 * - Con o sin letras mayúsculas.
 * - Con o sin números.
 * - Con o sin símbolos.
 * (Pudiendo combinar todos estos parámetros entre ellos)
'''

import secrets
import string

minus = string.ascii_lowercase
mayus = string.ascii_uppercase
numb = string.digits
spec = string.punctuation
password = ""
combi = ""

lenght = int(input("Introduzca la longitud de la password (8-16): "))

resp_minus = (input("Desea que contenga minusculas (S/N): ")).upper()
if resp_minus == "S": combi += minus

resp_mayus = (input("Desea que contenga mayusculas (S/N): ")).upper()
if resp_mayus == "S": combi += mayus

resp_numb = (input("Desea que contenga numeros (S/N): ")).upper()
if resp_numb == "S": combi += numb

resp_spec = (input("Desea que contenga caracteres especiales (S/N): ")).upper()
if resp_spec == "S": combi += spec

for i in range(lenght):
    password += ''.join(secrets.choice(combi))
print (password)
