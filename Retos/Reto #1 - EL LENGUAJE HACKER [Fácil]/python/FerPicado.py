# ejercicio #1 Python, Mouredev:

""" Escribe un programa que reciba un texto y transforme lenguaje natural a
"lenguaje hacker" (conocido realmente como "leet" o "1337"). 
Este lenguaje se caracteriza por sustituir caracteres alfanuméricos.
-Utiliza esta tabla (https://www.gamehouse.com/blog/leet-speak-cheat-sheet/) 
con el alfabeto y los números en "leet".
(Usa la primera opción de cada transformación. Por ejemplo "4" para la "a") """


def leet_translate(txt):

    normal_vacabulary = ''

    leet_vocabulary = {
        'a': '4', 'b': 'I3', 'c': '[', 'd': '|)', 'e': '3', 'f': '|=',
        'g': '&', 'h': '#', 'i': '1', 'j': ',_|', 'k': '>|', 'l': '1', 'm': '/\\/\\',
        'n': '^/', 'o': '0', 'p': '|*', 'q': '(_,)', 'r': 'I2', 's': '5', 't': '7',
        'u': '(_)', 'v': '\\/', 'w': 'VV', 'x': '><', 'y': 'Ч', 'z': '2'
    }

    for word in txt:
        if word in leet_vocabulary.keys():
            normal_vacabulary += leet_vocabulary[word]

        else:
            normal_vacabulary += word

    return normal_vacabulary


print(leet_translate(input("Write your message:")))
