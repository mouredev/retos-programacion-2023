simple_word = input("¿Cual es la palbra a transformar?")

print(f"Simple word: {simple_word}")
leet_language = {
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
    "m": "'/\/\'",
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
    "z": "2"
}

simple_word = simple_word.lower()
leet_word = ""
for position in range(len(simple_word)):
    leet_word += leet_language[simple_word[position]]

print(f"Leet word: {leet_word}")
