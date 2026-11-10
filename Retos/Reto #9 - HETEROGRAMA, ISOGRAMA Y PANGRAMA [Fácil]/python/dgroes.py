"""
* Crea 3 funciones, cada una encargada de detectar si una cadena de
* texto es un heterograma, un isograma o un pangrama.
* - Debes buscar la definición de cada uno de estos términos.
"""


"""
Un heterograma es una palabra o frase en la que ninguna letra del alfabeto se repite; es decir, cada letra aparece una sola vez.
Murciélago (m, u, r, c, i, é, l, a, g, o — ninguna letra se repite)

isograma: Es un concepto más amplio. En sentido estricto (y para muchos, sinónimo de heterograma), es una palabra 
o frase sin letras repetidas. Sin embargo, de manera más general, un isograma es una palabra donde cada letra aparece el 
mismo número de veces (por ejemplo, todas las letras aparecen 2 veces, como: "acondiciona", "Susa"



Pangrama: Es un texto (generalmente una frase) que contiene absolutamente todas las letras de un idioma al menos una vez. 
El objetivo aquí es la completitud del alfabeto. Un ejemplo clásico en español es: "El veloz murciélago hindú comió feliz cardillo y escayola" 
(contiene las 27 letras del abecedario).


"""

from collections import Counter
import unicodedata
import string
import re

def decomposeText(text):
    text = text.lower()

    # Quitar números
    text_without_numers = re.sub(r'\d', '', text)

    # Quitar caracteres
    clean_text = re.sub(r'[^a-zñ]', '', text_without_numers)

    # Quitar las tildes
    text_normalize = unicodedata.normalize('NFD', clean_text)
    text_without_tildes = "".join(c for c in text_normalize if unicodedata.category(c) != 'Mn')

    
    count = Counter(text_without_tildes)

    result = dict(count)

    return result


def heterograma(text):
    leters_list = decomposeText(text)


    result = not any(v > 1 for v in leters_list.values())

    if result is True:
        print(f"La palabra {text} es un Heterograma")
    else:
        print(f"La palabra {text} no es un Heterograma")


def isograma(text):
    leters_list = decomposeText(text)

    number = next(iter(leters_list.values()), None)

    # True si no hay ningún valor diferente al primero
    result = not any(v != number for v in leters_list.values())

    if result is True:
        print(f"La palabra {text} es un Isograma")
    else:
        print(f"La palabra {text} no es un Isograma")

def pangrama(text):
    alphabet = string.ascii_lowercase
    alphabet_list = list(alphabet)

    text_format = text.replace(" ", "")    
    leters_list = decomposeText(text_format)

    result = set(leters_list) == set(alphabet_list)

    if result is True:
        print(f"El Texto '\x1b[3m{text}\x1b[0m' es un Pangrama")
    else:
        print(f"El Texto '\x1b[3m{text}\x1b[0m' no es un Pangrama")

heterograma("Murciélago")
isograma("Hehehee")
pangrama("Benjamin Pardo el viejo saxofonista de la gran orquesta que toco un buen jazz con su whisky de kiwi")
