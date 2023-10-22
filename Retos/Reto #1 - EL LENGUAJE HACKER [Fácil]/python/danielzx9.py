"""```
/*
 * Escribe un programa que reciba un texto y transforme lenguaje natural a
 * "lenguaje hacker" (conocido realmente como "leet" o "1337"). Este lenguaje
 *  se caracteriza por sustituir caracteres alfanuméricos.
 * - Utiliza esta tabla (https://www.gamehouse.com/blog/leet-speak-cheat-sheet/) 
 *   con el alfabeto y los números en "leet".
 *   (Usa la primera opción de cada transformación. Por ejemplo "4" para la "a")
 */
```"""

print("Ingrese un texto para transformar en lenguaje hacker")
diccionario={"a":"4","b":"I3","c":"[","d":")","e":"3","f":"|=","g":"&","h":"#","i":"1","j":",_|","k":">|","l":"1",'m' : '/\/\\', 'n' : '^/', 'o' : '0', 'p' : '|*', 'q' : '(_,)', 'r' : 'I2', 's' : '5', 't' : '7', 'u' : '(_)', 'v' : '\/', 'w' : '\/\/', 'x' : '><', 'y' : 'j', 'z' : '2','1' : 'L','2' : 'R','3' : 'E','4' : 'A','5' : 'S','6' : 'b','7' : 'T','8' : 'B', '9' : 'g','0' : 'o'}


text = input()

for caracter in text:
    caracter = caracter.lower()
    hacker_text = ""

    if caracter in diccionario:
        hacker_text += diccionario[caracter]
    else:
        hacker_text += caracter
    print(hacker_text)



    
    


