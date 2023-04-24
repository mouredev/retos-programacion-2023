"""
 * Escribe un programa que reciba un texto y transforme lenguaje natural a
 * "lenguaje hacker" (conocido realmente como "leet" o "1337"). Este lenguaje
 *  se caracteriza por sustituir caracteres alfanuméricos.
 * - Utiliza esta tabla (https://www.gamehouse.com/blog/leet-speak-cheat-sheet/) 
 *   con el alfabeto y los números en "leet".
 *   (Usa la primera opción de cada transformación. Por ejemplo "4" para la "a")
"""

# Diccionario que contiene las traducciones por cada letra.

dict = {
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
    "k":  ">|",
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
}

#En función de la letra que le llegue la traducirá si está en el diccionario o la dejará igual si no está. 
#Todo esto partiendo de una variable "palabra" vacía.
def traducir(a):
    palabra = ""
    for i in range(len(a)):
        if (a[i] in dict) == True:
            palabra = palabra + dict[a[i]]
        else:
            palabra = palabra + a[i]

    print(f"la traducción es: {palabra}")

traducir(input("introduce un texto para traducir: ").lower())
