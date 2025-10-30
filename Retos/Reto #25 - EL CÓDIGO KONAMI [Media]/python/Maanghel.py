"""
Crea un programa que detecte cuando el famoso "Código Konami" se ha
    introducido correctamente desde el teclado.
Si sucede esto, debe notificarse mostrando un mensaje en la terminal.
"""

from pynput.keyboard import Key, Listener, Controller

KONAMI_CODE = [
    Key.up, Key.up, Key.down, Key.down,
    Key.left, Key.right, Key.left, Key.right,
    "a", "b"
    ]

press_keys = []

def on_press(key):
    """
    Maneja cada pulsación registrada por el listener.

    Convierte la tecla a un tipo comparable (string o Key) y la almacena
    en la lista de pulsaciones. Comprueba si las últimas teclas ingresadas
    coinciden con el código Konami; de ser así, imprime un mensaje y
    simula la pulsación de la tecla ESC para detener el programa.

    Args:
        key: objeto Key proporcionado por pynput que representa la tecla pulsada.
    """

    global press_keys
    keyboard = Controller()

    try:
        k = key.char
    except AttributeError:
        k = key

    press_keys.append(k)

    if press_keys[-len(KONAMI_CODE):] == KONAMI_CODE:
        print("¡Codigo KONAMI detectado!")
        keyboard.press(Key.esc)
        keyboard.release(Key.esc)

def on_release(key):
    """
    Maneja el evento de liberación de tecla.

    Si se libera la tecla ESC, imprime un mensaje y devuelve False para
    detener el listener.

    Args:
        ke
    if key == Key.esc:
        print("\nDeteniendo...")
        return False
    """

with Listener(on_press=on_press, on_release=on_release) as listener:
    print("Escuchando pulsaciones del teclado. Presiona 'esc' para salir.")
    listener.join()
