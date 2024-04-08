"""
 Escribe un programa que sea capaz de generar contraseñas de forma aleatoria.
 Podrás configurar generar contraseñas con los siguientes parámetros:
 - Longitud: Entre 8 y 16.
 - Con o sin letras mayúsculas.
 - Con o sin números.
 - Con o sin símbolos.
 (Pudiendo combinar todos estos parámetros entre ellos)
 """

from random import *
import string

def reto_3():
    n_characters=randint(8,16)
    caracter = string.printable
    caracteres=caracter.strip()
    password=[]
    cont=0
    while cont<n_characters:
        letra=choice(caracteres)
        password.append(letra)
        cont+=1
    passw=''.join(password)
    print(passw)

reto_3()

