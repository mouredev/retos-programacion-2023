# escribir sin espacios
# en caso de presionar una tecla no correspondiente se saltará a otra línea
# si lo prueban en pycharm los simbolos se imprimen al momento de apretarlas, en VSCode no sé porque no

import keyboard

KONAMI_CODE = "↑ ↑ ↓ ↓ ← → ← → B A".lower().split()

userInput = []


def on_press(event):
    global userInput
    if event.name == "flecha arriba":
        print("↑", end="")
        userInput.append("↑")
    elif event.name == "flecha abajo":
        print("↓", end="")
        userInput.append("↓")
    elif event.name == "flecha izquierda":
        print("←", end="")
        userInput.append("←")
    elif event.name == "flecha derecha":
        print("→", end="")
        userInput.append("→")
    elif event.name == "a":
        print("a", end="")
        userInput.append("a")
    elif event.name == "b":
        print("b", end="")
        userInput.append("b")
    else:
        print(f"\n{event.name}")


keyboard.on_press(on_press)

keyboard.wait('esc')


if userInput == KONAMI_CODE:
    print("\nIngresaste correctamente el código konami")
else:
    print("\nIngresaste incorrectamente el código konami")
