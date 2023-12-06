"""
 Crea 3 funciones, cada una encargada de detectar si una cadena de
 texto es un heterograma, un isograma o un pangrama.
 Debes buscar la definición de cada uno de estos términos.
"""
import string

def heterograma(palabra:str):
    letras:list = []
    for letra in palabra:
        letras.append(letra)

    if len(palabra) == len(set(letras)):
        return True
    else:
        return False

def isograma(palabra:str):
    contador:dict = {}
    for letra in palabra:
        if letra not in contador:
            contador[letra] = 0
        contador[letra] += 1

    if len(set(list(contador.values()))) == 1:
        return True
    else:
        return False

def pangrama(palabra:str):
    return True if all(letter in palabra for letter in string.ascii_lowercase) else False

print(heterograma('Calumbrientos'))
print(isograma('UNCOPYRIGHTABLE'))
print(pangrama('Extraño pan de col y kiwi se quemó bajo fugaz vaho'))

print(heterograma('Hello'))
print(isograma('Hello'))
print(pangrama('Hello'))
