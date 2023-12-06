"""
 * Crea 3 funciones, cada una encargada de detectar si una cadena de
 * texto es un heterograma, un isograma o un pangrama.
 * - Debes buscar la definición de cada uno de estos términos.
"""

import re
from unidecode import unidecode     # pip install unidecode

def checkHeterogram(text):
    text = list(text.lower())

    text_set = set(text)

    return len(text_set) == len(text)


def checkIsogram(text):
    prevNum = None
    text = text.lower()

    for letter in text:
        regex = f"{letter}"
        actualNum = len(re.findall(regex, text))

        if prevNum and prevNum != actualNum:
            return False

        prevNum = actualNum

    return True


def checkPangram(text):
    alphabet = list("abcdefghijklmnopqrtsuvwxyz")

    text = text.lower()
    text = unidecode(text)
    text = re.sub("[\u0300-\u036f]", '', text)
    text = re.sub("[\d\W\s]", '', text)

    for letter in alphabet:
        if letter not in text:
            return False

    return True


# heterograma = texto que no contiene letras repetidas
print(checkHeterogram("Hola"))                            # true
print(checkHeterogram("Hello"))                           # false
print(checkHeterogram("abcdefghijklmnopqrstuvwxyz"))      # true


# isograma = texto donde cada letra aparece el mismo número de veces
print(checkIsogram("hola"))           	# true -> todas se repiten 1 vez
print(checkIsogram("Hhoollaa"))       	# true -> se repiten 2 veces
print(checkIsogram("Hholla"))         	# false


# pangrama = texto que usa todas las letras del alfabeto de un idioma determinado
# panagram examples
str1 = "the quick brown fox jumps over the lazy dog" 
str2 = "When zombies arrive quickly fax judge pat" 
str3 = "Sixty zippers were quickly picked from the woven jute bag." 
str4 = "El veloz murciélago hindú comía feliz cardillo y kiwi, la cigüeña tocaba el saxofón detrás del palenque de paja" 

print(checkPangram(str1))         # true
print(checkPangram(str2))         # true
print(checkPangram(str3))         # true
print(checkPangram(str4))         # true
print(checkPangram("This is not a pangram"))              # false
print(checkPangram("abcdefghijklmnopqrstuvwxyz"))         # true
print(checkPangram("abcdefghijklmnñopqrstuvwxyz"))        # true