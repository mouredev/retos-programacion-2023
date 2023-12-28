import random
"""
Escribe un programa que sea capaz de generar contraseñas de forma aleatoria.
Podrás configurar generar contraseñas con los siguientes parámetros:
    - Longitud: Entre 8 y 16.
    - Con o sin letras mayúsculas.
    - Con o sin números.
    - Con o sin símbolos.
(Pudiendo combinar todos estos parámetros entre ellos)
"""

def desordena_contrasena(lista):
    contrasena = ""
    random.shuffle(lista)

    for caracter in lista:
        contrasena += caracter

    return contrasena


def rellena_contrasena(mayus, minus, simbols, nums):
    minusculas = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't',
                'u','v', 'w', 'x', 'y', 'z']
    mayusculas = ['A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P', 'Q', 'R', 'S', 'T',
                'U', 'V', 'W', 'X', 'Y', 'Z']
    numeros = ['0', '1', '2', '3', '4', '5', '6', '7', '8', '9']
    simbolos = ['!', '#', '$', '%', '&', '(', ')', '*', '+']

    lista_contrasenya = []

    for mayuscula in range(0, mayus):
        lista_contrasenya += random.choice(mayusculas)

    for minuscula in range(0, minus):
        lista_contrasenya += random.choice(minusculas)

    for simbolo in range(0, simbols):
        lista_contrasenya += random.choice(simbolos)

    for numero in range(0, nums):
        lista_contrasenya += random.choice(numeros)

    return lista_contrasenya


def generador_contrasena():
    global cantidad_letras_minusculas
    cantidad_caracteres_totales = int(input("Longitud de la contraseña (min. 8, máx. 16)\n"))

    while cantidad_caracteres_totales < 8 or cantidad_caracteres_totales > 16:
        cantidad_caracteres_totales = int(input("Longitud de la contraseña (min. 8, máx. 16)\n"))

    cantidad_letras_mayusculas = int(input("¿Cuántas letras mayúsculas quieres?\n"))
    cantidad_simbolos = int(input("¿Cuantos símbolos quieres?\n"))
    cantidad_numeros = int(input("¿Cuántos números quieres?\n"))

    cantidad_total = cantidad_letras_mayusculas + cantidad_simbolos + cantidad_numeros

    if cantidad_total > cantidad_caracteres_totales:
        print("Se han seleccionado más caracteres de los elegidos inicialmente.")
    else:
        cantidad_letras_minusculas = cantidad_caracteres_totales - cantidad_total

    lista = rellena_contrasena(cantidad_letras_mayusculas, cantidad_letras_minusculas, cantidad_simbolos, cantidad_numeros)
    contrasena = desordena_contrasena(lista)

    print(contrasena)


generador_contrasena()
