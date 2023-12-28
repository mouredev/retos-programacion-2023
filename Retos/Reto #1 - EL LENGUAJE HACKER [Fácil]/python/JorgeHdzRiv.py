'''
 * Escribe un programa que reciba un texto y transforme lenguaje natural a
 * "lenguaje hacker" (conocido realmente como "leet" o "1337"). Este lenguaje
 *  se caracteriza por sustituir caracteres alfanuméricos.
 * - Utiliza esta tabla (https://www.gamehouse.com/blog/leet-speak-cheat-sheet/) 
 *   con el alfabeto y los números en "leet".
 *   (Usa la primera opción de cada transformación. Por ejemplo "4" para la "a")
 */
'''

leet_diccionary = {
    #diccionario minusculas
        "a":"4",  "b":"|3",  "c":"[", "d":")", "e":"3", "f":"|=", "g":"&", "h":"#", "i":"1",
        "j":",_|", "k":">|", "l":"1", "m":"/\\/\\", "n":"^/", "o":"0", "p":"|*", "q":"(_,)", "r":"I2",
        "s":"5", "t":"7", "u":"(_)", "v":"\\/", "w":"\\/\\/", "x":"><", "y":"j", "z":"2",
    #diccionario numeros
        "0":"o", "1":"L", "2":"R", "3":"E", "4":"A", "5":"S", "6":"b", "7":"T", "8":"B", "9":"g",
    #diccionario mayusculas
        "A":"@", "B":"8", "C":"<", "D":"1)", "E":"€", "F":"|*", "G":"6", "H":"4", "I":"|", "J":"¿", "K":"|{",
        "L":"][", "M":"^^", "N":"?", "O":"<>", "P":"|?", "Q":"(0,)", "R":"|2", "S":"§", "T":"+", "U":"µ", "V":"\|",
        "W":"uu", "X":")(", "Y":"¥", "Z":"2",' ':' '
        }
    

text = input('Ingresa el texto o frase a encriptar: ')

for letter in text:
    print(leet_diccionary[letter],end="")

