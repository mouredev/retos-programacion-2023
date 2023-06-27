from pynput.keyboard import Key, KeyCode, Listener

KONAMI_CODE = [
    Key.up, Key.up, Key.down, Key.down,
    Key.left, Key.right, Key.left, Key.right,
    KeyCode.from_char("b"), KeyCode.from_char("a")
]

key_position = 0
last_key = Key.esc

def on_press(key):

    global key_position, last_key

    if key == Key.esc:
        print("Exit")
        return False    

    if key == KONAMI_CODE[key_position]:
        key_position += 1
    elif key == KONAMI_CODE[1] and last_key == KONAMI_CODE[0]:
        # Se controla que se escriba varias veces la primera tecla válida
        key_position = 2
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
    
    last_key = key

with Listener(on_press=on_press) as listener:
    listener.join()