# /*
#  * Escribe un programa que reciba un texto y transforme lenguaje natural a
#  * "lenguaje hacker" (conocido realmente como "leet" o "1337"). Este lenguaje
#  *  se caracteriza por sustituir caracteres alfanuméricos.
#  * - Utiliza esta tabla (https://www.gamehouse.com/blog/leet-speak-cheat-sheet/) 
#  *   con el alfabeto y los números en "leet".
#  *   (Usa la primera opción de cada transformación. Por ejemplo "4" para la "a")
#  */
def traductor_leet(texto: str):
    dic_caracteres = {
        "A":"4",
        "B":"I3",
        "C":"[",
        "D":")",
        "E":"3",
        "F":"|=",
        "G":"&",
        "H":"#",
        "I":"1",
        "J":",_|",
        "K":">|",
        "L":"1",
        "M":"/\/\\", #Doble barra porque si no cree el las "" son parte del str
        "N":"^/",
        "O":"0",
        "P":"|*",
        "Q":"(_,)",
        "R":"|2",
        "S":"5",
        "T":"7",
        "U":"(_)",
        "V":"\/",
        "W":"\/\/",
        "X":"><",
        "Y":"j",
        "Z":"2",
        " ":" "
    }

    texto = texto.upper()
    nuevo_texto = ""
    for palabra in texto:
        for letra in palabra:
            nuevo_texto += dic_caracteres.get(letra, "") #Lo que no este en el dicccionario lo suprime
    return nuevo_texto

print("Introduce el texto que se transformara a \"leet\" (Solo letras):")
texto = input()
print(traductor_leet(texto))
