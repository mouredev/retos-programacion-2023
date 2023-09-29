
#  Escribe un programa que reciba un texto y transforme lenguaje natural a
#  "lenguaje hacker" (conocido realmente como "leet" o "1337"). Este lenguaje
#   se caracteriza por sustituir caracteres alfanuméricos.
#  Utiliza esta tabla (https://www.gamehouse.com/blog/leet-speak-cheat-sheet/) 
#    con el alfabeto y los números en "leet".
#   (Usa la primera opción de cada transformación. Por ejemplo "4" para la "a")

leet = {
    'a': '4',
    'b': '8',
    'c': '<',
    'd': '|)',
    'e': '3',
    'f': '|=',
    'g': '9',
    'h': '#',
    'i': '1',
    'j': '_|',
    'k': '|<',
    'l': '1',
    'm': '|\/|',
    'n': '|\|',
    'o': '0',
    'p': '|>',
    'q': '(_,)',
    'r': '|2',
    's': '5',
    't': '7',
    'u': '|_|',
    'v': '\/',
    'w': '\/\/',
    'x': '><',
    'y': '¥',
    'z': '2',
    '1': 'L',
    '2': 'Z',
    '3': 'E',
    '4': 'A',
    '5': 'S',
    '6': 'b',
    '7': 'T',
    '8': 'B',
    '9': 'g',
    '0': 'O'
}

def text_to_leet(text):
    result = ''
    for char in text.lower():
        if char in leet:
            result += leet[char]
        else:
            result += char
    return result

texto_original = input("Ingrese un texto: ")
texto_en_leet = text_to_leet(texto_original)
print("Texto transformado en leet:")
print(texto_en_leet)
