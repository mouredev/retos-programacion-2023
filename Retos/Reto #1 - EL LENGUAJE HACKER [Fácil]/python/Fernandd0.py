'''
 Escribe un programa que reciba un texto y transforme lenguaje natural a
 "lenguaje hacker" (conocido realmente como "leet" o "1337"). Este lenguaje
 se caracteriza por sustituir caracteres alfanuméricos.
 - Utiliza esta tabla (https://www.gamehouse.com/blog/leet-speak-cheat-sheet/)
 con el alfabeto y los números en "leet".
 (Usa la primera opción de cada transformación. Por ejemplo "4" para la "a")
'''

#Solucíon:
dicionario_leet = {
    "a":"4",
    "b":"I3",
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
    "m":"/\/\\",
    "n":"^/",
    "o":"0",
    "p":"|*",
    "q": "(_,)",
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
    "5":"5",
    "6":"b",
    "7":"T",
    "8":"B",
    "9":"g",
    "0":"0"
}

def encriptador (texto):
    resultado = "" #variable que almacenará el texto encriptado.
    for char in texto.lower(): #iteracion para cada carácter del texto.
        if char in dicionario_leet: #verificar si el carácter está en el diccionario leet.
            resultado += dicionario_leet[char] #cambia el carácter del texto a "lenguaje hacker".
        else: #en caso el carácter no exista dentro del diccionario leet.
            resultado += char #agrega el carácter sin modificar.
    return resultado

if __name__ == "__main__":
  texto = input("Escriba un texto para encriptar: ")
  print(encriptador(texto))