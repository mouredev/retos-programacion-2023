# Reto #1: EL "LENGUAJE HACKER"
#### Dificultad: Fácil | Publicación: 02/01/23 | Corrección: 09/01/23

## Enunciado
"""
/*
 * Escribe un programa que reciba un texto y transforme lenguaje natural a
 * "lenguaje hacker" (conocido realmente como "leet" o "1337"). Este lenguaje
 *  se caracteriza por sustituir caracteres alfanuméricos.
 * - Utiliza esta tabla (https://www.gamehouse.com/blog/leet-speak-cheat-sheet/) 
 *   con el alfabeto y los números en "leet".
 *   (Usa la primera opción de cada transformación. Por ejemplo "4" para la "a")
 */
"""


def ask_text():
    return input("Text: ").lower().strip()


def transform_text_hacker(text):
    hackertext = ""
    for character in text:
        match character:
            case "a":
                hackertext = hackertext + "4"
            case "b":
                hackertext = hackertext + "|3"
            case "c":
                hackertext = hackertext + "["
            case "d":
                hackertext = hackertext + ")"
            case "e":
                hackertext = hackertext + "3"
            case "f":
                hackertext = hackertext + "|="
            case "g":
                hackertext = hackertext + "&"
            case "h":
                hackertext = hackertext + "#"
            case "i":
                hackertext = hackertext + "1"
            case "j":
                hackertext = hackertext + ",_|"
            case "k":
                hackertext = hackertext + ">|"
            case "l":
                hackertext = hackertext + "1"
            case "m":
                hackertext = hackertext + "'/\/'"
            case "n":
                hackertext = hackertext + "^/"
            case "o":
                hackertext = hackertext + "0"
            case "p":
                hackertext = hackertext + "|*"
            case "q":
                hackertext = hackertext + "(_,)"
            case "r":
                hackertext = hackertext + "l2"
            case "s":
                hackertext = hackertext + "5"
            case "t":
                hackertext = hackertext + "7"
            case "u":
                hackertext = hackertext + "(_)"
            case "v":
                hackertext = hackertext + "\/"
            case "w":
                hackertext = hackertext + "\/\/"
            case "x":
                hackertext = hackertext + "><"
            case "y":
                hackertext = hackertext + "j"
            case "z":
                hackertext = hackertext + "2"
            case "1":
                hackertext = hackertext + "L"
            case "2":
                hackertext = hackertext + "R"
            case "3":
                hackertext = hackertext + "E"
            case "4":
                hackertext = hackertext + "A"
            case "5":
                hackertext = hackertext + "S"
            case "6":
                hackertext = hackertext + "b"
            case "7":
                hackertext = hackertext + "T"
            case "8":
                hackertext = hackertext + "B"
            case "9":
                hackertext = hackertext + "g"
            case "0":
                hackertext = hackertext + "o"
            case _:
                hackertext = hackertext + character
    return hackertext


def main():
    text = ask_text()
    print(f"H4Ck3R T3><T: {transform_text_hacker(text)}")


if __name__ == "__main__":
    main()
