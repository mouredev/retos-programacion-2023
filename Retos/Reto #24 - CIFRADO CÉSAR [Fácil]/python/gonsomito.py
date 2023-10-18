"""
 * Crea un programa que realize el cifrado César de un texto y lo imprima.
 * También debe ser capaz de descifrarlo cuando así se lo indiquemos.
 *
 * Te recomiendo que busques información para conocer en profundidad cómo
 * realizar el cifrado. Esto también forma parte del reto.
"""

#En esta función recibo texto y clave para realizar la transcripción/cifrado.
#Hago uso de la funcion char()y ord() para sumar con valor ASCII. Devuelve el resultado
def caesar_palace_cyph(texto, clave):
    resultado = ""
    for char in texto:
        if ord(char) >= 65 and ord(char) <= 90:
            resultado += chr((ord(char) - 65 + clave) % 26 + 65)
        else:
            resultado += char
    return resultado
    
#Para no repetir código, uso esta función que pide texto y clave de codificación.    
def dame_texto():
    texto = input("Introduce texto: ").upper()
    clave = int(input("Qué clave numérica quieres usar: "))
    return texto, clave

#Este menú controla las opciones de cifrado en ambas direcciones. Salir si no se marca una válida.
def menu():
    print("BIENVENIDO AL CIFRADOR / DESCIFADROR <<CAESAR PALACE>>\n¿Qué quieres hacer?")
    print("1. Cifrar texto")
    print("2. Descifrar texto")
    print("")
    opcion = input("Ingrese una opción (1 o 2). Cualquier otra opción para SALIR: ")
    if opcion == "1":
        texto, clave = dame_texto()
        resultado = caesar_palace_cyph(texto, clave)
        print("Texto cifrado:", resultado)
    elif opcion == "2":
        texto, clave = dame_texto()        
        resultado = caesar_palace_cyph(texto, clave*-1)
        print("Texto descifrado:", resultado)
    else:
        print("Opción NO válida. Adiós muy buenas.")
        return False
                
menu()
