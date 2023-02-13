import random

letras = "abcdefghijklmnopqrstuvwxyz"

letras_mayus = "ABCDEFGHIJKLMNOPQRSTUVWXYZ"

numeros = "0123456789"

simbolos = "!#$%&/()<>*?=[]{\}|@"


def generador(longitud, opciones):
    contraseña = ""

    for i in range(longitud):
        caracter = random.choice(opciones)
        contraseña += caracter

    return contraseña


def opciones(parametros):
    match parametros:
        case "YYY":
            return letras + letras_mayus + numeros + simbolos
        case "YYN":
            return letras + letras_mayus + numeros
        case "YNY":
            return letras + letras_mayus + simbolos
        case "NYY":
            return letras + numeros + simbolos
        case "YNN":
            return letras + letras_mayus
        case "NYN":
            return letras + numeros
        case "NNY":
            return letras + simbolos
        case "NNN":
            return letras


longitud = int(input("Cuál es la longitud que quieres para tu contraseña? (8 a 16): "))
incluir_mayus = input("Quieres incluir letras mayusculas? (Y / N): ").upper()
incluir_nums = input("Quieres incluir numeros? (Y / N): ").upper()
incluir_simbolos = input("Quieres incluir símbolos? (Y / N): ").upper()

parametros = incluir_mayus + incluir_nums + incluir_simbolos

contraseña = generador(longitud, opciones(parametros))

print(contraseña)
