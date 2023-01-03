# Reto #1: EL "LENGUAJE HACKER

#  * Escribe un programa que reciba un texto y transforme lenguaje natural a
#  * "lenguaje hacker" (conocido realmente como "leet" o "1337"). Este lenguaje
#  *  se caracteriza por sustituir caracteres alfanuméricos.
#  * - Utiliza esta tabla (https://www.gamehouse.com/blog/leet-speak-cheat-sheet/) 
#  *   con el alfabeto y los números en "leet".
#  *   (Usa la primera opción de cada transformación. Por ejemplo "4" para la "a")

def run():

    def transformar_cadena(cadena):
        
        cadena_hacker = ""
        cadena = cadena.lower()
            
        for letra in cadena:

            if letra =="a":
                letra = "4"
                cadena_hacker=cadena_hacker+letra
            elif letra =="b":
                letra = "I3"
                cadena_hacker=cadena_hacker+letra
            elif letra =="c":
                letra = "["
                cadena_hacker=cadena_hacker+letra
            elif letra =="d":
                letra = ")"
                cadena_hacker=cadena_hacker+letra
            elif letra =="e":
                letra = "3"
                cadena_hacker=cadena_hacker+letra
            elif letra =="f":
                letra = "|="
                cadena_hacker=cadena_hacker+letra
            elif letra =="g":
                letra = "&"
                cadena_hacker=cadena_hacker+letra
            elif letra =="h":
                letra = "#"
                cadena_hacker=cadena_hacker+letra
            elif letra =="i":
                letra = "1"
                cadena_hacker=cadena_hacker+letra
            elif letra =="j":
                letra = ",_|"
                cadena_hacker=cadena_hacker+letra
            elif letra =="k":
                letra = ">|"
                cadena_hacker=cadena_hacker+letra
            elif letra =="l":
                letra = "1"
                cadena_hacker=cadena_hacker+letra
            elif letra =="m":
                letra = "JVI"
                cadena_hacker=cadena_hacker+letra
            elif letra =="n":
                letra = "^/"
                cadena_hacker=cadena_hacker+letra
            elif letra =="o":
                letra = "0"
                cadena_hacker=cadena_hacker+letra
            elif letra =="p":
                letra = "|*"
                cadena_hacker=cadena_hacker+letra
            elif letra =="q":
                letra = "(_,)"
                cadena_hacker=cadena_hacker+letra
            elif letra =="r":
                letra = "I2"
                cadena_hacker=cadena_hacker+letra
            elif letra =="s":
                letra = "5"
                cadena_hacker=cadena_hacker+letra
            elif letra =="t":
                letra = "7"
                cadena_hacker=cadena_hacker+letra
            elif letra =="u":
                letra = "(_)"
                cadena_hacker=cadena_hacker+letra
            elif letra =="v":
                letra = "|/"
                cadena_hacker=cadena_hacker+letra
            elif letra =="w":
                letra = "\/\/"
                cadena_hacker=cadena_hacker+letra
            elif letra =="x":
                letra = "><"
                cadena_hacker=cadena_hacker+letra
            elif letra =="y":
                letra = "j"
                cadena_hacker=cadena_hacker+letra
            elif letra =="z":
                letra = "2"
                cadena_hacker=cadena_hacker+letra
            elif letra =="1":
                letra = "L"
                cadena_hacker=cadena_hacker+letra
            elif letra =="2":
                letra = "R"
                cadena_hacker=cadena_hacker+letra
            elif letra =="3":
                letra = "E"
                cadena_hacker=cadena_hacker+letra
            elif letra =="4":
                letra = "A"
                cadena_hacker=cadena_hacker+letra
            elif letra =="5":
                letra = "S"
                cadena_hacker=cadena_hacker+letra
            elif letra =="6":
                letra = "b"
                cadena_hacker=cadena_hacker+letra
            elif letra =="7":
                letra = "T"
                cadena_hacker=cadena_hacker+letra
            elif letra =="8":
                letra = "B"
                cadena_hacker=cadena_hacker+letra
            elif letra =="9":
                letra = "g"
                cadena_hacker=cadena_hacker+letra
            elif letra =="0":
                letra = "o"
                cadena_hacker=cadena_hacker+letra
            else:
                letra = " "
                cadena_hacker=cadena_hacker+letra
        print(cadena_hacker)

    transformar_cadena("Hola mundo")
   
if __name__ =="__main__":
    run()