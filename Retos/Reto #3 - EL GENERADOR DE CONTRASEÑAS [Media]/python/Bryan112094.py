# Escribe un programa que sea capaz de generar contraseñas de forma aleatoria.
# Podrás configurar generar contraseñas con los siguientes parámetros:
# - Longitud: Entre 8 y 16.
# - Con o sin letras mayúsculas.
# - Con o sin números.
# - Con o sin símbolos.
# (Pudiendo combinar todos estos parámetros entre ellos)

import string
import random

def generar(longitud, mayusculas, numeros, simbolos):
    total_caracteres = string.ascii_lowercase
    result = ''
    if longitud >= 8 and longitud <= 16:
        if mayusculas:
            total_caracteres += string.ascii_uppercase
        if numeros:
            total_caracteres += string.digits
        if simbolos:
            total_caracteres += string.punctuation
        for i in range(longitud):
            result += random.choice(total_caracteres)
        print(result)
    else:
        print("Longitud incorrecta. Longitud entre 8 y 16")

generar(9,True,True,False)
