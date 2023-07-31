# ```
# /*
#  * Escribe un programa que reciba un texto y transforme lenguaje natural a
#  * "lenguaje hacker" (conocido realmente como "leet" o "1337"). Este lenguaje
#  *  se caracteriza por sustituir caracteres alfanuméricos.
#  * - Utiliza esta tabla (https://www.gamehouse.com/blog/leet-speak-cheat-sheet/) 
#  *   con el alfabeto y los números en "leet".
#  *   (Usa la primera opción de cada transformación. Por ejemplo "4" para la "a")
#  */
# ```

vocab = {
    "a": "4",
    "b": "13",
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
    "m": "",
    "n": "^/",
    "o": "0",
    "p": "|*",
    "q": "(_,)",
    "r": "l2",
    "s": "5",
    "t": "7",
    "u": "(_)",
    "v": "\/",
    "w": "\\/\\/",
    "x": "><",
    "y": "j",
    "z": "2"
}

def leet_translate(input: str) -> str:
    palabras = list(input.split())
    palabras_traducidas = []
    for palabra in palabras:
        transformar = lambda x: vocab[x]
        palabra_leet = ('').join(list(map(transformar, palabra)))
        palabras_traducidas.append(palabra_leet)
    
    return (" ").join(palabras_traducidas)

print(leet_translate(input("Introduce texto: ")))