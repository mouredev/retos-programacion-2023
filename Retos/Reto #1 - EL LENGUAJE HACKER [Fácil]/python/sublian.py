'''
* Escribe un programa que reciba un texto y transforme lenguaje natural a
 * "lenguaje hacker" (conocido realmente como "leet" o "1337"). Este lenguaje
 *  se caracteriza por sustituir caracteres alfanuméricos.
 * - Utiliza esta tabla (https://www.gamehouse.com/blog/leet-speak-cheat-sheet/) 
 *   con el alfabeto y los números en "leet".
 *   (Usa la primera opción de cada transformación. Por ejemplo "4" para la "a")

'''

def leet_language(text):
    leet_alphabet = {
        'a': '4',
        'b': '8',
        'c': '[',
        'd': ')>',
        'e': '3',
        'f': '|=',
        'g': '6',
        'h': '#',
        'i': '1',
        'j': '_|',
        'k': '|<',
        'l': '|',
        'm': '|\/|',
        'n': '|\|',
        'o': '0',
        'p': '|*',
        'q': '(,)',
        'r': 'I2',
        's': '5',
        't': '7',
        'u': '(_)',
        'v': '\/',
        'w': '\/\/',
        'x': '><',
        'y': '"/',
        'z': '2'
    }
    return "".join(leet_alphabet.get(c.lower(), c) for c in text)

if __name__ == '__main__':
    
    text=input("Please enter a text to convert to 1337: ")
    print(leet_language(text))
