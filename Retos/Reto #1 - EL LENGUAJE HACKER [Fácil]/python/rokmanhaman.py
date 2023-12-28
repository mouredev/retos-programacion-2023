text = input("ingrese un texto: ")

out = []

for t in text:
    if t == "a":
        t = "4"
    elif t == "b":
        t = "I3"
    elif t == "c":
        t = "["
    elif t == "d":
        t = ")"
    elif t == "e":
        t = "3"
    elif t == "f":
        t = "|="
    elif t == "g":
        t = "&"
    elif t == "h":
        t = "#"
    elif t == "i":
        t = "1"
    elif t == "j":
        t = ",_|"
    elif t == "k":
        t = ">|"
    elif t == "l":
        t = "1"
    elif t == "m":
        t = 'm'
    elif t == "n":
        t = "^/"
    elif t == "o":
        t = "0"
    elif t == "p":
        t = "|*"
    elif t == "q":
        t = "(_,)"
    elif t == "r":
        t = "I2"
    elif t == "s":
        t = "5"
    elif t == "t":
        t = "7"
    elif t == "u":
        t = "(_)"
    elif t == "v":
        t = "\/"
    elif t == "w":
        t = "\/\/"
    elif t == "x":
        t = "><"
    elif t == "y":
        t = "j"
    elif t == "z":
        t = "2"
    out.append(t)

print(''.join(out))