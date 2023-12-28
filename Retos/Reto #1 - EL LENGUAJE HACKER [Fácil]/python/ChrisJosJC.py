'''
 * Escribe un programa que reciba un texto y transforme lenguaje natural a
 * "lenguaje hacker" (conocido realmente como "leet" o "1337"). Este lenguaje
 *  se caracteriza por sustituir caracteres alfanuméricos.
 * - Utiliza esta tabla (https://www.gamehouse.com/blog/leet-speak-cheat-sheet/) 
 *   con el alfabeto y los números en "leet".
 *   (Usa la primera opción de cada transformación. Por ejemplo "4" para la "a")
'''


def get_leet(letra):

    letras = {
        "a": "4",
        "b": "I3",
        "c": "[",
        "d": ")",
        "e": "3",
        "f": "|=",
        "g": "&",
        "h": "#",
        "i": "1",
        "j": ",_|",
        "k": ">|",
        "l": "1",
        "m": "/\/\\",
        "n": "^/",
        "o": "0",
        "p": "|*",
        "q": "(_,)",
        "r": "I2",
        "s": "5",
        "t": "7",
        "u": "(_)",
        "v": "\/",
        "w": "\/\/",
        "x": "><",
        "y": "j",
        "z": "2",
        " ": " "
    }

    return letras[letra]


def Translate(text: str):
    letters = list(text)
    result = ""
    for letter in letters:
        result += get_leet(letter.lower())
    return result


print("Tu traductor a LEET (1337): \n")
entry = input("Ingresa el texto a traducir: ")
print(Translate(entry))
