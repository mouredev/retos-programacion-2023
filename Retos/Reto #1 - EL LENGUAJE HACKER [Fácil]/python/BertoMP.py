"""
 Escribe un programa que reciba un texto y transforme lenguaje natural a
 "lenguaje hacker" (conocido realmente como "leet" o "1337"). Este lenguaje
 se caracteriza por sustituir caracteres alfanuméricos.
 - Utiliza esta tabla (https://www.gamehouse.com/blog/leet-speak-cheat-sheet/)
 con el alfabeto y los números en "leet".
 (Usa la primera opción de cada transformación. Por ejemplo "4" para la "a")
 """


def cambia_letra(caracter):
    alfanum = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p',
               'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z', '0', '1', '2', '3', '4', '5', '6', '7',
               '8', '9']
    lenguaje_leet = ["4", "|3", "[", ")", "3", "|=", "&", "#", "1", ",_|", ">|", "1", "/\\/\\", "^/",
                     "0", "|*", "(_,)", "I2", "5", "7", "(_)", "\\/", "\\/\\/", "><", "j", "2", "o", "L", "R", "E", "A",
                     "S", "b", "T", "B", "g"]

    index = alfanum.index(caracter)
    return lenguaje_leet[index]


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
    texto_usuario = input("Introduce un texto a traducir: ")
    texto_traducido = traduce_a_leet(texto_usuario)
    print(f"El texto en lenguaje hacker es {texto_traducido}.")


inicio()
