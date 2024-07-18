# Escribe un programa que reciba un texto y transforme lenguaje natural a
# "lenguaje hacker" (conocido realmente como "leet" o "1337"). Este lenguaje
# se caracteriza por sustituir caracteres alfanuméricos.
# - Utiliza esta tabla (https://www.gamehouse.com/blog/leet-speak-cheat-sheet/)
# con el alfabeto y los números en "leet".
# (Usa la primera opción de cada transformación. Por ejemplo "4" para la "a")

def leet_transform(text):
    alphabet_dict = {'a': '4', 'b': 'I3', 'c': '[', 'd': ')', 'e': '3', 'f': '|=',
                     'g': '&', 'h': '#', 'i': '1', 'j': ',_|', 'k': '>|', 'l': '1',
                     'm': r'/\/\\', 'n': '^/', 'o': '0', 'p': '|*', 'q': '(_,)',
                     'r': 'I2', 's': '5', 't': '7', 'u': '(_)', 'v': r'\/',
                     'w': r'\/\/', 'x': '><', 'y': 'j', 'z': '2'}

    number_dict = {"1": 'L', "2": 'R', "3": 'E', "4": 'A', "5": 'S', "6": 'b', "7": 'T', "8": 'B', "9": 'g', "0": 'o'}

    leet_sentence = ""

    for letter in text:
        if letter in alphabet_dict.keys():
            leet_sentence += alphabet_dict[letter]
        elif letter in number_dict.keys():
            leet_sentence += number_dict[letter]
        else:
            leet_sentence += letter

    return leet_sentence


natural_sentence = input("Frase en lenguaje natural: ").lower()
leet = leet_transform(natural_sentence)
print(f"Frase en lenguaje 'leet': {leet}")

