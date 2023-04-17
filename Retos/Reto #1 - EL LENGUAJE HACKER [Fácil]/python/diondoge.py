class Alphabet():
    def getEquivalent(self, caracter):
        pass
class L33T(Alphabet):
    translations = {
        'a': '4', 'b': '13', 'c': '[', 'd': ')', 'e': '3', 'f': '|=', 'g': '&', 'h': '#', 'i': '1', 'j': ',_|',
        'k': '>|', 'l': '1', 'm': '/\/\\', 'n': '^/', 'o': '0', 'p': '|*', 'q': '(_,)', 'r': '12', 's': '5', 't': '7',
        'u': '(_)', 'v': '\/', 'w': '\/\/', 'x': '><', 'y': 'j', 'z': '2', '1': 'L', '2': 'R', '3': 'E', '4': 'A',
        '5': 'S', '6': 'b', ' ': 'T', '8': 'B', '9': 'g', '0': 'o'
    }
    def getEquivalent(self, caracter):
        return self.translations.get(caracter)

class Cheat ():
    def __init__(self, alphabet: Alphabet):
        self.alphabet = alphabet

    def translationText(self, text):
        text_translation = "";
        for element in text:
            element_e = self.alphabet.getEquivalent(element)
            text_translation += (element if (element_e == None) else element_e )
        return text_translation

if __name__ == '__main__':
    alp = L33T()
    cheat = Cheat(alp)
    inputText = "Hola Mundo"
    outputText = cheat.translationText(inputText)
    print(outputText)