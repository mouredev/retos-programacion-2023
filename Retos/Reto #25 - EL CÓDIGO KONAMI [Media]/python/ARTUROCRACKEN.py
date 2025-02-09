"""
 * Crea un programa que detecte cuando el famoso "Código Konami" se ha introducido correctamente
 * desde el teclado. Si sucede esto, debe notificarse mostrando un mensaje en la terminal.
"""

import keyboard

# Secuencia del Código Konami
KONAMI_CODE = [
    'up', 'up', 'down', 'down',
    'left', 'right', 'left', 'right',
    'b', 'a'
]

# Variables para trackear el progreso de la secuencia
key_position = 0
last_key = None

def detect_konami_code():
    global key_position, last_key

    print("Ingresa el codigo konami: ")
    # Bucle infinito para escuchar las teclas presionadas
    while True:
        event = keyboard.read_event()  # Escuchar el siguiente evento de teclado
        
        if event.event_type == keyboard.KEY_DOWN:  # Solo procesamos cuando una tecla es presionada
            key = event.name  # Nombre de la tecla presionada

            # Si se presiona 'esc', terminamos el programa
            if key == 'esc':
                print("Programa terminado.")
                break

            # Si la tecla presionada es la correcta según la secuencia
            if key == KONAMI_CODE[key_position]:
                key_position += 1
                print(f"Secuencia actual: {key_position}/{len(KONAMI_CODE)}. Tecla '{key}' detectada.")
            # Si presionamos la primera tecla correctamente después de un error
            elif key == KONAMI_CODE[0]:
                if last_key == KONAMI_CODE[0]:
                    # Si la primera tecla se presiona varias veces, reiniciamos la secuencia con la tercera tecla
                    key_position = 2
                else:
                    key_position = 1
            else:
                key_position = 0

            # Si hemos completado la secuencia, mostramos un mensaje
            if key_position == len(KONAMI_CODE):
                print("""
                \n
                ╦╔═╔═╗╔╗╔╔═╗╔╦╗╦  ╔═╗╔═╗╔╦╗╔═╗
                ╠╩╗║ ║║║║╠═╣║║║║  ║  ║ ║ ║║║╣ 
                ╩ ╩╚═╝╝╚╝╩ ╩╩ ╩╩  ╚═╝╚═╝═╩╝╚═╝
                \n
                """)
                break

            # Actualizamos la última tecla presionada
            last_key = key


detect_konami_code()
