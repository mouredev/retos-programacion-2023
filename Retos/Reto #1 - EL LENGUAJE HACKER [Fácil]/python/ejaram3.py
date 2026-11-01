"""LENGUAJE HACKER"""

leet_speak = {
    "a": "4",
    "b": "8",
    "c": "(",
    "d": "|)",
    "e": "3",
    "f": "|=",
    "g": "6",
    "h": "#",
    "i": "1",
    "j": "_|",
    "k": "|<",
    "l": "1",
    "m": "/\\/\\",
    "n": "|\\|",
    "o": "0",
    "p": "|*",
    "q": "0_",
    "r": "|2",
    "s": "5",
    "t": "7",
    "u": "|_|",
    "v": "\\/",
    "w": "\\/\\/",
    "x": "><",
    "y": "`/",
    "z": "2",
    "0": "o",
    "1": "l",
    "2": "z",
    "3": "e",
    "4": "a",
    "5": "s",
    "6": "g",
    "7": "t",
    "8": "b",
    "9": "g",
    " ": " ",
}

input_phrase: str = input("Ingresa la frase a traducir:\n")

translation_result = "".join(
    leet_speak[letter.lower()]
    for letter in input_phrase
    if letter.lower() in leet_speak
)

print(translation_result)
