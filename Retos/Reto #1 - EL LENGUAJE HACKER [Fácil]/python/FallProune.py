"""
Por FallProune
/*
* Escribe un programa que reciba un texto y transforme lenguaje natural a
* "lenguaje hacker" (conocido realmente como "leet" o "1337"). Este lenguaje
*  se caracteriza por sustituir caracteres alfanuméricos.
* - Utiliza esta tabla (https://www.gamehouse.com/blog/leet-speak-cheat-sheet/) 
*   con el alfabeto y los números en "leet".
*   (Usa la primera opción de cada transformación. Por ejemplo "4" para la "a")
*/
"""
#Primero voy a crear una variable que va a ser un diccionario del alfabeto y su traduccion al hacker

leetalf = {
    "a": "4",
    "b": "8",
    "c":"©",
    "d":"cl",
    "e":"3",
    "f":"|=",
    "g":"9",
    "h":"]-[",
    "i":"1",
    "j":",_|",
    "k":"1<",
    "l":"|",
    "m":"[V]",
    "n":"И",
    "o":"0",
    "p":"|o",
    "q":"(_,)",
    "r":"I2",
    "s":"5",
    "t":"7",
    "u":"(_)",
    "v":"บ",
    "w":"VV",
    "x":"×",
    "y":"Ч",
    "z":"2",
    " ": " ",
    "1":"I",
    "2": "R",
    "3": "E",
    "4": "A",
    "5": "S",
    "6": "G",
    "7": "T",
    "8": "B",
    "9": "g",
    "0": "O"
}
def traductor(): 
    text = input("Ingresa el texto que deceas traducir")
    traduction = ""

    for i in text : 
        x = leetalf.get(i.lower())
        traduction = "".join([traduction, x])   
        
    print(traduction)
    
traductor()
