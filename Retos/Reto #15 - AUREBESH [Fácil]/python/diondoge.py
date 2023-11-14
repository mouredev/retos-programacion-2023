  class Language():
    def setCharacter(self, character):
        #print(f'getEquivalent - {character.upper()}')
        self.getGramaticalRule(character);
    def setCharacterL(self, character):
        #print(f'getEquivalent - {character}')
        self.getGramaticalTranslatedRule(character);
    def getGramaticalRule(self, character):
        pass
    def getGramaticalTranslatedRule(self, character):
        pass
    def searhCharacterAlphabet(self, character):
        pass
    def searhCharactersTransaltedAlp(self, character):
        pass
    def getTranslatedText(self):
        pass

class Aurebesh (Language):
    __previousCharacter = None
    __translatedText = ''
    __alphabet_dict = {
        'A': 'Aurek', 'B': 'Besh', 'C': 'Cresh', 'CH': 'Cherek', 'D': 'Dorn', 'E': 'Esk', 'Æ': 'Enth', 'EO': 'Onith',
        'F': 'Forn', 'G': 'Grek', 'H': 'Herf', 'I': 'Isk', 'J': 'Jenth', 'K': 'Krill', 'KH': 'Krenth', 'L': 'Leth',
        'M': 'Mern', 'N': 'Nern', 'NG': 'Nen', 'O': 'Osk', 'OO': 'Orenth', 'P': 'Peth', 'Q': 'Qek', 'R': 'Resh',
        'S': 'Senth', 'SH': 'Shen', 'T': 'Trill', 'TH': 'Thesh', 'U': 'Usk', 'V': 'Vev', 'W': 'Wesk', 'X': 'Xesh',
        'Y': 'Yirt', 'Z': 'Zerek'
    }

    def searhCharacterAlphabet(self, character):
        if (character.isnumeric()):
            return character
        else:
            for k, v in self.__alphabet_dict.items():
                if (k == character.upper()):
                    return v
        return character

    def searhCharactersTransaltedAlp(self,character):
        if (character.isnumeric()):
            return character
        else:
            for k, v in self.__alphabet_dict.items():
                if (v == character):
                    return k
        return None

    def getGramaticalTranslatedRule(self, character):
        if self.__previousCharacter is None:
            self.__previousCharacter = ''
        if character != ' ' and (not character.isnumeric()):
            self.__previousCharacter = f'{self.__previousCharacter}{character}'
        else:
            self.__translatedText = self.__translatedText + character
        translatedCharacter = self.searhCharactersTransaltedAlp(self.__previousCharacter)
        if translatedCharacter is not None:
            #print(f'getGramaticalTranslatedRule - {translatedCharacter.upper()}')
            self.__translatedText = f'{self.__translatedText }{translatedCharacter}'
            self.__previousCharacter = ''

    def getGramaticalRule(self, character):
        if self.__previousCharacter is None:
            self.__previousCharacter = character
        else:
            characterTmp = f'{self.__previousCharacter}{character}'
            translatedCharacter = self.__alphabet_dict.get(characterTmp.upper())
            #print(f'translatedCharacter - {translatedCharacter}')
            if translatedCharacter is not None:
                self.__translatedText = self.__translatedText + translatedCharacter
            else:
                translatedCharacter = self.searhCharacterAlphabet(self.__previousCharacter)
                self.__translatedText = self.__translatedText + translatedCharacter
                translatedCharacter = self.searhCharacterAlphabet(character)
                self.__translatedText = self.__translatedText + translatedCharacter
            self.__previousCharacter = ''

    def getTranslatedText(self):
        if self.__previousCharacter is not None:
            translatedCharacter = self.searhCharacterAlphabet(self.__previousCharacter)
            self.__translatedText = self.__translatedText + translatedCharacter
            self.__previousCharacter = None
        translatedText = self.__translatedText
        self.__translatedText=''
        return translatedText

class Traductor ():
    def __init__(self, language: Language):
        self.language = language

    def translationText(self, text):
        text_translation = "";
        for element in text:
            self.language.setCharacter(element)
        text_translation = self.language.getTranslatedText()
        return text_translation

    def translationToTierra(self, text):
        text_translation = "";
        for element in text:
            self.language.setCharacterL(element)
        text_translation = self.language.getTranslatedText()
        return text_translation.title()

if __name__ == '__main__':
    alp = Aurebesh()
    cheat = Traductor(alp)
    inputText = "Hi Moure "
    outputText = cheat.translationText(inputText)
    print(f' texto Aurebesh =  {outputText}')
    outputText = cheat.translationToTierra(outputText)
    print(f' texto Tierra  =  {outputText}')
