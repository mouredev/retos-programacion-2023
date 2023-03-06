"""
 * Crea 3 funciones, cada una encargada de detectar si una cadena de
 * texto es un heterograma, un isograma o un pangrama.
 * - Debes buscar la definición de cada uno de estos términos.
"""


def is_heterograma(word):
    arr_words = []
    for e in word:
        if e not in arr_words:
            arr_words.append(e)
    return len(arr_words) == len(word)


def is_isograma(word):
    obj_words = {}
    for e in word:
        if e in obj_words:
            obj_words[e] += 1
        else:
            obj_words[e] = 1
    return all(e % 2 == 0 or e == 1 for e in obj_words.values())


def is_pangrama(word):
    alphabet = 'abcdefghijklmnñopqrstuvwxyz'
    arr_words = []
    for e in word:
        if e.lower() not in arr_words and e.lower() in alphabet:
            arr_words.append(e.lower())
    return len(arr_words) == 27


print(is_heterograma('luteranismo'))
print(is_isograma('papelera'))
print(is_pangrama('Benjamín pidió una bebida de kiwi y fresa. Noé, sin vergüenza, la más exquisita champaña del menú.'))
