# lenguaje Hacker

def leet_hacker():
    palabra = input("Ingrese la palabra a traducir: \n")

    for i in range(len(palabra)):

        if palabra[i] == "a":
            palabra = palabra.replace("a", "4")
        elif palabra[i] == "b":
            palabra = palabra.replace("b", "I3")
        elif palabra[i] == "c":
            palabra = palabra.replace("c", "[")
        elif palabra[i] == "d":
            palabra = palabra.replace("d", ")")
        elif palabra[i] == "e":
            palabra = palabra.replace("e", "3")
        elif palabra[i] == "f":
            palabra = palabra.replace("f", "|=")
        elif palabra[i] == "g":
            palabra = palabra.replace("g", "&")
        elif palabra[i] == "h":
            palabra = palabra.replace("h", "#")
        elif palabra[i] == "i":
            palabra = palabra.replace("i", "1")
        elif palabra[i] == "j":
            palabra = palabra.replace("j", ",_|")
        elif palabra[i] == "k":
            palabra = palabra.replace("k",">|")
        elif palabra[i] == "l":
            palabra = palabra.replace("l","1")
        elif palabra[i] == "m":
            palabra = palabra.replace("m","/\/\.") #Si pongo la ultima barra invertida, lo toma como clausula de escape
        elif palabra[i] == "n":
            palabra = palabra.replace("n","^/")
        elif palabra[i] == "o":
            palabra = palabra.replace("o","0")
        elif palabra[i] == "p":
            palabra = palabra.replace("p","|*") #
        elif palabra[i] == "q":
            palabra = palabra.replace("q","(_,)")
        elif palabra[i] == "r":
            palabra = palabra.replace("r","l2")
        elif palabra[i] == "s":
            palabra = palabra.replace("s", "5")
        elif palabra[i] == "t":
            palabra = palabra.replace("t","7")
        elif palabra[i] == "u":
            palabra = palabra.replace("u","(_)")
        elif palabra[i] == "v":
            palabra = palabra.replace("v","\/")
        elif palabra[i] == "w":
            palabra = palabra.replace("w","\/\/")
        elif palabra[i] == "x":
            palabra = palabra.replace("x","><")
        elif palabra[i] == "y":
            palabra = palabra.replace("y","j")
        elif palabra[i] == "z":
            palabra = palabra.replace("z","2")
        else:
            print("Unicamente se traducen letras...")
    print(palabra)

leet_hacker()