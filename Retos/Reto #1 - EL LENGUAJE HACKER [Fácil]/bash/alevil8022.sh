#
# Escribe un programa que reciba un texto y transforme lenguaje natural a
# "lenguaje hacker" (conocido realmente como "leet" o "1337"). Este lenguaje
#  se caracteriza por sustituir caracteres alfanuméricos.
# - Utiliza esta tabla (https://www.gamehouse.com/blog/leet-speak-cheat-sheet/) 
#   con el alfabeto y los números en "leet".
#   (Usa la primera opción de cada transformación. Por ejemplo "4" para la "a")
#

alfabeto = dict()

alfabeto = {"a":"4", 
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
            "m":"'/\/\'",
            "n":"^/",
            "o":"0",
            "p":"|*",
            "q":"(_,)",
            "r":"I2",
            "s":"5",
            "t":"7",
            "u":"(_)",
            "v":"\/",
            "w":"\/\/",
            "x":"><",
            "y":"j",
            "z":"2",
            " ":" "
            }


def convertir_texto(oracion, new_oracion):
    palabra=oracion.split(" ")
    cant_palabras=len(palabra)
    # print(palabra)
    new_oracion = ""
    numero=0
    for caracter in palabra:
        numero += 1
        caracter_min = caracter.lower()
        #print(caracter_min)
        cant_caracter=len(caracter_min)
        # print(cant_caracter)
        cant = 0
        new_palabra = ""
        new_caracter = ""
        while cant < cant_caracter:
            #print(caracter_min[cant])
            indice=caracter_min[cant]
            new_caracter = alfabeto[indice]
            new_palabra = new_palabra + new_caracter
            cant +=1
            #print(new_palabra)
        if cant_palabras <= numero:
            new_oracion = new_oracion + new_palabra
        else:
            new_oracion = new_oracion + new_palabra + " "
            #print(new_oracion)
    return new_oracion


oracion = input("Escriba la Palabra a traducir: ")
new_oracion = str
print("TEXTO ORIGINAL: ", oracion)
oracion_traducida = convertir_texto(oracion, new_oracion)
print("TEXTO TRADUCIDO: ", oracion_traducida)
