language_hacker = {
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
    "m": "/\/|",
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
    " ": " "
}

phrase = input("Ingresa tu mensaje: ")
phrase_hacker = ""

for letter in phrase:
    phrase_hacker += f"{language_hacker[letter.lower()]}"

print(phrase_hacker)