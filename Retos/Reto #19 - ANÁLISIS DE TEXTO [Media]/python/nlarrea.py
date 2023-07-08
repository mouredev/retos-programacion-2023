"""
 * Crea un programa que analice texto y obtenga:
 * #- Número total de palabras.
 * #- Longitud media de las palabras.
 * #- Número de oraciones del texto (cada vez que aparecen un punto).
 * #- Encuentre la palabra más larga.
 *
 * Todo esto utilizando un único bucle.
"""


def check_text(text):
    if not text: return 'You have to enter some text!'

    WORDS = text.split(" ")
    NUM_OF_WORDS = len(WORDS)

    words_info = {}
    max_length = {"word": WORDS[0], "wLength": len(WORDS[0])}
    REGEX = r"/[^A-zÀ-ú]/g"     # any character A-z including accents
    
    total_length = 0

    num_sentences = 1

    for index, word in enumerate(WORDS):
        # store the current word and its length
        words_info[index] = {
            "word": word.replace(REGEX, ''),
            "wLength": len(word.replace(REGEX, '')),
        }

        # update the largest word and its length
        if max_length["wLength"] < words_info[index]["wLength"]:
            max_length["word"] = words_info[index]["word"]
            max_length["wLength"] = words_info[index]["wLength"]
        elif max_length["wLength"] == words_info[index]["wLength"] and index != 0:
            max_length["word"] = [max_length["word"]]
            max_length["word"].append(word)

        total_length += words_info[index]["wLength"]

        # count the number of sentences
        if "." in word and index != (NUM_OF_WORDS - 1):
            num_sentences += 1

    # get the average word length
    average_length = int(total_length / NUM_OF_WORDS)

    print_result(NUM_OF_WORDS, average_length, num_sentences, max_length)


def print_result(n_words, average_length, n_sentences, max_length):
    print(f"Number of words: {n_words}")
    print(f"Average word length: {average_length}")
    print(f"Number of sentences: {n_sentences}")
    print(f"Largest word(s):\n'{max_length['word']}' ({max_length['wLength']} letters)")


text = 'Lorem ipsum dolor sit amet consectetur adipisicing elit. Non culpa impedit natus cum nobis in?'
check_text(text)