"""
 Escribe un programa que reciba un texto y transforme lenguaje natural a
 "lenguaje hacker" (conocido realmente como "leet" o "1337"). Este lenguaje
 se caracteriza por sustituir caracteres alfanuméricos.
 - Utiliza esta tabla (https://www.gamehouse.com/blog/leet-speak-cheat-sheet/)
 con el alfabeto y los números en "leet".
 (Usa la primera opción de cada transformación. Por ejemplo "4" para la "a")
 """


def cambia_letra(caracter):
    diccionario_esp_leet = {
        "a": "4",
        "b": "|3",
        "c": "[",
        "d": ")",
        "e": "3",
        "f": "|=",
        "g": "&",
        "h": "#",
        "i": "1",
        "j": ",_|",
        "k": ">|",
        "l": "1",
        "m": "/\\/\\",
        "n": "^/",
        "o": "0",
        "p": "|*",
        "q": "(_,)",
        "r": "I2",
        "s": "5",
        "t": "7",
        "u": "(_)",
        "v": "\\/",
        "w": "\\/\\/",
        "x": "><",
        "y": "j",
        "z": "2",
        "0": "o",
        "1": "L",
        "2": "R",
        "3": "E",
        "4": "A",
        "5": "S",
        "6": "b",
        "7": "T",
        "8": "B",
        "9": "g",
    }

    return diccionario_esp_leet[caracter]


def traduce_a_leet(texto):
    texto_en_leet = ""
  
    for letra in texto:
        if letra == 'ñ':
            texto_en_leet += "ñ"
        elif letra.isalnum():
            texto_traducido = cambia_letra(letra)
            texto_en_leet += texto_traducido
        else:
            texto_en_leet += letra
          
    return texto_en_leet


def inicio():
    texto_usuario = input("Introduce un texto a traducir: ").lower()
    texto_traducido = traduce_a_leet(texto_usuario)
    print(f"El texto en lenguaje hacker es {texto_traducido}.")


inicio()
