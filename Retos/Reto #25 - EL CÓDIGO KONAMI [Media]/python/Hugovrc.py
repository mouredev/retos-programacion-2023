from pynput.keyboard import Key, KeyCode, Listener

codigo_ingresado = []
codigo_konami = [Key.up, Key.up, Key.down, Key.down, Key.left, Key.right, Key.left, Key.right, KeyCode.from_char("b"), KeyCode.from_char("a")]

def pulsa(tecla):
    
    codigo_ingresado.append(tecla)
    if tecla == Key.esc:
        return False
    elif codigo_ingresado == codigo_konami:
        print("Codigo introducido correctamente!!!")
        listener.stop()
listener = Listener(pulsa)

listener.start()

listener.join()