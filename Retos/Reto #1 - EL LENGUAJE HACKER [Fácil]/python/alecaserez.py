leet = {
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
    "M": "[V]",
    "N": "^/",
    "O": "0",
    "P": "|*",
    "Q": "(_,)",
    "R": "I2",
    "S": "5",
    "T": "7",
    "U": "(_)",
    "V": "\/",
    "W": "\/\/",
    "X": "><",
    "Y": "j",
    "Z": "2",
}

def translate(word):
    for k in word:
        if k.upper() in leet:
            word = word.replace(k, leet[k.upper()])
        
    print(word)


translate("hello world")