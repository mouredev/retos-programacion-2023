"""
 * Escribe un programa que reciba un texto y transforme lenguaje natural a
 * "lenguaje hacker" (conocido realmente como "leet" o "1337"). Este lenguaje
 *  se caracteriza por sustituir caracteres alfanuméricos.
 * - Utiliza esta tabla (https://www.gamehouse.com/blog/leet-speak-cheat-sheet/) 
 *   con el alfabeto y los números en "leet".
 *   (Usa la primera opción de cada transformación. Por ejemplo "4" para la "a")
 *
 * Ejercicio hecho por PabloGradolph.
 * Fecha: 03/01/2023
"""

# Función que acepta un caracter y retorna su traducción en lenguaje hacker.
def lenguaje_hacker(caracter):
    leet_alphabet = {
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
        "1": "L",
        "2": "R",
        "3": "E",
        "4": "A",
        "5": "S",
        "6": "b",
        "7": "T",
        "8": "B",
        "9": "g",
    }

    if caracter in leet_alphabet:
        return leet_alphabet[caracter]
    else:
        return caracter

# Función main donde pedimos el texto y lo vamos traduciendo con ayuda de la función anterior.
def main():
    print("Introduzca un texto para traducir a lenguaje hacker: ")
    text = input().lower()
    new_text = ""

    for i in text:
        new_text = new_text + lenguaje_hacker(i)

    print("El texto traducido a lenguaje hacker es:")
    print(new_text)

# Ejecutamos.
if __name__ == "__main__":
    main()