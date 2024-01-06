diccionario_hacker = {
     "A": "4",
     "B": "I3",
     "C": "[",
     "D": ")",
     "E": "3",
     "F": "|=",
     "G": "&",
     "H": "#",
     "I": "1",
     "J": ",_|",
     "K": ">|",
     "L": "1",
     "M": "/\\/\\",
     "N": "^/",
     "O": "0",
     "P": "|*",
     "Q": "(_,)",
     "R": "I2",
     "S": "5",
     "T": "7",
     "U": "(_)",
     "V": "\\/",
     "W": "\\/\\/",
     "X": "><",
     "Y": "j",
     "Z": "2",
     "1":"L",
     "2":"R",
     "3":"E",
     "4":"A",
     "5":"S",
     "6":"b",
     "7":"T",
     "8":"B",
     "9":"g",
     "0":"o"
    }


def encriptacion(palabra):

    palabra = palabra.upper()
    lista_caracteres = list(palabra)
    palabra_hacker = ""

    for caracter in lista_caracteres:
        if caracter in diccionario_hacker.keys():
            palabra_hacker = palabra_hacker + diccionario_hacker[caracter]
        else:
            palabra_hacker = palabra_hacker + caracter
    return palabra_hacker


palabra = input("Ingrese un texto: ")

print(encriptacion(palabra))
