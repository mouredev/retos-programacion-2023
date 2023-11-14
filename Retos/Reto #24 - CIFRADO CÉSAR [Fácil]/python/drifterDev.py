def cifrar_mensaje(mensaje, desplazamiento):
    letras = "ABCDEFGHIJKLMNOPQRSTUVWXYZ".lower()
    mensaje_cifrado = ""
    mensaje = mensaje.lower()
    for letra in mensaje:
        if letra in letras:
            mensaje_cifrado += letras[
                (letras.index(letra) + desplazamiento) % (len(letras))
            ]
        else:
            mensaje_cifrado += letra
    return mensaje_cifrado


def descifrar_mensaje(mensaje, desplazamiento):
    letras = "ABCDEFGHIJKLMNOPQRSTUVWXYZ".lower()
    mensaje_descifrado = ""
    mensaje = mensaje.lower()
    for letra in mensaje:
        if letra in letras:
            mensaje_descifrado += letras[
                (letras.index(letra) - desplazamiento) % len(letras)
            ]
        else:
            mensaje_descifrado += letra
    return mensaje_descifrado


if __name__ == "__main__":
    try:
        modo = int(
            input(
                "Ingrese la opcion deseada\n1- Cifrar mensaje\n2- Descifrar mensaje\n"
            )
        )
        mensaje = input("Por favor ingrese el mensaje\n")
        desplazamiento = int(
            input(
                "Ahora introduzca el número de desplazamientos para realizar el algoritmo\n"
            )
        )
        if modo == 1:
            print(cifrar_mensaje(mensaje, desplazamiento))
        elif modo == 2:
            print(descifrar_mensaje(mensaje, desplazamiento))
        print("\nPrograma finalizado.")
    except:
        print("Error al introducir la información")
