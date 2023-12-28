from pynput.keyboard import Key, KeyCode, Listener

codeKonami = [Key.up, Key.up, Key.down, Key.down, Key.left, Key.right,
            Key.left, Key.right, KeyCode.from_char("b"), KeyCode.from_char("a")]
codePress = []

def codeGenerated(key):
    if Key.esc == key:
        print("Código incorrecto")
        return False
    else:
        codePress.append(key)
        if codeKonami == codePress:
            print("Código Konami encontrado")
            return False

if __name__ == "__main__":
    print("Ingrese codigo: ")

    codigo = Listener(codeGenerated)
    codigo.start()
    codigo.join()