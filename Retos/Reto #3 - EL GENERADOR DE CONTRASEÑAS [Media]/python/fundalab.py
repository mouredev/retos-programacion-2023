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

import secrets
import random
import string

#función para generar el password
def generador_pass():
    return ''.join(secrets.choice(cadena) for _ in range(int(longitud_pass)))

longitud_pass = 0
simbolos = False
numeros = False
mayusculas = False
cadena = ""
password_gen = ""

#solicitamos la longitud desea de caracteres

while True:
    longitud_pass = input("Indique entre 8 y 16 caracteres para generar su password: ")
    try:
        if int (longitud_pass) < 8: 
            longitud_pass = 8
        if int (longitud_pass) > 16: 
            longitud_pass = 16
        print("Caracteres válidos: ", longitud_pass)
        break
    except ValueError:
        print("Ingrese un número válido")

#solicitamos si desea simbolos en el password    
while True:
    respuesta = input("Indique si desea símbolos en su password (si): ").lower()
    try:
        if respuesta == "si": 
            simbolos = True
            break
        elif respuesta == "no":
            simbolos = False
            break
    except ValueError:
        print("Ingrese una respuesta válida") 

 #solicitamos si desea numeros en el password    
while True:
    respuesta = input("Indique si desea números en su password (si): ").lower()
    try:
        if respuesta == "si": 
            numeros = True
            break
        elif respuesta == "no":
            numeros = False
            break
    except ValueError:
        print("Ingrese una respuesta válida")  

 #solicitamos si desea mayúsculas en el password    
while True:
    respuesta = input("Indique si desea mayúsculas en su password (si): ").lower()
    try:
        if respuesta == "si": 
            mayusculas = True
            break
        elif respuesta == "no":
            mayusculas = False
            break
    except ValueError:
        print("Ingrese una respuesta válida")
         
# examinamos las opciones para componer la cadena de donde extraeremos el password
cadena = string.ascii_lowercase
if simbolos == True: cadena = cadena + string.punctuation
if numeros == True: cadena = cadena + string.digits
if mayusculas == True: cadena = cadena + string.ascii_uppercase

print(generador_pass())