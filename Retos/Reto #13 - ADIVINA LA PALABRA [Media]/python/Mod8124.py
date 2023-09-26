#  Crea un pequeño juego que consista en adivinar palabras en un número máximo de intentos:
#  - El juego comienza proponiendo una palabra aleatoria incompleta
#  - Por ejemplo "m_ur_d_v", y el número de intentos que le quedan
#  - El usuario puede introducir únicamente una letra o una palabra (de la misma longitud que
#  la palabra a adivinar)
#  - Si escribe una letra y acierta, se muestra esa letra en la palabra. Si falla, se resta
#  uno al número de intentos
#  - Si escribe una resolución y acierta, finaliza el juego, en caso contrario, se resta uno
#  al número de intentos
#  - Si el contador de intentos llega a 0, el jugador pierde
#  - La palabra debe ocultar de forma aleatoria letras, y nunca puede comenzar ocultando más del 60%
#  - Puedes utilizar las palabras que quieras y el número de intentos que consideres

import random

catFigure = {
           0: """
   /\_/\  (
  ( ^.^ ) _)
    \\"/  (
  ( | | )
 (__d b__) GAME OVER
           """,
        1: """
   /\_/\  (
  ( ^.^ ) _)
    \\"/  (
  ( | | )
 (__d b__) 
            """,
        2: """
   /\_/\  
  ( ^.^ ) 
    \\"/  
  ( | | )
 (__d b__)
            """,
        3: """
   /\_/\  
  ( ^.^ ) 
    \\"/  
  ( | | )
            """,
        4: """
   /\_/\  
  ( ^.^ ) 
    \\"/  
            """,
        5: """
   /\_/\  
  ( ^.^ ) 
            """,
}

words = {
    "EN":["Apple",  "Banana", "Monitor", "Lemon", "Elephant", "Flower", "Grape", "House", "Fish", "Jacket", "Rice","Lion", "Camera", "Notebook", "Orange", "Tomato", "Queen", "Rabbit", "Shirt", "Tree", "Umbrella", "Violin", "Water", "Xylophone", "Yellow", "Book", "Shoe", "Chair", "Desk", "Egg", "Goat", "Globe", "Lion", "Duck", "mouse", "Juice", "Kite", "Lamp", "Moon", "Nail", "Ocean", "berserk"],
    "ES":["Amarillo", "Bicicleta", "Casa", "Diente", "Elefante", "Flor", "Gato", "Helado", "Isla", "Jirafa", "Kilometro", "Lapiz", "Manzana", "Naranja", "Oso", "Pajaro", "Queso", "Rana", "Silla", "Tigre", "Uva", "Vaso", "Mascara", "Yate", "Zanahoria", "Arbol", "Goma", "Cama", "Ducha", "Escalera", "Fiesta", "Gafas", "Huevo", "Invierno", "Jardín", "Llave", "Maleta", "Nube", "Ojo", "Piso"]
}

msg = {
    "currentLetter":"your letter, {}",
    "lives": "you have {} lives left",
     "currentWord":"current word: "
}

def getRandomWord(lang):
    DEFAULTPERCENTAGE = 60
    word = random.choice(words[lang]).lower()
    revealWord = (DEFAULTPERCENTAGE * len(word)) // 100
    return [word, revealWord]

def getRandomIndexLetter(word, length):
    indexes = list(range(len(word)))
    random.shuffle(indexes)
    return indexes[:length]

def letsPlay():
    LIVES = 5 # lives by default xd
    chooseLang = input('Choose language: EN or ES : ')
    if chooseLang != 'EN' and chooseLang != 'ES':
        return letsPlay()
    [randomWord, AmountLetterDiscoverd] = getRandomWord(chooseLang)
    hiddenIndexes = getRandomIndexLetter(randomWord, AmountLetterDiscoverd)
    hideWord = ""

    for index, char in enumerate(randomWord):
     if index in hiddenIndexes:
        hideWord += char
     else:
        hideWord += "_"
    _letsPlay(LIVES, randomWord, hideWord)

def printRound(guess, lives, currentWord, additional=False):
    print('')
    print(msg["currentLetter"].format(guess) + (' is in the word' if additional else ' is not in the word'))
    print(msg["lives"].format(lives))
    print(msg['currentWord'] + currentWord + '\n')
    
def _letsPlay(lives, originalWord, currentWord):
    if lives == 0:
       print(msg["lives"].format(lives))
       print(catFigure[lives])
       return print('The word was', originalWord)
    if originalWord == currentWord:
       return print('YOU WIN!!, The word was', originalWord)
    guess = input('Guess a letter: ')

    if guess in originalWord:
            newWord = ""
            for i in range(len(originalWord)):
                if originalWord[i] == guess:
                    newWord += guess
                else:
                    newWord += currentWord[i]
            printRound(guess, lives, currentWord, True)
            _letsPlay(lives, originalWord, newWord)
    else:   
            printRound(guess, lives, currentWord)
            print(catFigure[lives])
            _letsPlay(lives-1, originalWord, currentWord)

letsPlay()
