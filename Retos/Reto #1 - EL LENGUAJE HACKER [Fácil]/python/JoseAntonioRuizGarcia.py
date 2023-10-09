'''
* Escribe un programa que reciba un texto y transforme lenguaje natural a
* "lenguaje hacker" (conocido realmente como "leet" o "1337"). Este lenguaje
*  se caracteriza por sustituir caracteres alfanuméricos.
* - Utiliza esta tabla (https://www.gamehouse.com/blog/leet-speak-cheat-sheet/) 
*   con el alfabeto y los números en "leet".
*   (Usa la primera opción de cada transformación. Por ejemplo "4" para la "a")
'''

leet_vocabulary = {
    "A": "4",
    "Á": "4",
    "B": "I3",
    "C": "[",
    "D": ")",
    "E": "3",
    "É": "3",
    "F": "|=",
    "G": "&",
    "H": "#",
    "I": "1",
    "Í": "1",
    "J": ",_|",
    "K": ">|",
    "L": "1",
    "M": "/\/\\",
    "N": " ^/",
    "O": "0",
    "Ó": "0",
    "P": "|*",
    "Q": "(_,)",
    "R": "I2",
    "S": "5",
    "T": "7",
    "U": "(_)",
    "Ú": "(_)",
    "V": "\/",
    "W": "\/\/",
    "X": "><",
    "Y": "j",
    "Z": "2",
    "0": "o",
    "1": "L",
    "2": "R",
    "3": "E",
    "4": "A",
    "5": "S",
    "6": "b",
    "7": "T",
    "8": "B",
    "9": "g",
    " ": " "
}

def convertLeet(text_original: str) -> None:
    text_leet = [leet_vocabulary.get(ch, ch) for ch in text_original]
    text_leet = ''.join(text_leet)

    print(f'Conversión: {text_leet}')

if __name__ == '__main__':
    text = input('Introduce un texto:\n')
    convertLeet(text.upper())

    