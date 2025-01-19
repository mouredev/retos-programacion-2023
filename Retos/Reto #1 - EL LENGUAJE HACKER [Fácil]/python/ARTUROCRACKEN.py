# /*
#  * Escribe un programa que reciba un texto y transforme lenguaje natural a
#  * "lenguaje hacker" (conocido realmente como "leet" o "1337"). Este lenguaje
#  *  se caracteriza por sustituir caracteres alfanuméricos.
#  * - Utiliza esta tabla (https://www.gamehouse.com/blog/leet-speak-cheat-sheet/) 
#  *   con el alfabeto y los números en "leet".
#  *   (Usa la primera opción de cada transformación. Por ejemplo "4" para la "a")
#  */

diccionario_1337 = {"A": "4", "B": "I3", "C": "[", "D": ")", "E": "3", "F": "|=", "G": "&", "H": "#", "I": "1",
            "J": ",_|", "K": ">|", "L": "1", "M": "/\/\\", "N": " ^/", "O": "0", "P": " |*", "Q": "(_,)",
            "R": "I2", "S": "5", "T": "7", "U": "(_)", "V": "\/", "W": "\/\/", "X": "><", "Y": "j", "Z": "2",
            "1": "L", "2": "R", "3": "E", "4": "A", "5": "S", "6": "b", "7": "T", "8": "B", "9": "g", "0": "o"}

def traducir_a_leet(texto):
    if type(texto) != str:
        return "Error: input must be string."

    texto_traducido = ""

    for letra in texto:
        if letra.upper() in diccionario_1337:
            texto_traducido += diccionario_1337[letra.upper()]
        else:
            texto_traducido += letra
    
    return texto_traducido

texto1 = traducir_a_leet("Hola mundo")
texto2 = traducir_a_leet(3)
texto3 = traducir_a_leet(True)

print(texto1)
print(texto2)
print(texto3)
