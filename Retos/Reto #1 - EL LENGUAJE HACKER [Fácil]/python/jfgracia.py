 #
 # Escribe un programa que reciba un texto y transforme lenguaje natural a
 # "lenguaje hacker" (conocido realmente como "leet" o "1337"). Este lenguaje
 #  se caracteriza por sustituir caracteres alfanuméricos.
 # - Utiliza esta tabla (https://www.gamehouse.com/blog/leet-speak-cheat-sheet/) 
 #   con el alfabeto y los números en "leet".
 #   (Usa la primera opción de cada transformación. Por ejemplo "4" para la "a")
 # 

input_text = input("Write any text: ")
hacker_text = ""

for i in range(0,len(input_text)) :
    match input_text[i] :
        case "A"|"a" :
            hacker_text += "4"
        case "B"|"b" :
            hacker_text += "13"
        case "C"|"c" :
            hacker_text += "["
        case "D"|"d" :
            hacker_text += ")"
        case "E"|"e" :
            hacker_text += "3"
        case "F"|"f" :
            hacker_text += "|="
        case "D"|"d" :
            hacker_text += ")"
        case "G"|"g" :
            hacker_text += "&"
        case "H"|"h" :
            hacker_text += "#"
        case "I"|"i" :
            hacker_text += "1"
        case "J"|"j" :
            hacker_text += ",_|"
        case "K"|"k" :
            hacker_text += ">|"
        case "L"|"l" :
            hacker_text += "1"
        case "M"|"m" :
            hacker_text += "/\\/\\"
        case "N"|"n" :
            hacker_text += "^/"
        case "O"|"o" :
            hacker_text += "0"
        case "P"|"p" :
            hacker_text += "|*"
        case "Q"|"q" :
            hacker_text += "(_,)"
        case "R"|"r" :
            hacker_text += "|2"
        case "S"|"s" :
            hacker_text += "5"
        case "T"|"t" :
            hacker_text += "7"
        case "U"|"u" :
            hacker_text += "(_)"
        case "V"|"v" :
            hacker_text += "\\/"
        case "W"|"w" :
            hacker_text += "\\/\\/"
        case "X"|"x" :
            hacker_text += "><"
        case "Y"|"y" :
            hacker_text += "j"
        case "Z"|"z" :
            hacker_text += "2"
        case "1" :
            hacker_text += "L"
        case "2" :
            hacker_text += "R"
        case "3" :
            hacker_text += "E"
        case "4" :
            hacker_text += "A"
        case "5" :
            hacker_text += "S"
        case "6" :
            hacker_text += "b"
        case "7" :
            hacker_text += "T"
        case "8" :
            hacker_text += "B"
        case "9" :
            hacker_text += "g"
        case "0" :
            hacker_text += "o"
        case _ :
            hacker_text += input_text[i]

print(hacker_text)