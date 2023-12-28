# No estoy usando la letra ñ
print("Cifrado Cesar")

TAM_MAX = 26 # total de letras

def Mensaje():
    print("Introduzca mensaje: ")
    return input("-> ").lower()


def ObtenerRot():
    rot = 0
    while True:
        print(f"Ingrese ROT (1 - {TAM_MAX})")
        rot = int(input("-> "))
        if rot >= 1 and rot <= TAM_MAX:
            return rot


def MensajeTraducido(mensaje, rot):
    traduccion = ""

    for letra in mensaje:
        if letra.isalpha():
            num = ord(letra)
            num += rot

            if num > ord("z"):
                num -= 26
            elif num < ord("a"):
                num += 26

            traduccion += chr(num)
        else:
            traduccion += letra

    print(f"Traduccion: {traduccion}")

mensaje = Mensaje()
rot = ObtenerRot()

MensajeTraducido(mensaje, rot)
