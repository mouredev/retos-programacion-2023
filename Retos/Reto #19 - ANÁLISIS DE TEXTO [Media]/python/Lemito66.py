'''
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

def analize_word(word: str) -> str:
    total_numbers_of_words = 0
    total_length_of_words = []
    total_sentences = 0
    longest_word = ''
    word_without_punctuation = replace_punctuation(word)
    for word_without_punctuation in word_without_punctuation.split(' '):
        total_numbers_of_words += 1
        total_length_of_words.append(len(word_without_punctuation))
        if '.' in word_without_punctuation:
            total_sentences += 1
        if len(word_without_punctuation) > len(longest_word):
            longest_word = word_without_punctuation
            
    print(total_length_of_words)
    total_length_of_words = sum(total_length_of_words) / len(total_length_of_words)
    
    return f'Número total de palabras: {total_numbers_of_words}\nLongitud media de las palabras: {total_length_of_words}\nNúmero de oraciones del texto: {total_sentences}\nPalabra más larga: {longest_word}'

def replace_punctuation(word: str) -> str:
    punctuation = ',;:¿?!()"\''
    for i in punctuation:
        word = word.replace(i, '')
    return word

print(analize_word('Hola, como estas. Mañana. nos vamos de fiesta?'))