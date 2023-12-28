'''
* Escribe un programa que reciba un texto y transforme lenguaje natural a
 * "lenguaje hacker" (conocido realmente como "leet" o "1337"). Este lenguaje
 *  se caracteriza por sustituir caracteres alfanuméricos.
 * - Utiliza esta tabla (https://www.gamehouse.com/blog/leet-speak-cheat-sheet/) 
 *   con el alfabeto y los números en "leet".
 *   (Usa la primera opción de cada transformación. Por ejemplo "4" para la "a")

'''

def hacker_language(text):
    leet_alphabet = {
        'a': '4',
        'b': 'I3',
        'c': '[',
        'd': ')>',
        'e': '3',
        'f': '|=',
        'g': '&',
        'h': '#',
        'i': '1',
        'j': '_|',
        'k': '>|',
        'l': '1',
        'm': '/\/\\',
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
        'z': '2'
    }
    leet_text = ''
    for char in text.lower():
        if char.isalnum():
            leet_text += leet_alphabet.get(char, char) #comprueba que la frase introducida sea alfanumérica
        else:
            leet_text += char #en el caso de que la frase introducida no sea alfanumérica porque tiene espacios en blanco o algún otro caracter se dejará tal cual ha sido introducido.
    return leet_text

frase = input("Escribe un texto para convertirlo a lenguaje hacker: ")
print(hacker_language(frase))
