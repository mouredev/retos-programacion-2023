def transfor_language(text : str):

    language_hacker = {
        "A":"4",    "B":"I3",   "C":"[",    "D":")",
        "E":"3",    "F":"|=",   "G":"&",    "H":"#",
        "I":"1",    "J":",_|",  "K":">|",   "L":"1",
        "M":"JVI",  "N":"^/",   "O":"0",    "P":"|*",
        "Q":"(_,)", "R":"I2",   "S":"5",    "T":"7",
        "U":"(_)",  "V":"|/",   "W":"\/\/", "X":"><",
        "Y":"j",    "Z":"2",    "1":"L",    "2":"R",
        "3":"E",    "4":"A",    "5":"S",    "6":"b",
        "7":"T",    "8":"B",    "9":"g",    "0":"o",
    }
    frase = ''
    for p in range(len(text)):
        if text[p] in language_hacker:
            frase += language_hacker[text[p]]
    return(frase)

while True:
    text = str(input('Ingresa un texto: ')).upper()
    print(transfor_language(text))
