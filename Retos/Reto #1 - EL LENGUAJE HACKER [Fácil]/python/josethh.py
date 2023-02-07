
# Escribe un programa que reciba un texto y transforme lenguaje natural a
# "lenguaje hacker" (conocido realmente como "leet" o "1337"). Este lenguaje
#  se caracteriza por sustituir caracteres alfanuméricos.
# - Utiliza esta tabla (https://www.gamehouse.com/blog/leet-speak-cheat-sheet/) 
#   con el alfabeto y los números en "leet".
#   (Usa la primera opción de cada transformación. Por ejemplo "4" para la "a")
 

interpreter = {
    'a': '4',
    'b': '13', 
    'c': '[',
    'd': ')',
    'e': '3', 
    'f': '|=',
    'g': '&',
    'h': '#',
    'i': '][',
    'j': ',_|',
    'k': '>|',
    'l': '1',
    'm': 'jvi',
    'n': '/\/',
    'o': '<>',
    'p': '|*',
    'q': '<|',
    'r': '/2',
    's': '2',
    't': '+',
    'u': 'L|',
    'v': '\|',
    'w': 'vN',
    'x': 'ecks',
    'y': 'j',
    'z': '7_',
    ' ': '12',
    '1': 'L',
    '2': 'R',
    '3': 'E',
    '4': 'A',
    '5': 'S',
    '6': 'G',
    '7': 'T',
    '8': 'B',
    '9': 'g',
    '0': 'o'
}

text = 'variable que almacenará el texto encriptado'
hack_lang = ''

for item in interpreter:
    if item in text:
        hack_lang += interpreter[item]
    else: 
        continue

print(hack_lang)
