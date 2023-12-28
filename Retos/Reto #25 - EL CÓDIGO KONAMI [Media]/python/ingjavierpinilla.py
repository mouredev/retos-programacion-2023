from pynput.keyboard import Key, KeyCode, Listener

CODIGO_KONAMI = [
    Key.up,
    Key.up,
    Key.down,
    Key.down,
    Key.left,
    Key.right,
    Key.left,
    Key.right,
    KeyCode.from_char("b"),
    KeyCode.from_char("a"),
]

posicion_actual = 0


def show(key):
    global posicion_actual

    if key == CODIGO_KONAMI[posicion_actual]:
        posicion_actual += 1
    if posicion_actual == len(CODIGO_KONAMI):
        print("\n\n Codigo Konami introducido correctamente")
        posicion_actual = 0


with Listener(on_press=show) as listener:
    listener.join()
