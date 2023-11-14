# Reto 01: El lenguaje hacker
# /*
#  * Escribe un programa que reciba un texto y transforme lenguaje natural a
#  * "lenguaje hacker" (conocido realmente como "leet" o "1337"). Este lenguaje
#  *  se caracteriza por sustituir caracteres alfanuméricos.
#  * - Utiliza esta tabla (https://www.gamehouse.com/blog/leet-speak-cheat-sheet/) 
#  *   con el alfabeto y los números en "leet".
#  *   (Usa la primera opción de cada transformación. Por ejemplo "4" para la "a")
#  */

def leet_translate(text):
    leet = {"A":"4","B":"|3","C":"[","D":")","E":"3","F":"|=","G":"&","H":"#","I":"1",
            "J":",_|","K":">|","L":"1","M":"/\/\\","N":"^/","O":"0","P":"|*","Q":"(_,)",
            "R":"|2","S":"5","T":"7","U":"(_)","V":"\/","W":"\/\/","X":"><","Y":"j","Z":"2"}
    
    leet_text = ""

    for i in text:
        if i in leet:
            leet_text = leet_text + leet[i]
        else:
            leet_text = leet_text + i
    
    return leet_text

print("Leet translator")
print("===============")

text = input("Introduce un texto:")
leet_text = ""

leet_text = leet_translate(text.upper())

print(leet_text)
