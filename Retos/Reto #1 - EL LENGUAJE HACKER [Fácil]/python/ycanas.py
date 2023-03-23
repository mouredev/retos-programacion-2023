def to_leet(natural):
    leet = {
        "A": "4",     "N": "^/",
        "B": "I3",    "O": "0",
        "C": "[",     "P": "|*",
        "D": ")",     "Q": "(_,)",
        "E": "3",     "R": "I2",
        "F": "|=",    "S": "5",
        "G": "&",     "T": "7",
        "H": "#",     "U": "(_)",
        "I": "1",     "V": "\/",
        "J": ",_|",   "W": "\/\/",
        "K": ">|",    "X": "><",
        "L": "1",     "Y": "j",
        "M": "/\/\\", "Z": "2"
    }

    hacker = ""

    for i in natural.upper():
        hacker += leet[i] if i in leet else i

    return hacker

print(to_leet("Hola mundo"))
