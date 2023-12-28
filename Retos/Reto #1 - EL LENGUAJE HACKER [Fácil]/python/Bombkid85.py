def leet(text):

    leet_alphabet = {"a": "4", "b": "I3", "c": "[", "d": ")", "e": "3", "f": "|=", "g": "&", "h": "#", "i": "1", "j": ",_|", "k": ">|",
                "l": "1", "m": "/\/\\", "n": "^/", "o": "0", "p": "|*", "q": "(_,)", "r": "|2", "s": "5", "t": "7", "u": "(_)",
                "v": "\/", "w": "\/\/", "x": "><", "y": "j", "z": "2", "1": "L", "2": "R", "3": "E", "4": "A", "5": "S", "6": "b",
                "7": "T", "8": "B", "9": "g", "0": "o"
            }

    text = text.lower()

    leet_text = ""

    for char in text:
        if char in leet_alphabet:
            leet_text = leet_text + leet_alphabet[char]
        else:
            leet_text = leet_text + char

    return leet_text
    
print(leet("Hola, soy Bombkid y estamos en 2023"))
print(leet("Este es el reto 1 'EL LENGUAJE HACKER'"))
