# Reto #19: Análisis de texto
# Dificultad: Media | Publicación: 11/05/23 | Corrección: 15/05/23

## Enunciado

#
# Crea un programa que analice texto y obtenga:
# - Número total de palabras.
# - Longitud media de las palabras.
# - Número de oraciones del texto (cada vez que aparecen un punto).
# - Encuentre la palabra más larga.
#
# Todo esto utilizando un único bucle.
#

class TextAnalizer:
    def __init__(self, text):
        self.text = text
        self.words_number = 0
        self.length_total = 0
        self.sentence_number = 0
        self.longest_word = ""

    def analize(self):
        for word in self.text.split():
            self.words_number += 1
            self.length_total += len(word)

            if word[-1] in ["."]:
                self.sentence_number += 1

            if len(word) > len(self.longest_word):
                self.longest_word = word

        self.average_length = self.length_total / self.words_number

    def print_results(self):
        print("Número total de palabras:", self.words_number)
        print("Longitud media de las palabras:", self.average_length)
        print("Número de oraciones:", self.sentence_number)
        print("Palabra más larga:", self.longest_word)

if __name__ == "__main__":
    text = input("Ingresa el texto a analizar: ")
    analizer = TextAnalizer(text)
    analizer.analize()
    analizer.print_results()