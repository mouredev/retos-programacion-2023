'''
/*
 * Escribe un programa que reciba un texto y transforme lenguaje natural a
 * "lenguaje hacker" (conocido realmente como "leet" o "1337"). Este lenguaje
 *  se caracteriza por sustituir caracteres alfanuméricos.
 * - Utiliza esta tabla (https://www.gamehouse.com/blog/leet-speak-cheat-sheet/) 
 *   con el alfabeto y los números en "leet".
 *   (Usa la primera opción de cada transformación. Por ejemplo "4" para la "a")
 */
'''

leetDict={"a":"4", "e":"3", "i":"1", "o":"0", "u":"v"}

def thelleter():
    text=input("Introduce un texto para transformar:")
    for l in leetDict.keys():
        text = text.replace(l, leetDict[l])
        
    return text


print(thelleter()) 