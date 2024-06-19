"""
Reto #1: EL "LENGUAJE HACKER"

/*
 * Escribe un programa que reciba un texto y transforme lenguaje natural a
 * "lenguaje hacker" (conocido realmente como "leet" o "1337"). Este lenguaje
 *  se caracteriza por sustituir caracteres alfanuméricos.
 * - Utiliza esta tabla (https://www.gamehouse.com/blog/leet-speak-cheat-sheet/) 
 *   con el alfabeto y los números en "leet".
 *   (Usa la primera opción de cada transformación. Por ejemplo "4" para la "a")
 */
"""

#Crear la funcion para traducir texto a "leet"
def leet_translator(text):
      #Diccionario para cambiar los valores alfanumericos a "leet"
      leet = {
        "A": "4",
        "B": "I3",
        "C": "[",
        "D": ")",
        "E": "3",
        "F": "|=",
        "G": "&",
        "H": "#",
        "I": "1",
        "J": ",_|",
        "K": ">|",
        "L": "1",
        "M": "/\\/\\",
        "N": " ^/",
        "O": "0",
        "P": " |*",
        "Q": "(_,)",
        "R": "I2",
        "S": "5",
        "T": "7", 
        "U": "(_)", 
        "V": "\\/", 
        "W": "\\/\\/", 
        "X": "><", 
        "Y": "j", 
        "Z": "2",
        "1": "L", 
        "2": "R", 
        "3": "E", 
        "4": "A", 
        "5": "S", 
        "6": "b", 
        "7": "T", 
        "8": "B", 
        "9": "g", 
        "0": "o"}

      #Crear la variable donde se almacenara la cadena leet
      leet_text = ""
 
      #Se recorre cada caracter 'letra' en el texto 'text'
      for letra in text:
        #letra.upper() convierte la letra a mayúscula para buscarla en el diccionario leet
        if letra.upper() in leet:
          #Si la letra está en el diccionario leet, se agrega su equivalente en "leet" a leet_text
          leet_text += leet[letra.upper()]
        # Si no está en el diccionario, se agrega la letra tal cual a leet_text
        else:
          leet_text += letra
      #Retorno del texto traducido
      return leet_text

#Pedir el texto al ususario
texto = input("Ingrese el texto a traducir: ")
#Crear una variable para traducir el texto ingresado con la funcion leet_translator
texto_traducido = leet_translator(texto)
#Mostrar el resultado
print(f"\nTexto encriptado: {texto_traducido}")