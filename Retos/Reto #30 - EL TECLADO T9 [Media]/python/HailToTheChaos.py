'''
 Los primeros dispositivos móviles tenían un teclado llamado T9
 con el que se podía escribir texto utilizando únicamente su
 teclado numérico (del 0 al 9).

 Crea una función que transforme las pulsaciones del T9 a su
 representación con letras.
 - Debes buscar cuál era su correspondencia original.
 - Cada bloque de pulsaciones va separado por un guión.
 - Si un bloque tiene más de un número, debe ser siempre el mismo.
 - Ejemplo:
     Entrada: 6-666-88-777-33-3-33-888
     Salida: MOUREDEV
'''

KEYBOARD = {
    "0": " ",
    "1": ",.?!",
    "2": "ABC",
    "3": "DEF",
    "4": "GHI",
    "5": "JKL",
    "6": "MNO",
    "7": "PQRS",
    "8": "TUV",
    "9": "WXYZ"
}


def convert_T9_to_text(input: str) -> str:
    output = ""

    keystrokes = input.split("-")

    for keystroke in keystrokes:
        if keystroke[0] in KEYBOARD.keys() and len(keystroke) <= len(KEYBOARD[keystroke[0]]):
            output += KEYBOARD[keystroke[0]][len(keystroke)-1]

    return output


if __name__ == '__main__':
    print(convert_T9_to_text("44-666-555-2-0-6-88-66-3-666-1111"))
