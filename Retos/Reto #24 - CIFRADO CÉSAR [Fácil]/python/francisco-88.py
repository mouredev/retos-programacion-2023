def cifrar(texto, clave):
    resultado = ""

    for char in texto:
        if char.isalpha():
            ascii_offset = 65 if char.isupper() else 97
            resultado += chr((ord(char) - ascii_offset + clave) % 26 + ascii_offset)
        else:
            resultado += char
    
    return resultado

def descifrar(texto, clave):
    return cifrar(texto, -clave)

opcion = input("¿Quieres cifrar o descifrar? Por favor utiliza c=cifrar o d=descifrar: ")
clave = int(input("Ingresa el número de desplazamientos: "))
mensaje = input("Ingresa el mensaje: ")

if opcion.lower() == "c":
    print("Mensaje cifrado: " + cifrar(mensaje, clave))
elif opcion.lower() == "d":
    print("Mensaje descifrado: " + descifrar(mensaje,clave))
else:
    print("Opción inválida")