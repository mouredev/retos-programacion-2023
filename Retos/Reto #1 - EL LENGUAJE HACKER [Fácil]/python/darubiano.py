"""
 Escribe un programa que reciba un texto y transforme lenguaje natural a 'lenguaje hacker' (conocido realmente como "leet" o "1337").
 Este lenguaje se caracteriza por sustituir caracteres alfanuméricos.
 
 Utiliza esta tabla (https://www.gamehouse.com/blog/leet-speak-cheat-sheet/) con el alfabeto y los números en "leet".
 (Usa la primera opción de cada transformación. Por ejemplo "4" para la "a")
"""
diccionario={"a":"4","b":"I3","c":"[","d":")","e":"3","f":"|=","g":"&","h":"#","i":"1","j":",_|","k":">|","l":"1",'m' : '/\/\\', 'n' : '^/', 'o' : '0', 'p' : '|*', 'q' : '(_,)', 'r' : 'I2', 's' : '5', 't' : '7', 'u' : '(_)', 'v' : '\/', 'w' : '\/\/', 'x' : '><', 'y' : 'j', 'z' : '2','1' : 'L','2' : 'R','3' : 'E','4' : 'A','5' : 'S','6' : 'b','7' : 'T','8' : 'B', '9' : 'g','0' : 'o'}
def lenguaje_hacker_junior(texto):
    texto_hacker = ""
    for letra in texto:
        letra = letra.lower()
        if letra in diccionario:
            texto_hacker += diccionario[letra]
        else:
            texto_hacker += letra
    print(texto_hacker)
#* Solucion junior
lenguaje_hacker_junior("Aquí está un texto de prueba para ver si funciona el reto!")

def lenguaje_hacker_senior(texto):
    texto = texto.lower()   
    texto_hacker = texto.translate(texto.maketrans(diccionario))
    print(texto_hacker)
#* Solucion senior
lenguaje_hacker_senior("Aquí está un texto de prueba para ver si funciona el reto!")

def lenguaje_hacker_chatgpt(texto):
    print(texto.lower().translate(str.maketrans(diccionario)))
#* Solucion chatgpt 👀
lenguaje_hacker_chatgpt("Aquí está un texto de prueba para ver si funciona el reto!")

