'''

Escribe un programa que reciba un texto y transforme lenguaje natural a "lenguaje hacker" (conocido realmente como "leet" o "1337"). Este lenguaje se caracteriza por sustituir caracteres alfanuméricos.
  - Utiliza esta tabla (https://www.gamehouse.com/blog/leet-speak-cheat-sheet/) 
con el alfabeto y los números en "leet".
(Usa la primera opción de cada transformación. Por ejemplo "4" para la "a")
 
'''


def leet_speak(text):
    leet_dict = {
        'a': '4',
        'b': '8',
        'c': '(',
        'd': '[)',
        'e': '3',
        'f': '|=',
        'g': '6',
        'h': '#',
        'i': '!',
        'j': ']',
        'k': '|<',
        'l': '1',
        'm': '|\/|',
        'n': '|\|',
        'o': '0',
        'p': '|*',
        'q': '9',
        'r': '|2',
        's': '5',
        't': '7',
        'u': '|_|',
        'v': '\/',
        'w': '\/\/',
        'x': '><',
        'y': '`/',
        'z': '2'
    }

    leet_text = ''
    for char in text:
        leet_text += leet_dict.get(char.lower(), char)
    return leet_text


texto = input("Ingrese el texto a transformar a lenguaje hacker (leet): ")
texto_en_leet = leet_speak(texto)
print("Texto en lenguaje hacker (leet):", texto_en_leet)
