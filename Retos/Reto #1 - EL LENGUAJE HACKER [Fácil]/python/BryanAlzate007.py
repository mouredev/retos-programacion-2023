"""
/*
 * Escribe un programa que reciba un texto y transforme lenguaje natural a
 * "lenguaje hacker" (conocido realmente como "leet" o "1337"). Este lenguaje
 *  se caracteriza por sustituir caracteres alfanuméricos.
 * - Utiliza esta tabla (https://www.gamehouse.com/blog/leet-speak-cheat-sheet/) 
 *   con el alfabeto y los números en "leet".
 *   (Usa la primera opción de cada transformación. Por ejemplo "4" para la "a")
 */
"""

alphabet = {
    "a":"4",
    "b":"|3",
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
    "m":"/\/\ ",
    "n":"^/",
    "o":"0",
    "p":"|*",
    "q":"(_,)",
    "r":"|2",
    "s":"5",
    "t":"7",
    "u":"(_)",
    "V":"\/",
    "w":"\/\/",
    "x":"><",
    "y":"j",
    "z":"2"
    }

def leet(text):
    text = text.lower()
    text_leet=""
    for i in text:
        if i in alphabet:
            text_leet += alphabet[i]        
        else:
            text_leet += i
    return text_leet

text = input("ingresa el texto que deseas cambiar a leet ")
print(f'El texto en Leet es: {leet(text)}')