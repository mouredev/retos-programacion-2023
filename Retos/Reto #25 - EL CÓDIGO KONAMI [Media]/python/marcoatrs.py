import keyboard

konami_code = ["up", "up", "down", "down", "left", "right", "left", "right", "b", "a"]

code = []


def on_press(event: keyboard.KeyboardEvent):
    code.append(event.name)
    if konami_code == code:
        print("Konami Code :)")
        code.clear()
    else:
        if code == konami_code[: len(code)]:
            return
        code.clear()


keyboard.on_press(on_press)

while True:
    pass
