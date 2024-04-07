'''/*
 * Crea un programa que analice texto y obtenga:
 * - Número total de palabras.
 * - Longitud media de las palabras.
 * - Número de oraciones del texto (cada vez que aparecen un punto).
 * - Encuentre la palabra más larga.
 *
 * Todo esto utilizando un único bucle.
 */'''

from functools import reduce

def text_analyzer(text:str) -> dict:
    data:dict = {}
    words:int = 0
    largest_word:str = ''

    data['total_senteces'] = 0

    # How many senteces are 
    if '.' in text:
        sentences:list[str] = text.split('.')
        data['total_senteces'] = len(sentences)

    # How many words are 
    for sentence in sentences:
        correct_sentence:str = sentence

        sentence = sentence.strip()
        if not ' ' in sentence[0]:
           correct_sentence = ' '+ sentence

        words +=correct_sentence.count(' ')  

        # The largest word 
        cheking_word = reduce(lambda x,y: x if len(x)>len(y) else y ,correct_sentence.split(' '))
        if len(cheking_word) >= len(largest_word):
            largest_word = cheking_word

    data['largest_word'] = largest_word
    data['total_words'] = words

    return data

# Tests
print(text_analyzer('hola como estas.Esto es una oracion'))
print(text_analyzer('hola como estas. Esto es una oracion'))
print(text_analyzer('  hola jejejejeje como estas. Esto es una oracion'))
print(text_analyzer('  hola csadfsdfsoomooooolalaallla estas.    Esto es una oracion    '))
