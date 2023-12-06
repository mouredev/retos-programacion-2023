
 # Reto 1 - Zebenpixel
 # Escribe un programa que reciba un texto y transforme lenguaje natural a
 # "lenguaje hacker" (conocido realmente como "leet" o "1337"). Este lenguaje
 # se caracteriza por sustituir caracteres alfanuméricos.
 # - Utiliza esta tabla (https://www.gamehouse.com/blog/leet-speak-cheat-sheet/) 
 #   con el alfabeto y los números en "leet".
 #   (Usa la primera opción de cada transformación. Por ejemplo "4" para la "a")
 #

def change_letter(caracter):
    leet = {
        #diccionario minusculas
        "a":"4",  "b":"|3",  "c":"[", "d":")", "e":"3", "f":"|=", "g":"&", "h":"#", "i":"1",
        "j":",_|", "k":">|", "l":"1", "m":"/\\/\\", "n":"^/", "o":"0", "p":"|*", "q":"(_,)", "r":"I2",
        "s":"5", "t":"7", "u":"(_)", "v":"\\/", "w":"\\/\\/", "x":"><", "y":"j", "z":"2",
        #diccionario numeros
        "0":"o", "1":"L", "2":"R", "3":"E", "4":"A", "5":"S", "6":"b", "7":"T", "8":"B", "9":"g",
        #diccionario mayusculas
        "A":"@", "B":"8", "C":"<", "D":"1)", "E":"€", "F":"|*", "G":"6", "H":"4", "I":"|", "J":"¿", "K":"|{",
        "L":"][", "M":"^^", "N":"?", "O":"<>", "P":"|?", "Q":"(0,)", "R":"|2", "S":"§", "T":"+", "U":"µ", "V":"\|",
        "W":"uu", "X":")(", "Y":"¥", "Z":"2",}

    return leet[caracter]


def  translate_to_leet(text):
    text_in_leet = ""
   
    for character in text:
        # deja tal cual el carácter si es una ñ o es carácter acentuado
        if character == 'ñ' or character == 'á' or character == 'é' or character == 'í' or character == 'ó' or character == 'ú':
            text_in_leet +=  character
        elif character.isalnum(): # .isalnum() verifica con el método si todos los caracteres de string son alfanuméricos o no
            text_translated = change_letter(character)
            text_in_leet += text_translated
        else:
            text_in_leet += character
          
    return text_in_leet

def leetTranslator():
    text_user = input("Introduce un texto a traducir: ")
    text_translated_end = translate_to_leet(text_user)
    print(f"El texto en lenguaje hacker es:  {text_translated_end}")

leetTranslator()