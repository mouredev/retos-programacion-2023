'''
* Escribe un programa que reciba un texto y transforme lenguaje natural a
* "lenguaje hacker" (conocido realmente como "leet" o "1337"). Este lenguaje
* se caracteriza por sustituir caracteres alfanuméricos.
* Utiliza esta tabla (https://www.gamehouse.com/blog/leet-speak-cheat-sheet/)
* con el alfabeto y los números en "leet".
* (Usa la primera opción de cada transformación. Por ejemplo "4" para la "a")
'''
import random


def lenguaje():
    texto = input("Escribe el texto a transformar: ")
    texto.lower()
    caracteres = []
    for el in texto:
        if el == "a":
            el = random.choice(["4", "@", "^", "/\\"])
        elif el == "b":
            el = random.choice(["8", "I3", "j3", "ß"])
        elif el == "c":
            el = random.choice(["<", "©", "(", "¢"])
        elif el == "d":
            el = random.choice(["I>", "[)", ")", "|]"])
        elif el == "e":
            el = random.choice(["3", "€", "£", "[-"])
        elif el == "f":
            el = random.choice(["ƒ", "/=", "|="])
        elif el == "g":
            el = random.choice(["9", "6", "&"])
        elif el == "h":
            el = random.choice(["#", "}{", "]-[", ")-("])
        elif el == "i":
            el = random.choice(["1", "|", "!", "]["])
        elif el == "j":
            el = random.choice(["_|", "]", ";", "_]"])
        elif el == "k":
            el = random.choice(["|<", "/<", "1<", "|["])
        elif el == "l":
            el = random.choice(["7", "|_", "1_"])
        elif el == "m":
            el = random.choice(["µ", "^^", "(v)", "|V|"])
        elif el == "n":
            el = random.choice(["|\\|", "/\\/", "/V", "ท"])
        elif el == "o":
            el = random.choice(["0", "Q", "()", "[]"])
        elif el == "p":
            el = random.choice(["|*", "/*", "|o", "|º"])
        elif el == "q":
            el = random.choice(["()_", "0_", "¶"])
        elif el == "r":
            el = random.choice(["®", "Я", "lz"])
        elif el == "s":
            el = random.choice(["5", "z", "§", "$"])
        elif el == "t":
            el = random.choice(["+", "-|-", "†", "-|-"])
        elif el == "u":
            el = random.choice(["(_)", "|_|", "]_["])
        elif el == "v":
            el = random.choice(["\\/", "|/", "\\|"])
        elif el == "w":
            el = random.choice(["\\/\\/", "\\N", "\\X/"])
        elif el == "x":
            el = random.choice(["><", "Ж"])
        elif el == "y":
            el = random.choice(["'/", "¥", "Ч"])
        elif el == "z":
            el = random.choice(["2", "-/_"])
        caracteres.append(el)
    convert = "".join(caracteres)
    print(convert)
    print(type(convert))


lenguaje()
