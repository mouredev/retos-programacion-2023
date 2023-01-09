def speakHacker(palabra):
    leetspeaker={
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
            "m": "/\\/\\",
            "n": "^/",
            "o": "0",
            "p": "|*",
            "q": "(_,)",
            "r": "12",
            "s": "$",
            "t": "7",
            "u": "|_|",
            "v": "\\/",
            "w": "\\/\\/",
            "x": "><",
            "y": "j",
            "z": "2",
        }
    palabraHacker=''
    for letra in palabra.lower():
        if letra in leetspeaker:
            palabraHacker += leetspeaker[letra]
        else:
            palabraHacker += letra
    return palabraHacker


print(speakHacker(input('Ingrese palabra a tranducir a lenguaje Hacker: ')))
