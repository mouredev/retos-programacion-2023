from pynput.keyboard import Key, Listener, KeyCode
from functools import lru_cache


@lru_cache(maxsize=100)
def konami_sequence() -> list[Key]:
    return [
    Key.up, Key.up, Key.down, Key.down,
    Key.left, Key.right, Key.left, Key.right,
    KeyCode.from_char('b'), KeyCode.from_char('a')
    ]


current_keys = []


def show(key: Key) -> bool:
    current_keys.append(key)

    print(f"\nYou entered: {key}")

    slice_keys = current_keys[-10:] if len(current_keys) > 9 else current_keys
    if len(slice_keys) > 9 and all(command == slice_keys[i] for i, command in enumerate(konami_sequence())):
        print("\nSecuencia Konami detectada!")
        print("¡Felicidades!")
        return False
        
    if key in (Key.esc,):
        print("Adiós, nos vemos pronto")
        return False
        
        
def main() -> None:
    print("--- Intenta adivinar la secuencia konami ---")
    with Listener(on_press=show) as listener:
        listener.join()


if __name__ == "__main__":
    main()