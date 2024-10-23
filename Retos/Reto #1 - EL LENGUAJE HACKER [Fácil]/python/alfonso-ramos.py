leet_alphabet = {
    "a": "4",
    "b": "8",
    "c": "[",
    "d": ")",
    "e": "3",
    "f": "/=",
    "g": "6",
    "h": "#",
    "i": "1",
    "j": "]",
    "k": "1<",
    "l": "|",
    "m": "|v|",
    "n": "/v",
    "o": "[]",
    "p": "?",
    "q": "9",
    "r": "|9",
    "s": "$",
    "t": "/",
    "u": "(_)",
    "v": "|/",
    "w": "2u",
    "x": ")(",
    "y": "7",
    "z": "7_",
    " ": " "
}

def conversor_leet(text):
    leet_text = ''
    for i, char in enumerate(text):
        alphabet_char = text[i].lower()
        leet_char = leet_alphabet[alphabet_char]
        leet_text += leet_char
    print(leet_text)


conversor_leet('Hola mundo soy Poncho Ramos')