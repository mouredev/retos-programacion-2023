#!/usr/bin/env python3

def is_separator(character):
    if character == ',' or character == ';' or character == '.' or character.isspace():
        return True
    else:
        return False

def is_end_of_sentence(character):
    if character == '.':
        return True
    else:
        return False

class TextAnalyzer:
    def __init__(self):
        self.__init_data()

    def __init_data(self):
        self.longest_word = ""
        self.mean_word_length = 0
        self.sentences = 0
        self.words = 0

    def analyze(self, text):
        self.__init_data()

        word = ""
        for char in text:
            if not is_separator(char):
                word = word + char
            else:
                if word.isspace() or len(word) == 0:
                    continue
                self.words = self.words + 1
                len_word = len(word)
                self.mean_word_length = self.mean_word_length + len_word
                if len(self.longest_word) < len_word:
                    self.longest_word = word
                if is_end_of_sentence(char):
                    self.sentences = self.sentences + 1
                word = ""
        self.mean_word_length = self.mean_word_length / self.words

    def print_results(self):
        print("Longest word: " + self.longest_word)
        print("Mean word length: " + str(self.mean_word_length))
        print("Sentences: " + str(self.sentences))
        print("Words: " + str(self.words))

if __name__ == "__main__":
    # Text from: https://educaciodigital.cat/ioc-batx/moodle/mod/book/view.php?id=14232&chapterid=9527
    text = """El hombre, desde su origen, guiado por unas miras que pretenden ser prácticas, ha ido enmendando la plana a la Naturaleza y convirtiéndola en campo.
El hombre, paso a paso, ha hecho su paisaje, amoldándolo a sus exigencias. Con esto, el campo ha seguido siendo campo, pero ha dejado de ser Naturaleza. Mas, al seleccionar las plantas y animales que le son útiles, ha empobrecido la Naturaleza original, lo que equivale a decir que ha tomado una resolución precipitada porque el hombre sabe lo que le es útil hoy, pero ignora lo que le será útil mañana. Y el aceptar las especies actualmente útiles y desdeñar el resto supondría, según nos dice Faustino Cordón, sacrificar la friolera de un millón de especies animales y medio millón de especies vegetales, limitación inconcebible de un patrimonio que no podemos recrear y del que quizá dependieran los remedios para el hambre y la enfermedad de mañana.
Así las cosas, y salvo muy contadas reservas, apenas queda en el mundo Naturaleza natural. """

    print("Texto a analizar:")
    print(text)
    print("")
    print("Analisis:")
    analyzer = TextAnalyzer()
    analyzer.analyze(text)
    analyzer.print_results()
