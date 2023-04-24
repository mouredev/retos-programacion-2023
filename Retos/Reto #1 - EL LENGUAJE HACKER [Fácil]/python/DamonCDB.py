texto = (input("Introduce un texto para pasar a leet: ")).lower()
texto2 =""

for letra in texto:
    if letra == "a":
        texto2 += "4"
    elif letra == "b":
        texto2 += "I3"
    elif letra == "c":
        texto2 += "["
    elif letra == "d":
        texto2 += ")"
    elif letra == "e":
        texto2 += "3"
    elif letra == "f":
        texto2 += "|="
    elif letra == "g":
        texto2 += "&"
    elif letra == "h":
        texto2 += "#"
    elif letra == "i":
        texto2 += "1"
    elif letra == "j":
        texto2 += ",_|"
    elif letra == "k":
        texto2 += ">|"
    elif letra == "l":
        texto2 += "1"
    elif letra == "m":
        texto2 += "/\/\\"
    elif letra == "n":
        texto2 += "^/"
    elif letra == "o":
        texto2 += "0"
    elif letra == "p":
        texto2 += "|*"
    elif letra == "q":
        texto2 += "(_,)"
    elif letra == "r":
        texto2 += "I2"
    elif letra == "s":
        texto2 += "5"
    elif letra == "t":
        texto2 += "7"
    elif letra == "u":
        texto2 += "(_)"
    elif letra == "v":
        texto2 += "\/"
    elif letra == "w":
        texto2 += "\/\/"
    elif letra == "x":
        texto2 += "><"
    elif letra == "y":
        texto2 += "j"
    elif letra == "z":
        texto2 += "2"
    elif letra == " ":
        texto2 += " "

print(texto2)
