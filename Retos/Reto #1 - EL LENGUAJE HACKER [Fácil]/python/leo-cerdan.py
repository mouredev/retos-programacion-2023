"""
 Escribe un programa que reciba un texto y transforme lenguaje natural a
 "lenguaje hacker" (conocido realmente como "leet" o "1337"). Este lenguaje
  se caracteriza por sustituir caracteres alfanuméricos.
 - Utiliza esta tabla (https://www.gamehouse.com/blog/leet-speak-cheat-sheet/) 
   con el alfabeto y los números en "leet".
   (Usa la primera opción de cada transformación. Por ejemplo "4" para la "a")
"""

def lenguaje_hacker(text):
    hacker = {
        "a":"4", "á":"4", "b":"I3", "c":"[", "d":")", "e":"3", "é":"3", "f":"|=", "g":"&",
        "h":"#", "i":"1", "í":"1", "j":",_|", "k":">|", "l":"1", "m":"/\/\ ", "n":"^/",
        "o":"0", "ó":"0", "p":"|*", "q":"(_,)", "r":"I2", "s":"5", "t":"7", "u":"(_)",
        "ú":"(_)", "v":"\/", "w":"\/\/", "x":"><", "y":"j", "z":"2", "1":"L", "2":"R",
        "3":"E", "4":"A", "5":"S", "6":"b", "7":"T", "8":"B", "9":"g", "0":"o"
    }

    text = text.lower()
    resultado = ""
    for i in text:
        if i in hacker:
            resultado += hacker[i] + " "

    return resultado[0:len(resultado)]

def main():
    print(lenguaje_hacker("leet"))
    print(lenguaje_hacker("Reto hecho en Python"))
    print(lenguaje_hacker("Máquina"))
    print(lenguaje_hacker("FUSIÓN"))
    print(lenguaje_hacker("51786"))

main()
