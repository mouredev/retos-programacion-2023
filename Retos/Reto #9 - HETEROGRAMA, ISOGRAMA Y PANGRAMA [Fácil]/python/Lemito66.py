""" 
 * Crea 3 funciones, cada una encargada de detectar si una cadena de
 * texto es un heterograma, un isograma o un pangrama.
 * - Debes buscar la definición de cada uno de estos términos.
"""

def heterograma(words: str):
    '''
    Un heterograma es una palabra o frase que no contiene ninguna letra repetida.
    '''
    diccionary_of_words = {}
    response = ''
    lower_word = words.lower()
    for i in range(len(lower_word)):
        if lower_word[i] in diccionary_of_words:
            response += 'No es un heterograma'
            return response
        else:
            diccionary_of_words[lower_word[i]] = 1
    response += 'Es un heterograma'
    return response

def isograma(words: str):
    '''
    Un isograma es una palabra o frase en la que cada letra aparece el mismo número de veces.
    '''
    dictionary_of_words = {}
    response = ''
    lower_word = words.lower()
    for i in range(len(lower_word)):
        if lower_word[i] in dictionary_of_words:
            dictionary_of_words[lower_word[i]] += 1
        else:
            dictionary_of_words[lower_word[i]] = 1
            
    for value in dictionary_of_words.values():
        if value > 1:
            response += 'No es un isograma'
            return response
    response += 'Es un isograma'
    return response

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