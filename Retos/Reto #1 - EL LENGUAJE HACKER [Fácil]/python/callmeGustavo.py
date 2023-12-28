


def reto2(text):
    diccionario = {
    "a": "4", 
    "b": "I3", 
    "c": "[", 
    "d": ")", 
    "e": "3", 
    "f": "|=", 
    "g": "&", 
    "h": "#", 
    "i": "1", 
    "j": ",_|", 
    "k": ">|",
    "l": "1", 
    "m": "/\/\\", 
    "n": "^/", 
    "o": "0", 
    "p": "|*", 
    "q": "(_,)", 
    "r": "|2", 
    "s": "5", 
    "t": "7", 
    "u": "(_)",
    "v": "\/", 
    "w": "\/\/", 
    "x": "><", 
    "y": "j", 
    "z": "2", 
    "1": "L", 
    "2": "R", 
    "3": "E", 
    "4": "A", 
    "5": "S", 
    "6": "b",
    "7": "T", 
    "8": "B", 
    "9": "g", 
    "0": "o",
    " ": " "
}

    # text = input('Ingrese texto: ')



    text_translate = ''

    for letter in text:
        
        if letter in diccionario.keys():
            text_translate += diccionario[letter]

    print(text_translate)

    return text_translate



text = input("Write the text to translate: ")
reto2(text)

