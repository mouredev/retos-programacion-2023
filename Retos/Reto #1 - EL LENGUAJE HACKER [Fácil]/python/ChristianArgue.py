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

lenguaje_hacker = {"A": "4", "B": "I3", "C": "[", "D": ")", "E": "3", "F": "|=", "G": "&", "H": "#", "I": "1", "J": ",_|", "K": ">|",
                   "L": "1", "M": "/\/\\", "N": "^/", "O": "0", "P": "|*", "Q": "(_,)", "R": "I2", "S": "5", "T": "7", "U": "(_)", "V": "\/",
                   "W": "\/\/", "X": "><", "Y": "j", "Z": "2"}


texto = input('Ingrese una palabra: ')
new_text = ''

for e in texto.upper():
    if e in lenguaje_hacker:
        new_text += lenguaje_hacker[e]
    else:
        new_text += e

print(f'Su nueva palabra es: {new_text}')