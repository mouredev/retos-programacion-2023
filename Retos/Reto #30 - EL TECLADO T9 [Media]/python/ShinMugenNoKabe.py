# Los primeros dispositivos móviles tenían un teclado llamado T9
# con el que se podía escribir texto utilizando únicamente su
# teclado numérico (del 0 al 9).

# Crea una función que transforme las keystrokes del T9 a su
# representación con letras.

# - Debes buscar cuál era su correspondencia original.
# - Cada bloque de keystrokes va separado por un guión.
# - Si un bloque tiene más de un número, debe ser siempre el mismo.
# - Ejemplo:
#     Entrada: 6-666-88-777-33-3-33-888
#     Salida: MOUREDEV


T9_KEYBOARD = {
    "1": [",", ".", "?", "!"],
    "2": ["A", "B", "C"],
    "3": ["D", "E", "F"],
    "4": ["G", "H", "I"],
    "5": ["J", "K", "L"],
    "6": ["M", "N", "O"],
    "7": ["P", "Q", "R", "S"],
    "8": ["T", "U", "V"],
    "9": ["W", "X", "Y", "Z"],
    "0": [" "]
}


def get_character(keystroke: str) -> str:
    num_pressed = keystroke[0]
    times_pressed = len(keystroke)
    
    if not num_pressed in T9_KEYBOARD:
        raise ValueError("Invalid number")
    
    return T9_KEYBOARD[num_pressed][times_pressed - 1]


def get_t9_text(keystrokes: str) -> str:
    if not keystrokes:
        raise ValueError("Please type something in your keyboard")
    
    keystrokes_secuence = keystrokes.split("-")
    
    return "".join([get_character(keystroke) for keystroke in keystrokes_secuence])
    
    
if __name__ == "__main__":
    mouredev = get_t9_text("6-666-88-777-33-3-33-888")
    assert mouredev == "MOUREDEV"
    print(mouredev)
    
    saludos_amigos = get_t9_text("7777-2-555-88-3-666-7777-0-2-6-444-4-666-7777-1111-1111")
    assert saludos_amigos == "SALUDOS AMIGOS!!"
    print(saludos_amigos)