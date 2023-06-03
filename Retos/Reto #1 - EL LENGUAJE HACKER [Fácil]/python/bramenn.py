hacker_dictionary = {
    "a":"4",
    "b":"I3",
    "c":"[",
    "d":")",
    "e":"3",
    "f":"|=",
    "g":"&",
    "h":"#",
    "i":"1",
    "j":",_|",
    "k":">|",
    "l":"1",
    "m":"/\\/\\",
    "n":"^/",
    "o":"0",
    "p":"|*",
    "q":"(_,)",
    "r":"I2",
    "s":"5",
    "t":"7",
    "u":"(_)",
    "v":"\\/",
    "w":"\\/\\/",
    "x":"><",
    "y":"j",
    "z":"2",
    " ":" ",
}

def main(text: str):
    return "".join(letter.replace(letter, hacker_dictionary.get(letter, letter)) for letter in text.lower())


print(main("leet"))