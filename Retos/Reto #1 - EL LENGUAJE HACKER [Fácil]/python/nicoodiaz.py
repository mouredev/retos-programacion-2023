abc = {
    "A":"4",
    "B":"I3",
    "C":"[",
    "D":")",
    "E":"3",
    "F":"|=",
    "G":"&",
    "H":"#",
    "I":"1",
    "J":",_|",
    "K":">|",
    "L":"1",
    "M":"JVI",
    "N":"^/",
    "O":"0",
    "P":"|*",
    "Q":"(_,)",
    "R":"I2",
    "S":"5",
    "T":"7",
    "U":"(_)",
    "V":"|/",
    "W":"\/\/",
    "X":"><",
    "Y":"j",
    "Z":"2",
    "1":"L",
    "2":"R",
    "3":"E",
    "4":"A",
    "5":"S",
    "6":"b",
    "7":"T",
    "8":"B",
    "9":"g",
    "0":"o",
    " ":" ",
}

normal_word = input('Escribe lo que quieras transformar: ')
normal_word_M = normal_word.upper()
word_leet = ''

for i in range(len(normal_word_M)):
    speel = normal_word_M[i]
    result = speel.replace(speel, abc[speel])
    word_leet += result
    
print(f'En lenguaje leet es: ', {word_leet})