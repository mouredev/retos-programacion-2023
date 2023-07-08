'''
* Escribe un programa que reciba un texto y transforme lenguaje natural a
* "lenguaje hacker" (conocido realmente como "leet" o "1337"). Este lenguaje
*  se caracteriza por sustituir caracteres alfanuméricos.
* - Utiliza esta tabla(https: // www.gamehouse.com/blog/leet-speak-cheat-sheet/)
*   con el alfabeto y los números en "leet".
*   (Usa la primera opción de cada transformación. Por ejemplo "4" para la "a")
'''

leet_dir = {
    'a': '4',
    'b': 'I3',
    'c': '[',
    'd': ')',
    'e': '3',
    'f': '|=',
    'g': '&',
    'h': '#',
    'i': '1',
    'j': ',_|',
    'k': '>|',
    'l': '£',
    'm': '|\/|',
    'n': '^/',
    'o': '0',
    'p': '|*',
    'q': '(_,)',
    'r': 'I2',
    's': '5',
    't': '7',
    'u': '(_)',
    'v': '\/',
    'w': '\/\/',
    'x': '><',
    'y': 'j',
    'z': '2',
}

def lenguaje_hacker():
    text = input('Please, input your Text to convert to l33t code:\n>').lower()
    leet_text = ''

    for letter in text:
        if letter in leet_dir:
            leet_text += leet_dir[letter]
        else:
            leet_text += letter
    return print(leet_text)


lenguaje_hacker()