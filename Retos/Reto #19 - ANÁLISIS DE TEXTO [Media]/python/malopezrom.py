# /*
# * Crea un programa que analice texto y obtenga:
#     * - Número total de palabras.
# * - Longitud media de las palabras.
# * - Número de oraciones del texto(cada vez que aparecen un punto).
# * - Encuentre la palabra más larga.
# *
# * Todo esto utilizando un único bucle.
# */

import re

# /**
# * Función que analiza un texto y obtiene:
#  * - Número total de palabras.
#  * - Longitud media de las palabras.
#  * - Número de oraciones del texto(cada vez que aparecen un punto).
#  * - Palabra más larga.
#  */

def analyzeText(text):
    wordsRegex = re.compile(r'\b\w+\b', re.UNICODE)
    sentenceRegex = re.compile(r'\b\w+\.', re.UNICODE)
    words = text.replace("\n", " ").split(" ")
    sentences = 0
    longestWord = ""
    length = 0
    size = 0

    for word in words:
        if wordsRegex.match(word):
            size += 1
            if sentenceRegex.match(word):
                sentences += 1
        length += len(word)
        if len(word) > len(longestWord):
            longestWord = word

    averageLength = length // size

    print(f"Total de palabras: {size}")
    print(f"Longitud media: {averageLength}")
    print(f"Numero de frases: {sentences}")
    print(f"Palabra mas larga: {longestWord}({len(longestWord)})")


analyzeText("""
la luna asoma: federico garcía lorca
                           cuando sale la luna
                           se pierden las campanas
                           y aparecen las sendas
                           impenetrables.
                           cuando sale la luna,
                           el mar cubre la tierra
                          y el corazón se siente
                           isla en el infinito.
                           nadie come naranjas
                           bajo la luna llena.
                           es preciso comer
                           fruta verde y helada.
                           cuando sale la luna
                           de cien rostros iguales,
                           la moneda de plata
                           solloza en el bolsillo.
""")