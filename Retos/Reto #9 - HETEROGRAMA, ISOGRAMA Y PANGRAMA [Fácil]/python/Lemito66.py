""" 
 * Crea 3 funciones, cada una encargada de detectar si una cadena de
 * texto es un heterograma, un isograma o un pangrama.
 * - Debes buscar la definición de cada uno de estos términos.
"""
def reemplazar_tildes(word: str):
    to_replace = {
        'á': 'a',
        'é': 'e',
        'í': 'i',
        'ó': 'o',
        'ú': 'u',
    }
    for words in to_replace:
        word = word.replace(words, to_replace[words])
    return word

def heterograma(words: str):
    '''
    Un heterograma es una palabra o frase que no contiene ninguna letra repetida.
    '''
    diccionary_of_words = {}
    response = ''
    new_word = reemplazar_tildes(words).lower()
    for i in range(len(new_word)):
        if new_word[i] in diccionary_of_words:
            response += 'No es un heterograma'
            return response
        else:
            diccionary_of_words[new_word[i]] = 1
    response += 'Es un heterograma'
    return response


def isograma(words: str):
    '''
    Un isograma es una palabra o frase en la que cada letra aparece el mismo número de veces.
    '''
    dictionary_of_words = {}
    response = ''
    new_word = reemplazar_tildes(words).lower()
    for i in range(len(new_word)):
        if new_word[i] in dictionary_of_words:
            dictionary_of_words[new_word[i]] += 1
        else:
            dictionary_of_words[new_word[i]] = 1

    for value in dictionary_of_words.values():
        if value > 1:
            response += 'No es un isograma'
            return response
    response += 'Es un isograma'
    return response


def pangrama(words: str):
    '''
    Un pangrama es una frase en la que aparecen todas las letras del abecedario
    '''
    new_word = reemplazar_tildes(words).lower()
    alphabet = {
        'a': 0, 'b': 0, 'c': 0, 'd': 0, 'e': 0, 'f': 0, 
        'g': 0, 'h': 0, 'i': 0, 'j': 0, 'k': 0, 'l': 0, 
        'm': 0, 'n': 0, 'ñ': 0, 'o': 0, 'p': 0, 'q': 0, 
        'r': 0, 's': 0, 't': 0, 'u': 0, 'v': 0, 'w': 0, 
        'x': 0, 'y': 0, 'z': 0
    }
    response = ''
    for word in range(len(new_word)):
        if new_word[word] in alphabet:
            alphabet[new_word[word]] += 1
    for value in alphabet.values():
        if value == 0:
            response += 'No es un pangrama'
            return response
    response += 'Es un pangrama'
    return response

print(pangrama("El veloz murciélago hindú comía feliz cardillo y kiwi. La cigüeña tocaba el saxofón detrás del palenque de paja"))
print(pangrama("Jovencillo emponzoñado de whisky, qué figurota exhibe. Cadáveres de ñus, paz y asombro, ¿qué más añadir?"))
print(pangrama("El pingüino Wenceslao hizo kilómetros bajo exhaustiva lluvia y frío, añoraba a su querido cachorro."))
print(pangrama("Victimá"))


print(isograma("Víctima"))
print(isograma("Políglota"))
print(isograma("Abstemio"))
print(isograma("Desoxirribonucleico"))
print(isograma("Hipopótamo"))
print(isograma("Benzodiacepina"))

print(heterograma("Víctima"))
print(heterograma("Wágner"))
print(heterograma("Queso"))
print(heterograma("Néctar"))
print(heterograma("Lánguido"))
