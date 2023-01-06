dict_hacker_language = {
        "A" : "4",
        "B" : "13",
        "C" : "[",
        "D" : ")",
        "E" : "3",
        "F" : "|=",
        "G" : "&",
        "H" : "#",
        "I" : "1",
        "J" : ",_|",
        "K" : ">|",
        "L" : "1",
        "M" : "/\\/\\",
        "N" : "|\|",
        "O" : "0",
        "P" : "|*",
        "Q" : "(_,)",
        "R" : "12",
        "S" : "5",
        "T" : "7",
        "U" : "(_)",
        "V" : "\\/",
        "W" : "\\/\\/",
        "X" : "><",
        "Y" : "j",
        "Z" : "2",
        " " : " ",
        "1" : "L",
        "2" : "R",
        "3" : "E",
        "4" : "A",
        "5" : "S",
        "6" : "b",
        "7" : "T",
        "8" : "B",
        "9" : "g",
        "0" : "o",
}

frase = input("Ingresa tu frase a encriptar")
frase_mayusculas = frase.upper()
diccionario_convertir = list(frase_mayusculas)


for letra in diccionario_convertir:
    print(dict_hacker_language[letra], end="")
