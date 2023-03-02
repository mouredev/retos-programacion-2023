def heterograma(texto: str):
    #  Creamos el texto sin espacios.
    texto_sin_espacios = texto.replace(" ", "")
    #  Utilizamos la estructura de datos set de python, que elimina automaticamente los duplicados.
    if len(texto_sin_espacios) == set(texto):
        #  Si tiene la misma longitud la lista y el set, significa que no hay duplicados.
        return True
    else:
        return False


def isograma(texto: str):
    #  Creamos el texto sin espacios.
    texto_sin_espacios = texto.replace(" ", "")
    #  Si la longitud de la frase es el doble que el set, significa que cada letra aparece dos veces.
    if (len(texto_sin_espacios) / 2) == len(set(texto_sin_espacios)):
        return True
    else:
        return False


def pangrama(texto: str):
    #  Lista con todas las letras en el alfabeto español.
    letras = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'ñ', 'o', 'p', 'q', 'r', 's', 't',
              'u', 'v', 'w', 'x', 'y', 'z']
    #  Por cada letra del texto, si es la primera vez que aparece se elimina de la lista de letras.
    for caracter in texto:
        if caracter in letras:
            letras.remove(caracter)
    #  Si no quedan letras en la lista al terminar la frase, significa que se han utilizado todas.
    if len(letras) == 0:
        return True
    else:
        return False

