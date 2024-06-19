#!/usr/bin/env python3

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

limit_sup = 0
limit_inf = 0

in_range = False
longitud = 0

is_mayusculas = False
is_numeros = False
is_simbolos = False

mayusculas = [chr(i) for i in range(65, 91)]
minusculas = [chr(i) for i in range(97, 123)]
numeros = [chr(i) for i in range(48, 58)]
simbolos = [chr(i) for i in range(33, 48)] + [chr(i) for i in range(58, 64)] + [chr(i) for i in range(91, 97)] + [chr(i) for i in range(123, 127)]

contraseña = ''

while in_range == False: 
    longitud = int(input("\n[i] Ingrese la longitud que desea para su contraseña el valor tiene que estár entre 8 y 16 caracteres: "))

    in_range = True if not ( longitud < 8 or longitud > 16 ) else False

    if not in_range:
        print('\n\t[!] Solo se acepta una cantidad de 8 hasta 16 caracteres en la contraseña')

is_mayusculas = False if input("\n\t[i] Desea MAYÚSCULAS en su password (Si/No): ").lower() != 'si' else True
is_numeros = False if input("\n\t[i] Desea NÚMEROS en su password (Si/No): ").lower() != 'si' else True
is_simbolos = False if input("\n\t[i] Desea SÍMBOLOS en su password (Si/No): ").lower() != 'si' else True


i = 0
caracteres = minusculas.copy()
caracteres += mayusculas if is_mayusculas else [] 
caracteres +=  numeros if is_numeros else []
caracteres += simbolos if is_simbolos else []

while i < longitud:
    
    limit_sup = len(caracteres) - 1
    limit_inf = 0

    contraseña += caracteres[random.randint(limit_inf,limit_sup)] 
    i += 1



print(f'\n[+] Se ha generado la siguiente contraseña: {contraseña}')



