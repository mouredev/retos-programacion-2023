from collections import Counter
import re
import string

def heterograma(diccionario = dict):
    for frecuency in diccionario.values():
        if frecuency > 1:
            return False
    return True
    # return sum(diccionario.values()) == len(diccionario.values()) ahorro de lineas pero mas ineficiente?

def isograma(diccionario = dict):
    frecuency_list = set()
    for frecuency in diccionario.values():
        frecuency_list.add(frecuency)
        if len(frecuency_list) > 1:
            print(frecuency_list)
            return False
    return True
    frecuency = set(diccionario.values())
    return len(frecuency) == 1
def pangrama(diccionario = dict):
    alpha = set(string.ascii_lowercase)
    alpha -= set(diccionario.keys())
    return len(alpha) == 0

def char_counter(string):
    tex_cleaned = re.sub(r"[\d\W]", "", string.lower().replace(" ", ""))
    return dict(Counter(tex_cleaned))



print(heterograma(char_counter('pero')))
print(isograma(char_counter('ppeerroo')))
print(pangrama(char_counter("Benjamín pidió una bebida de kiwi y fresa. Noé, sin vergüenza, la más exquisita champaña del menú")))

