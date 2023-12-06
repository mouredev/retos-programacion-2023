import string

ASCII_UPPERCASE = list(string.ascii_uppercase)


def encrypt(text: str, shift: int):
    return caesar_cipher(text, shift, True)


def decrypt(text: str, shift: int):
    return caesar_cipher(text, shift, False)


def caesar_cipher(text: str, shift: int = 3, operation: bool = True) -> str:
    coded_text = ""
    text = text.upper()

    for c in text:
        if c not in ASCII_UPPERCASE:
            coded_text += c
            continue
        _shift = shift if operation else shift * -1
        new_index = (ASCII_UPPERCASE.index(c) + _shift) % len(ASCII_UPPERCASE)
        coded_text += ASCII_UPPERCASE[new_index]
    return coded_text


if __name__ == "__main__":
    text = str(input("Por favor ingrese el texto: "))
    shift = int(input("Por favor ingrese el desplazamiento: "))
    operation = int(
        input("Por favor indique la operacion: \n1. Encriptar \n2. Desencriptar\n")
    )
    if operation == 1:
        print(encrypt(text=text, shift=shift))
    elif operation == 2:
        print(decrypt(text=text, shift=shift))
    else:
        print("Operación invalida")
