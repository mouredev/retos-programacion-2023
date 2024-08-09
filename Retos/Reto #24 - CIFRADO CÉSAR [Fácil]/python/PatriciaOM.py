"""
Crea un programa que realize el cifrado César de un texto y lo imprima.
También debe ser capaz de descifrarlo cuando así se lo indiquemos.

Te recomiendo que busques información para conocer en profundidad cómo
realizar el cifrado. Esto también forma parte del reto.
"""
import unicodedata
from unicodedata import normalize

def reto24(text: str, cifrado:bool, desplazamiento:int):
    #El cifrado César consiste en desplazar una cantidad de letras concreta. Si ciframos sumamos, si desciframos restamos.
    #creamos el alfabeto
    alfabeto = ["a", "b", "c", "d", "e", "f", "g", "h", "i", "j", "k", "l", "m"
                "n", "o", "p", "q", "r", "s", "t", "u", "v", "w", "x", "y", "z"]
    texto_cifrado = ""
    i = 0
    #pasamos el texto a minúscula y le quitamos los acentos para evitar errores
    text = text.lower()
    text = normalize('NFD', text).encode('ascii', 'ignore').decode("utf-8")
    while i < len(text):
        #en caso de querer cifrarlo
        if cifrado:
            if text[i] in alfabeto:
                indice = alfabeto.index(text[i]) #nos quedamos con el indice
                if (indice+desplazamiento) < len(alfabeto): #comprobamos que no nos quedamos fuera de rango
                    texto_cifrado = texto_cifrado + alfabeto[indice+desplazamiento]
                else:
                    #Si sumamos y nos pasamos de rango, guardamos la cantidad de caracteres que nos sobran para empezar a contar desde atrás
                    caracteres_sobran = len(alfabeto) - indice - desplazamiento
                    texto_cifrado = texto_cifrado + alfabeto[-caracteres_sobran]    
            else:
                texto_cifrado = texto_cifrado + text[i]
        #en caso de querer descifrarlo
        else:
            if text[i] in alfabeto:
                indice = alfabeto.index(text[i])
                #en este caso nos podemos salir del rango cuando restamos el desplazamiento
                if (indice-desplazamiento) >= 0:
                    texto_cifrado = texto_cifrado + alfabeto[indice-desplazamiento]
                else:
                    caracteres_faltan = indice - desplazamiento #da un número negativo
                    texto_cifrado = texto_cifrado + alfabeto[len(alfabeto)+caracteres_faltan] #hay que sumarlo porque el número es negativo
            else:
                texto_cifrado = texto_cifrado + text[i]
        i+=1
    
    return texto_cifrado

print(reto24("lsqe e xshsw bcde", False, 4))
print(reto24("Hola a todos xyzw", True, 4))