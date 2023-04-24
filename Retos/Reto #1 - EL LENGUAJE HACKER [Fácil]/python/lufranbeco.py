# Escribe un programa que reciba un texto y transforme lenguaje natural a
# "lenguaje hacker" (conocido realmente como "leet" o "1337"). Este lenguaje
# se caracteriza por sustituir caracteres alfanuméricos.
# - Utiliza esta tabla (https://www.gamehouse.com/blog/leet-speak-cheat-sheet/) 
#   con el alfabeto y los números en "leet".
#   (Usa la primera opción de cada transformación. Por ejemplo "4" para la "a")

inputText = input("Enter the text to transform: ")
inputText = inputText.lower()

my_dict_leet={"a":"4","b":"I3","c":"[","d":")","e":"3","f":"|=","g":"&",
"h":"#","i":"1","j":",|","k":">|","l":"1","m":"/\/\\","n":"^/","o":"0",
"p":"|*","q":"(,)","r":"I2","s":"5","t":"7","u":"(_)","v":"/","w":"//",
"x":"><","y":"j","z":"2"}

outputText = ""

for chr in inputText:
    for key in my_dict_leet:
        if(key==chr):
            outputText=outputText+my_dict_leet[key]
print(outputText)