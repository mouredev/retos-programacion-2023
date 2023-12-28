
'''
 Crea un programa que detecte cuando el famoso "Código Konami" se ha introducido correctamente
 desde el teclado. Si sucede esto, debe notificarse mostrando un mensaje en la terminal.
'''

import keyboard

keys = {'FLECHA ARRIBA':    '⬆',
        'FLECHA ABAJO':     '⬇',
        'FLECHA IZQUIERDA': '⬅',
        'FLECHA DERECHA':   '➡',
        'A':                '🅰',
        'B':                '🅱'}

konami_code = ['⬆', '⬆', '⬇', '⬇', '⬅', '➡', '⬅', '➡', '🅱', '🅰']

position = 0

def on_key_press(e):
    global position
    if e.name.upper() in keys:
        print(keys[e.name.upper()])
        if konami_code[position] == keys[e.name.upper()]:
            position += 1
        else:
            position = 0
        
        if position == len(konami_code):
            print("✔ KONAMI ✔")
            position = 0
    
keyboard.on_press(on_key_press)

keyboard.wait("esc")