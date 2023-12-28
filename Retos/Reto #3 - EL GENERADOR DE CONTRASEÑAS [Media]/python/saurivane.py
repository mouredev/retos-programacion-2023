"""
/*
 * Escribe un programa que sea capaz de generar contraseñas de forma aleatoria.
 * Podrás configurar generar contraseñas con los siguientes parámetros:
 * - Longitud: Entre 8 y 16.
 * - Con o sin letras mayúsculas.
 * - Con o sin números.
 * - Con o sin símbolos.
 * (Pudiendo combinar todos estos parámetros entre ellos)
 */
 """

import random
import string

def contraseña(long, mayus, num, sim):
 
    contraseña = ""
    azar = "abcdefghijklmnñopqrstuvwxyz"
    
    if mayus == "S":
       azar = azar + "ABCDEFGHIJKLMNÑOPQRSTUVWXYZ"
        
    if num == "S":
        azar = azar + "0123456789"
    
    if sim == "S":
        azar = azar + "ºª\\!|@·#$%&/()=?\'¿¡€^`[*+]¨´><;,:._-"
        
    if long == "A" or "8":
        for i in range(0,8):
            contraseña = contraseña + random.choice(azar)
    elif long == "B" or "16":
        for i in range(0,16):
            contraseña = contraseña + random.choice(azar)
    
    return contraseña
 
longitud = (input("Elige la longitud de la contraseña entre A)8 o B)16: "))
mayusculas = input("Con mayusculas? S/N: ")
numeros = input("Con númros?S/N: ")
simbolos = input("Con símbolos?S/N: ")

print(contraseña(longitud.upper(), mayusculas.upper(), numeros.upper(), simbolos.upper()))

 