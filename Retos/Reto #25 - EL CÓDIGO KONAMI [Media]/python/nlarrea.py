from pynput.keyboard import Key, Listener, KeyCode

KONAMI = [
    Key.up, Key.up,
    Key.down, Key.down,
    Key.left, Key.right,
    Key.left, Key.right,
    KeyCode.from_char('b'),
    KeyCode.from_char('a')
]

user_pressed = []

def on_press(key):
    try:
        user_pressed.append(key)
        print(f"pressed key: {key}")

        if all(list(map(
            lambda user_key, konami_key: user_key == konami_key,
            user_pressed, KONAMI
        ))):
            print("\nKONAMI CODE!\n")
            
        if len(user_pressed) == len(KONAMI):
            user_pressed.pop(0)
    except:
        pass

def on_release(key):
    if key == Key.esc:
        # stop listener
        return False




if __name__ == "__main__":
    print("Enter ESC to quit at any time.\n")
    
    # collect events untill released
    with Listener(on_press=on_press, on_release=on_release) as listener:
        listener.join()