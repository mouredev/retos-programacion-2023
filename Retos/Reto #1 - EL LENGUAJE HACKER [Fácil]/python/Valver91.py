"""
 * Escribe un programa que reciba un texto y transforme lenguaje natural
  a "lenguaje hacker" (conocido realmente como "leet" o "1337").
  Este lenguaje se caracteriza por sustituir caracteres alfanuméricos.
  con el alfabeto y los números en "leet".
 * Utiliza esta tabla:
   (https://www.gamehouse.com/blog/leet-speak-cheat-sheet/) 
 * Usa la primera opción de cada transformación,
   por ejemplo "4" para la "a".
"""

texto_integro = input("Introduce tu texto a traducir: ")

diccionario = {"a":"4", "b":"|3", "c":"[", "d":")", "e":"3",
               "f":"|=", "g":"&", "h":"#", "i":"1", "j":",_|",
               "k":">|", "l":"1", "m":"/\/\\", "n":"^/", "o":"0",
               "p":"|*", "q":"(_,)", "r":"12", "s":"5", "t":"7",
               "u":"(_)", "v":"\\/", "w":"\\/\\/", "x":"><", "y":"j",
               "z":"2", "1":"L", "2":"R", "3":"E", "4":"A", '5':'S',
               '6':'b', '7':'T', '8':'B', '9':'g',
               '0':'o'}

def traductor():
    texto = texto_integro.lower()
    texto_traducido = ""
    for letra in texto:
        if letra in diccionario.keys():
            texto_traducido += diccionario[letra]
        else:
            texto_traducido += letra        
    print(f"Su texto traducido es: {texto_traducido}")

traductor()