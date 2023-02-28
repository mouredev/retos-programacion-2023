""" 
 * Crea 3 funciones, cada una encargada de detectar si una cadena de
 * texto es un heterograma, un isograma o un pangrama.
 * - Debes buscar la definición de cada uno de estos términos.
"""

def heterograma(words: str):
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

print(heterograma("Víctima"))
print(heterograma("Wágner"))
print(heterograma("Queso"))
print(heterograma("Néctar"))
print(heterograma("Lánguido"))