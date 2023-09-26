"""/*
 * Crea un programa que detecte cuando el famoso "Código Konami" se ha introducido correctamente
 * desde el teclado. Si sucede esto, debe notificarse mostrando un mensaje en la terminal.
 */
"""
import keyboard

konami_code = ["up", "up", "down", "down", "left", "right", "left", "right", "b", "a"]
sequence = 0


def check_sequence(e):
    global sequence
    if e.name in konami_code[sequence]:
        print("\nVas Bien sigue asi:")
        sequence += 1
        if sequence == len(konami_code):
            print("Konami Code!")
            sequence = 0
    else:
        sequence = 0


keyboard.on_press(check_sequence)
keyboard.wait("esc")
