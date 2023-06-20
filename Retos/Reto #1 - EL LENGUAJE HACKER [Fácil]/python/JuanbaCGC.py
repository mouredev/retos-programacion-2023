alphabet = {
    "a": "4", "b": "I3", "c": "[", "d": ")", "e": "3", "f": "|=", "g": "&", "h": "#", "i": "1",
    "j": ",_|", "k": ">|", "l": "1", "m": "/\/\\", "n": '^/', "o": "0", "p": "|*", "q": "(_,)",
    "r": "I2", "s": "5", "t": "7", "u": "(_)", "v": "\/", "w": "\/\/", "x": "><", "y": "j", "z": "2"
}

numbers = {
    1: "L", 2: "R", 3: "E", 4: "A", 5: "S", 6: "b", 7: "T", 8: "B", 9: "g", 0: "o"
}

def translate(text):
    translation = ""
    for character in text:
        if character.isalpha():
            if character in alphabet:
                translation += alphabet[character]
            else:
                translation += character.upper()
        elif character.isdigit():
            number = int(character)
            translation += numbers[number]
        else:
            translation += character
    return translation

print("Please, introduce the text that will be translated to leet")
text = input().lower()
print(translate(text))
