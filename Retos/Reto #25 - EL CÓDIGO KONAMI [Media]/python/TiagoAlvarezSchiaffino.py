from pynput import keyboard
from pynput.keyboard import Key, Listener, KeyCode

KONAMI_CODE = [
    Key.up,
    Key.up,
    Key.down,
    Key.down,
    Key.left,
    Key.right,
    Key.left,
    Key.right,
    KeyCode.from_char("b"),
    KeyCode.from_char("a")
]

key_position = 0

def on_press(key):
    """
    Function to be called when a key is pressed.

    Args:
        key: The key that was pressed.
    """
    global key_position

    if key == Key.esc:
        print("Exiting...")
        return False

    if key == KONAMI_CODE[key_position]:
        key_position += 1
    elif key == KONAMI_CODE[0]:
        if key_position == 0:
            key_position = 1
        else:
            key_position = 0
    else:
        key_position = 0

    if key_position == len(KONAMI_CODE):
        print("""
        \n
        ╦╔═╔═╗╔╗╔╔═╗╔╦╗╦  ╔═╗╔═╗╔╦╗╔═╗
        ╠╩╗║ ║║║║╠═╣║║║║  ║  ║ ║ ║║║╣ 
        ╩ ╩╚═╝╝╚╝╩ ╩╩ ╩╩  ╚═╝╚═╝═╩╝╚═╝
        \n
        """)
        return False

with Listener(on_press=on_press) as listener:
    listener.join()
