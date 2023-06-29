import keyboard

# Código Konami a detectar
konami_code = ['up', 'up', 'down', 'down', 'left', 'right', 'left', 'right', 'b', 'a']

# Lista para almacenar las teclas ingresadas por el usuario
user_input = []

# Función para verificar si se ingresó el Código Konami
def check_konami_code():
    if user_input == konami_code:
        print("¡Código Konami detectado!")

# Función para manejar las teclas presionadas
def on_key_press(event):
    key = event.name.lower()

    # Agregar la tecla a la lista de entrada del usuario
    user_input.append(key)

    # Verificar si se ingresó el Código Konami
    check_konami_code()

    # Limitar la lista de entrada del usuario al tamaño del Código Konami
    user_input[:] = user_input[-len(konami_code):]

# Registrar el manejador de eventos para las teclas presionadas
keyboard.on_press(on_key_press)

# Mantener el programa en ejecución
keyboard.wait()