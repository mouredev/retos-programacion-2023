'''
Escribe un programa que sea capaz de generar contraseñas de forma aleatoria.
Podrás configurar generar contraseñas con los siguientes parámetros:
- Longitud: Entre 8 y 16.
- Con o sin letras mayúsculas.
- Con o sin números.
- Con o sin símbolos.
(Pudiendo combinar todos estos parámetros entre ellos)
'''
longitud = int(input("Introduce la longitud de la contraseña: "))
mayusculas = input("¿Quieres mayúsculas? (S/N): ")
numeros = input("¿Quieres números? (S/N): ")
simbolos = input("¿Quieres símbolos? (S/N): ")

import random
import string

def generar_contrasena(longitud, mayusculas, numeros, simbolos):
    caracteres = string.ascii_lowercase
    if mayusculas.upper() == "S" :
        caracteres += string.ascii_uppercase
    if numeros.upper() == "S":
        caracteres += string.digits
    if simbolos.upper() == "S":
        caracteres += string.punctuation
    contrasena = "".join(random.choice(caracteres) for i in range(longitud))
    return contrasena

print(generar_contrasena(longitud, mayusculas, numeros, simbolos))