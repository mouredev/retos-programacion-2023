#Definiendo lenguaje leet en diccionario
leet = {
    "a":"4",
    "b":"I3",
    "c":"[",
    "d":")",
    "e":"3",
    "f":"|=",
    "g":"&",
    "h":"#",
    "i":"1",
    "j":",_|",
    "k":">|",
    "l":"1",
    "m":"/\\/\\",
    "n":"^/",
    "o":"0",
    "p":"|*",
    "q":"(_,)",
    "r":"I2",
    "s":"5",
    "t":"7",
    "u":"(_)",
    "v":"\/",
    "w":"\/\/",
    "x":"><",
    "y":"j",
    "z":"2",
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
    ",":",",
    ".":".",
    ";":";",
    "-":"-",
    "_":"_",
    ":":":",
    }

#Funcion para convertir caracteres a leet
def convertir_leet(char):
    x = leet.get(char)
    return x

#Input de texto
print("Introduzca una palabra o texto:")
text = input().lower().split()

leet_word = list()
leet_text = list()

for word in text: #Recorriendo cada palabra
    for char in word: #Recorriendo cada caracter en palabra
        leet_word.append(convertir_leet(char)) #Convirtiendo e insertando caracter leet en lista
    leet_text.append("".join(leet_word)) #Recuperando palabra convertida
    leet_word.clear() #Limpiando lista para próxima palabra
        
#Devolviendo traducción
print("La traduccion es:")
print(" ".join(leet_text))
    




