#Ejercicio #1 - El lenguaje hacker - Python - TheMartuu 

# Escribe un programa que reciba un texto y transforme lenguaje natural a
# -"lenguaje hacker" (conocido realmente como "leet" o "1337"). Este lenguaje
# -  se caracteriza por sustituir caracteres alfanuméricos.
# - Utiliza esta tabla (https://www.gamehouse.com/blog/leet-speak-cheat-sheet/) 
# -con el alfabeto y los números en "leet".
# -(Usa la primera opción de cada transformación. Por ejemplo "4" para la "a")
 
alphabet = {"A": "4", "B" : "ß", "C" : "¢", "D": "[)", "E": "3", "F":"ƒ", "G":"6", "H":"|-|", "I":"|", "J":"._]","K":"|<", "L":"£", "M":"|\/|", "N":"И", "O":"0", "P":"|o", "Q":"()_", "R":"Я", "S": "$", "T":"7", "U":"µ", "V":"\/", "W":"VV","X":"×","Y":"¥", "Z":"7_", "0":"o", "1":"I", "2":"Z", "3": "E", "4": "A", "5": "S", "6":"G", "7": "T", "8":"B", "9":"g"," ": " " }

normalText = str(input("Ingrese la frase: "))

leetText = ' '
for i in normalText.upper(): 
    if i in alphabet:
        leetText += alphabet[i] 
    else:
        leetText += i

print(leetText)