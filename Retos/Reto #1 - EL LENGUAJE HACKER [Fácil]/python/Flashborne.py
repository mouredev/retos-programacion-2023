entrada = input("Ingresa un texto para transformarlo a lenguaje hacker: ").upper()

leet = {
    "A": "4",
    "B": "l3",
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
    "R": "l2",
    "S": "5",
    "T": "7",
    "U": "(_)",
    "V": r"\/",
    "W": r"\/\/",
    "X": "><",
    "Y": "j",
    "Z": "2",
}


resultado = ""

for i in entrada:
    resultado += leet.get(i, i)

print(resultado)