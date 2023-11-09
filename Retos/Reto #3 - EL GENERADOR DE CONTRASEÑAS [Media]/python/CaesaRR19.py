import string
from random import choice


def creador_contraseñas(longitud=8, mayus=True, num=True, simb=True):
    diccionario = {
        "minusculas": string.ascii_lowercase,
        "mayusculas": string.ascii_uppercase,
        "numeros": string.digits,
        "simbolos": string.punctuation,
    }
    contra = ""
    if not mayus:
        del diccionario["mayusculas"]
    if not num:
        del diccionario["numeros"]
    if not simb:
        del diccionario["simbolos"]

    if longitud in range(8, 17):
        for _ in range(longitud):
            contra += choice(diccionario[choice(list(diccionario.keys()))])
        return contra
    return "Ingrese una longitud válida."


print(creador_contraseñas(16, False, False, True))
