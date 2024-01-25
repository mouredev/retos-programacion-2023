"""
/*
 * Crea un programa que realize el cifrado César de un texto y lo imprima.
 * También debe ser capaz de descifrarlo cuando así se lo indiquemos.
 *
 * Te recomiendo que busques información para conocer en profundidad cómo
 * realizar el cifrado. Esto también forma parte del reto.
 */
"""

def cifrar_texto(cadena):
    texto = cadena.lower()
    texto_cifrado = ""
    
    for caracter in texto:
        texto_cifrado += chr(ord(caracter) + 5)
    return texto_cifrado

def descifrar_texto(cadena):
    texto = cadena.lower()
    texto_descifrado = ""

    for caracter in texto:
        texto_descifrado += chr(ord(caracter) - 5)
    return texto_descifrado

print("Selecciona una opcion\n")
print("1. Cifrar texto\n")
print("2. Descifrar texto\n")
opcion = input("Opcion:")
texto = input("Introduce el texto\n")

if int(opcion) == 1:
    print(cifrar_texto(texto))
elif int(opcion) == 2:
    print(descifrar_texto(texto))