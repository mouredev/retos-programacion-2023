
# * Escribe un programa que reciba un texto y transforme lenguaje natural a
# * "lenguaje hacker" (conocido realmente como "leet" o "1337"). Este lenguaje
# *  se caracteriza por sustituir caracteres alfanuméricos.
# * - Utiliza esta tabla(https://www.gamehouse.com/blog/leet-speak-cheat-sheet/)
# *   con el alfabeto y los números en "leet".
# *   (Usa la primera opción de cada transformación. Por ejemplo "4" para la "a")


def leetTranslator(text):

    letters = [('A', '/-\\'), ('B', '|3'), ('C', '<'), ('D', '[)'), ('E', '£'), ('F', 'ƒ'), ('G', '6'), ('H', ']-|'), ('I', '1'), ('J', ',_|'), ('K', '|{'), ('L', '|_'), ('M', '|V|'), ('N', '|\|'), ('Ñ', 'N'), ('O', '()'), ('P', '|*'), ('Q', '0¿'), ('R', '|2'), ('S', '5'), (
        'T', '7'), ('U', '(_)'), ('V', '\/'), ('W', 'V\/'), ('X', '><'), ('Y', '¥'), ('Z', '2'), ('0', 'O'), ('1', 'I'), ('2', 'Z'), ('3', 'E'), ('4', 'A'), ('5', 'S'), ('6', 'G'), ('7', 'T'), ('8', 'B'), ('9', 'P'), (" ", "  "), (",", "."), (".", ","), ("?", "P")]

    text = list(text)
    text = [letra.upper() for letra in text]

    for i in text:
        for letter, leet in letters:
            if i == letter:
                indice = text.index(i)
                text[indice] = leet

    text = ''.join(text)
    return print(text)


leetTranslator("Hello World")
leetTranslator("Hola World")
leetTranslator("Hello Mundo")
leetTranslator("Hola Mundo")
