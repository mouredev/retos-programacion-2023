"""/*
 * Escribe un programa que reciba un texto y transforme lenguaje natural a
 * "lenguaje hacker" (conocido realmente como "leet" o "1337"). Este lenguaje
 *  se caracteriza por sustituir caracteres alfanuméricos.
 * - Utiliza esta tabla (https://www.gamehouse.com/blog/leet-speak-cheat-sheet/) 
 *   con el alfabeto y los números en "leet".
 *   (Usa la primera opción de cada transformación. Por ejemplo "4" para la "a")
 */"""
def transform(word):
    dictionary = {
        'a': '4', 'b': '|3', 'c': '[', 'd': ')', 'e': '3', 'f': '|=', 'g': '&', 'h': '#',
        'i': '1', 'j': '_|', 'k': '|<', 'l': '1', 'm': '/\\/\\', 'n': '^/', 'o': '0',
        'p': '|*', 'q': '(_,)', 'r': '|2', 's': '5', 't': '7', 'u': '|_|', 'v': '\\/',
        'w': '\\/\\/', 'x': '><', 'y': '`/', 'z': '2', '1': 'L', '2': 'R', '3': 'E',
        '4': 'A', '5': 'S', '6': 'b', '7': 'T', '8': 'B', '9': 'g', '0': 'o'
    }

    leet_word = ''.join(dictionary.get(char, char) for char in word.lower())
    return leet_word

print(transform('abc'))