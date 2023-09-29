'''
 * Crea 3 funciones, cada una encargada de detectar si una cadena de
 * texto es un heterograma, un isograma o un pangrama.
 * - Debes buscar la definición de cada uno de estos términos.
'''

import string

def heterograma(texto):
    texto = texto.lower()
    letras = set()

    for caracter in texto:
        if caracter.isalpha():
            if caracter in letras:
                return False
            letras.add(caracter)

    return True

def isograma(texto):
    texto = texto.lower()
    letras = set()

    for caracter in texto:
        if caracter.isalpha():
            if caracter in letras:
                return False
            letras.add(caracter)

    return True

def pangrama(texto):
    texto = texto.lower()
    letras = set(texto)

    for letra in string.ascii_lowercase:
        if letra not in letras:
            return False

    return True

def verificaTexto(texto):
    if heterograma(texto):
        print("El texto ingresado es un heterograma.")
    elif isograma(texto):
        print("El texto ingresado es un isograma.")
    elif pangrama(texto):
        print("El texto ingresado es un pangrama.")
    else:
        print("El texto ingresado no es un heterograma, isograma ni pangrama.")

# Programa principal
textoIngresado = input("Ingresa un texto: ")
verificaTexto(textoIngresado)