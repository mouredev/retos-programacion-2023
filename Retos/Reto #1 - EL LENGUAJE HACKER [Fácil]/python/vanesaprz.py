"""
# Reto #1: EL "LENGUAJE HACKER"
#### Dificultad: Fácil | Publicación: 02/01/23 | Corrección: 09/01/23

## Enunciado
/*
 * Escribe un programa que reciba un texto y transforme lenguaje natural a
 * "lenguaje hacker" (conocido realmente como "leet" o "1337"). Este lenguaje
 *  se caracteriza por sustituir caracteres alfanuméricos.
 * - Utiliza esta tabla (https://www.gamehouse.com/blog/leet-speak-cheat-sheet/) 
 *   con el alfabeto y los números en "leet".
 *   (Usa la primera opción de cada transformación. Por ejemplo "4" para la "a")
 */
"""
#creación de diccionario leet conteniendo las equivalencias.
leet= {

    "a": "4",
    "b": "I3",
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
    "m": "/\/\ ",
    "n":"^/",
    "o":"0",
    "P":"|*",
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
}

def translate_to_leet(text:str)  -> str:
    in_leet= "" #empty list en la que se guardará la traducción.
    for letter in text.lower(): #se convierten las letras a minúsculas para poder compararlas con el diccionario
        try:
            in_leet += leet[letter] #se añaden las traducciones a la lista vacía.
        except KeyError:
            in_leet += letter #En caso de que se emplee una letra/símbolo no incluidos en el diccionario, se incluirá el símbolo tal cual
    return in_leet

texto=input("Indica el texto a traducir a leet: ")

print(translate_to_leet(texto))
    
