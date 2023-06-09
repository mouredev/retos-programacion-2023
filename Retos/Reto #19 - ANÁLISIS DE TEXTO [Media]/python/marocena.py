''''
/*
 * Crea un programa que analice texto y obtenga:
 * - Número total de palabras.
 * - Longitud media de las palabras.
 * - Número de oraciones del texto (cada vez que aparecen un punto).
 * - Encuentre la palabra más larga.
 *
 * Todo esto utilizando un único bucle.
 */
'''

def get_word_number(text: list) -> int:
    
    return text.split().__len__()

def get_word_average_length(text: list) -> float:

    words_len = []
    for word in text:
        words_len.append(word.__len__())
    
    return '{:.2f}'.format(sum(words_len)/words_len.__len__())

def get_sentence_number(text: str) -> int:

    num_sentences = 0
    for char in text:
        if char == ".":
            num_sentences += 1
    
    return num_sentences

def get_longest_word(text: list) -> str:

    longest_word = ""
    for word in text:
        if word[-1] == "." or word[-1] == ",": #omitting other puntuation marks like: ", :, !, ?, etc.
            word = word[:-1]
  
        if word.__len__() > longest_word.__len__():
            longest_word = word
        else:
            continue
    
    return longest_word

text = '''
    En un lugar de la Mancha, de cuyo nombre no quiero acordarme,
    no ha mucho tiempo que vivía un hidalgo de los de lanza en astillero,
    adarga antigua, rocín flaco y galgo corredor. Una olla de algo más vaca que carnero,
    salpicón las más noches, duelos y quebrantos los sábados, lantejas los viernes,
    algún palomino de añadidura los domingos, consumían las tres partes de su hacienda.
'''

print(
    "Número de palabras: ", get_word_number(text), "\n",
    "Longitud media de palabra: ", get_word_average_length(text.split()), "\n",
    "Número de oraciones: ", get_sentence_number(text), "\n",
    "Palabra más larga: ", get_longest_word(text.split()),
    sep = ""
    )

