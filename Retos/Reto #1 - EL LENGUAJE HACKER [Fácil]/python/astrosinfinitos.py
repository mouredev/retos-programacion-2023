# ""
# Escribe un programa que reciba un texto y transforme lenguaje natural a
# "lenguaje hacker" (conocido realmente como "leet" o "1337"). Este lenguaje
# se caracteriza por sustituir caracteres alfanuméricos.
# Utiliza esta tabla (https://www.gamehouse.com/blog/leet-speak-cheat-sheet/)
# con el alfabeto y los números en "leet".
# (Usa la primera opción de cada transformación. Por ejemplo "4" para la "a")
#

# He puesto el carácter r para que se interprete como una cadena raw y no como un salto de línea

texto = input("Introduce un texto y conviértelo a lenguaje hacker: ")


def lenguaje_hacker(texto):

    hacker = {
        "a": "4",
        "á": "4",
        "b": "I3",
        "c": "[",
        "d": ")",
        "e": "3",
        "é": "3",
        "f": "|=",
        "g": "&",
        "h": "#",
        "i": "1",
        "í": "1",
        "j": ",_|",
        "k": ">|",
        "l": r"1",
        "m": r"/\/\ ",
        "n": "^/",
        "o": "0",
        "ó": "0",
        "p": "|*",
        "q": "(_,)",
        "r": "I2",
        "s": "5",
        "t": "7",
        "u": "(_)",
        "ú": "(_)",
        "v": r"\/",
        "w": r"\/\/",
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

    texto = texto.lower()
    resultado = ""
    for letra in texto:
        resultado += hacker.get(letra, letra)
    print(resultado)
    return resultado
    texto = input("Introduce un texto y conviértelo a lenguaje hacker: ")


# Convertir el texto a lenguaje hacker y almacenarlo en una variable
texto_hacker = lenguaje_hacker(texto)

# Imprimir el texto original y el texto convertido
print("Texto normal:", texto)
print("Texto en lenguaje hacker:", texto_hacker)
