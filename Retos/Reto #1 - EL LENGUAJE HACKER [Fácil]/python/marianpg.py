def leet(text):
    # Creamos un diccionario con las transformaciones del lenguaje "leet"
    leet_dict = {
    "a" : "4",
    "b" : "I3",
    "c" : "[",
    "d" : ")",
    "e" : "3",
    "f" : "|=",
    "g" : "&",
    "h" : "#",
    "i" : "1",
    "j" : ",_|",
    "k" : ">|",
    "l" : "1",
    "m" : " /\\/\\",
    "n" : "^/",
    "o" : "0",
    "p" : "|*",
    "q" : "(_,)",
    "r" : "I2",
    "s" : "5",
    "t" : "7",
    "u" : "(_)",
    "v" : "\\/",
    "w" : "\\/\\/",
    "x" : "><",
    "y" : "j",
    "z" : "2",
    "0" : "o",
    "1" : "L",
    "2" : "R",
    "3" : "E",
    "4" : "A",
    "5" : "S",
    "6" : "b",
    "7" : "T",
    "8" : "B",
    "9" : "g"
}

    # lista vacia
    leet_text = []

    for char in text:
    
        if char in leet_dict:
            leet_text.append(leet_dict[char])
    
        else:
            leet_text.append(char)

    
    return ''.join(leet_text)

# Testeamos
print("               _ _               _              _            ") 
print("  ___ ___   __| (_) __ _  ___   | |    ___  ___| |_          ") 
print(" / __/ _ \ / _` | |/ _` |/ _ \  | |   / _ \/ _ \ __|         ") 
print("| (_| (_) | (_| | | (_| | (_) | | |__|  __/  __/ |_          ") 
print(" \___\___/ \__,_|_|\__, |\___/  |_____\___|\___|\__|         ") 
print("                   |___/                                     ")



print(leet('Hello world!')) 
print(leet("Hola Mundo!"))
