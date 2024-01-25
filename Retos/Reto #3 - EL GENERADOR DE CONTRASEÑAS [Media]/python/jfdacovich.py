import random
import string

# Reto 3: El Generador de contraseñas 

""" Escribe un programa que sea capaz de generar contraseñas de forma aleatoria.
 * Podrás configurar generar contraseñas con los siguientes parámetros:
 * - Longitud: Entre 8 y 16.
 * - Con o sin letras mayúsculas.
 * - Con o sin números.
 * - Con o sin símbolos.
 * (Pudiendo combinar todos estos parámetros entre ellos)
 
 """


def generador_contrasenas(longitud_contrasena=8, mayusculas=False, numeros=False, simbolos=False):

    # Documentación consultada: https://docs.python.org/3/library/string.html#string.ascii_lowercase
    
    caracteres = string.ascii_lowercase
    # Longitud entre 8 y 16 caracteres
    longitud_contrasena = max(8, min(longitud_contrasena, 16))
    # Con o sin letras mayúsculas
    if mayusculas:
        caracteres += string.ascii_uppercase
    # Con o sin números
    if numeros:
        caracteres += string.digits
    # Con o sin símbolos
    if simbolos:
        caracteres += string.punctuation

    password = ""

    for i in range(longitud_contrasena):
        password += random.choice(caracteres)
    return password

# test

print(generador_contrasenas())
print(generador_contrasenas(longitud_contrasena=16))
print(generador_contrasenas(longitud_contrasena=1))
print(generador_contrasenas(longitud_contrasena=22))
print(generador_contrasenas(longitud_contrasena=12, mayusculas=True))
print(generador_contrasenas(longitud_contrasena=12, mayusculas=True, numeros=True))
print(generador_contrasenas(longitud_contrasena=12, mayusculas=True, numeros=True, simbolos=True))