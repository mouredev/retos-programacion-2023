"""/*
 * Escribe un programa que reciba un texto y transforme lenguaje natural a
 * "lenguaje hacker" (conocido realmente como "leet" o "1337"). Este lenguaje
 *  se caracteriza por sustituir caracteres alfanuméricos.
 * - Utiliza esta tabla (https://www.gamehouse.com/blog/leet-speak-cheat-sheet/) 
 *   con el alfabeto y los números en "leet".
 *   (Usa la primera opción de cada transformación. Por ejemplo "4" para la "a")
 */"""

LEET_ALPHABET: dict = {
    "a": "4",
    "b": "13",
    "c": "[",
    "d": ")",
    "e": "3",
    "f": "|=",
    "g": "6",
    "h": "#",
    "i": "1",
    "j": ",_|",
    "k": ">|",
    "l": "|_",
    "m": "/\\/\\",
    "n": "^/",
    "o": "0",
    "p": "|*",
    "q": "9",
    "r": "|2",
    "s": "5",
    "t": "7",
    "u": "(_)",
    "v": "\\/",
    "w": "\\/\\/",
    "x": "><",
    "y": "j",
    "z": "2",
    "1": "L",
    "2": "R",
    "3": "E",
    "4": "A",
    "5": "S",
    "6": "b",
    "7": "T",
    "8": "B",
    "9": "g",
    "0": "o",
}


def leet_conversor(text: str) -> str:
    """Return a text trasform in a leet speaking"""
    leet_text: str = ""
    for i in text:
        for key, value in LEET_ALPHABET.items():
            if i == key:
                leet_text += value
                break
    return leet_text


print(leet_conversor("savitar"))
