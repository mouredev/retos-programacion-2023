import random

WORDS = [
    'murmullo', 'camino', 'herrero', 'bandera', 'inteligente', 'ciudad', 'alborto',
    'montaña', 'pintura', 'ventana', 'maremoto', 'floristeria', 'cancion', 'sombrero',
    'espejo', 'delfin', 'caballo', 'guitarra', 'almohada', 'pasillo', 'zapato',
    'libreria', 'bosque', 'oceano', 'mensaje', 'transistor', 'cuberteria', 'escudriñar'
]

class Game():
    def __init__(self):
        self.__WORDS__ = WORDS
        self.__lifes__ = 5
        self.__run__ = True
        print(f'Comienzas el juego con {self.__lifes__} vidas.')

    def __choiceWord__(self):
        '''
            Elige una palabra aleatoria de la lista de palabras posibles
            Crea una lista con la palabra seleccionada completa y la oculta
        '''
        word_selected = random.choice(self.__WORDS__)
        self.__WORDS__.remove(word_selected)
        word_selected = [ch for ch in word_selected]
        self.__word__ = word_selected[:]
        self.__hideWord__(word_selected)
    
    def __hideWord__(self, word: list):
        '''
            Oculta un máximo de un 60% de caracteres de la palabra seleccionada
            Crea una lista con la relación de letras ofuscadas
        '''
        length = len(self.__word__)
        n_hide = int(round(length * 0.6, 0))
        positions = random.choices(range(length), k=n_hide)
        
        self.__letters_hide__ = []
        for pos in positions:
            word[pos] = '_'
            self.__letters_hide__.append(self.__word__[pos])

        self.__hide_word__ = word
    
    def __question__(self):
        # Pregunta una letra y comprueba si es de las ocultas
        print(''.join(self.__hide_word__))
        ch = input('Introduce una letra: ')
        self.__checkLetter__(ch)
    
    def __checkLetter__(self, letter: str):
        '''
            Verifica que la letra indicada se encuentra entre las ocultas
            Si es así, actualiza los datos y muestra el acierto o la victoria
            Si no es así, informa del fallo, resta una vida y comprueba si se ha perdido
        '''
        if letter in self.__letters_hide__:
            print('¡Genial! Acertaste.\n')
            self.__updateWord__(letter)
            
            if self.__letters_hide__ == []:
                print('Enhorabuena, ¡has ganado loco!.')
                self.__run__ = False

        else:
            self.__lifes__ -= 1
            if self.__lifes__ > 0:
                print(f'Has fallado mandril, te quedan {self.__lifes__} vidas.\n')
            else:
                print('Has perdido colega, tendrás más suerte la próxima.')
                self.__run__ = False
    
    def __updateWord__(self, letter: str):
        '''
            Actualiza la lista ofuscada con la letra encontrada
            Elimina el caracter de la relación de letras ocultas
        '''
        for pos, ch in enumerate(self.__word__):
            if letter == ch:
                self.__hide_word__[pos] = letter
        
        while letter in self.__letters_hide__:
            self.__letters_hide__.remove(letter)

    def run(self):
        # Elige una palabra e inicia el juego
        self.__choiceWord__()
        while self.__run__:
            self.__question__()

if __name__ == '__main__':
    gm = Game()
    gm.run()
