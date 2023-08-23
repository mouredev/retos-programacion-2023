def traductor(texto):
    dict_1 = {
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
        "k": "|<",
        "l": "|",
        "m": "[v]",
        "n": "^/",
        "o": "0",
        "p": "?",
        "q": "9",
        "r": "2",
        "s": "5",
        "t": "7",
        "u": "(_)",
        "v": "\/",
        "w": "N/",
        "x": "><",
        "y": "\|/",
        "z": "%",
        " ":" "
    }
    resultado = ""
    for i in texto:
        resultado += dict_1[i]
    return resultado

entrada = input("El texto: ")

print(traductor(entrada))