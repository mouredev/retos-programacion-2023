"""```
/*
 * Crea un programa capaz de gestionar una pieza de Tetris.
 * - La pantalla de juego tiene 10 filas y 10 columnas representadas por símbolos 🔲
 * - La pieza de tetris a manejar será la siguiente (si quieres, puedes elegir otra):
 *   🔳
 *   🔳🔳🔳
 * - La pieza aparecerá por primera vez en la parte superior izquierda de la pantalla de juego.
 *   🔳🔲🔲🔲🔲🔲🔲🔲🔲🔲
 *   🔳🔳🔳🔲🔲🔲🔲🔲🔲🔲
 *   🔲🔲🔲🔲🔲🔲🔲🔲🔲🔲
 *   🔲🔲🔲🔲🔲🔲🔲🔲🔲🔲
 *   🔲🔲🔲🔲🔲🔲🔲🔲🔲🔲
 *   🔲🔲🔲🔲🔲🔲🔲🔲🔲🔲
 *   🔲🔲🔲🔲🔲🔲🔲🔲🔲🔲
 *   🔲🔲🔲🔲🔲🔲🔲🔲🔲🔲
 *   🔲🔲🔲🔲🔲🔲🔲🔲🔲🔲
 *   🔲🔲🔲🔲🔲🔲🔲🔲🔲🔲
 * - Debes desarrollar una función capaz de desplazar y rotar la pieza en el tablero,
 *   recibiendo una acción cada vez que se llame, mostrando cómo se visualiza en la pantalla  de juego.
 * - Las acciones que se pueden aplicar a la pieza son: derecha, izquierda, abajo, rotar.
 * - Debes tener en cuenta los límites de la pantalla de juego.
 */"""
import time

from os import system

import random

screen = [
    ["🔳", "🔳", "🔳", "🔳", "🔳", "🔳", "🔳", "🔳", "🔳", "🔳"],
    ["🔳", "🔳", "🔳", "🔳", "🔳", "🔳", "🔳", "🔳", "🔳", "🔳"],
    ["🔳", "🔳", "🔳", "🔳", "🔳", "🔳", "🔳", "🔳", "🔳", "🔳"],
    ["🔳", "🔳", "🔳", "🔳", "🔳", "🔳", "🔳", "🔳", "🔳", "🔳"],
    ["🔳", "🔳", "🔳", "🔳", "🔳", "🔳", "🔳", "🔳", "🔳", "🔳"],
    ["🔳", "🔳", "🔳", "🔳", "🔳", "🔳", "🔳", "🔳", "🔳", "🔳"],
    ["🔳", "🔳", "🔳", "🔳", "🔳", "🔳", "🔳", "🔳", "🔳", "🔳"],
    ["🔳", "🔳", "🔳", "🔳", "🔳", "🔳", "🔳", "🔳", "🔳", "🔳"],
    ["🔳", "🔳", "🔳", "🔳", "🔳", "🔳", "🔳", "🔳", "🔳", "🔳"],
    ["🔳", "🔳", "🔳", "🔳", "🔳", "🔳", "🔳", "🔳", "🔳", "🔳"],
    ["🔳", "🔳", "🔳", "🔳", "🔳", "🔳", "🔳", "🔳", "🔳", "🔳"],
    ["🔳", "🔳", "🔳", "🔳", "🔳", "🔳", "🔳", "🔳", "🔳", "🔳"],
    ["🔳", "🔳", "🔳", "🔳", "🔳", "🔳", "🔳", "🔳", "🔳", "🔳"],
    ["🔳", "🔳", "🔳", "🔳", "🔳", "🔳", "🔳", "🔳", "🔳", "🔳"],
    ["🔳", "🔳", "🔳", "🔳", "🔳", "🔳", "🔳", "🔳", "🔳", "🔳"],
    ["🔳", "🔳", "🔳", "🔳", "🔳", "🔳", "🔳", "🔳", "🔳", "🔳"],  
]
cube = {"shape":[(0,0),(0,1),(1,0),(1,1)],"rotation_left": False,"rotation_right": False}
stick = {"shape":[(0,0),(0,1),(0,2),(0,3)],"rotation_left": False,"rotation_right": False}
hat = {"shape":[(0,1),(1,0),(1,1),(1,2)],"rotation_left": False,"rotation_right": False}
left_shoe = {"shape":[(0,0),(1,0),(1,1),(1,2)],"rotation_left": False,"rotation_right": False}
right_shoe = {"shape":[(0,2),(1,0),(1,1),(1,2)],"rotation_left": False,"rotation_right": False}
left_corner = {"shape":[(0,0),(0,1),(1,1),(1,2)],"rotation_left": False,"rotation_right": False}
right_corner = {"shape":[(0,1),(0,2),(1,0),(1,1)],"rotation_left": False,"rotation_right": False}
pieces = [
    cube,stick,hat,left_shoe,right_shoe,left_corner,right_corner
]
piece_blocked = False
position_piece = []

def print_screen():
    global screen
    for row in screen:
        print("".join(row))
def print_piece():
    global screen
    global pieces
    global piece_blocked
    global position_piece
    piece = random.choice(pieces)
    for element in piece["shape"]:
        screen[element[0]][element[1]+3] = "🔲"
        position_piece.append((element[0],element[1]+3))
    piece_blocked = 0
def fall_piece():
    global screen
    global position_piece
    global piece_blocked
    old_position = position_piece
    new_position = []
    for element in old_position:
        if element[0] <= 15:
            screen[element[0]][element[1]] = "🔳"
            new_position.append((element[0]+1,element[1]))
        else:
            piece_blocked = True
    for element in new_position:
        if element[0] <= 15:
            screen[element[0]][element[1]] = "🔲"
    
    position_piece = new_position
    
def game():
    timer = 0
    timer_max = 100
    game_score = 0
    game_over = False
    global piece_blocked
    print_piece()
    while timer <= timer_max and game_over == False:
        system("clear")
        print(f"Time Remaining: {timer_max-timer} Segs\n")
        print(f"Game Score: {game_score} points\n")
        print_screen()
        fall_piece()
        time.sleep(1)
        if piece_blocked == True:
            print_piece()
        timer += 1

    print(f"\nGame Over, Final Score: {game_score}")

if __name__ == "__main__":

    game()
