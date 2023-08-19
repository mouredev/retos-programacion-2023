"""
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
 *
 *
 * Autor: Víctor Andrés
 * Fecha: 18-8-2023
 * Instrucciones: Instala la libreria pynput
 * Mueve la pieza con las flechas y rotla con la tecla de espacio
 * Para salir de la aplicación utiliza la tecla Ctrl
 """
import os
from pynput.keyboard import Key, Listener

def show_screen(screen, piece):   
    screen = initial_screen()
    screen = set_piece(screen, piece)
    print_screen(screen)

def initial_screen()->[]:
    val = [0] * 10
    for x in range (10):
        val[x] = ["🔲"] * 10
    return val

def set_piece(screen, piece)->[]:
    for element in list(piece):
        screen[element[0]][element[1]] = "🔳"
    return screen

def check_grid(piece, x, y):
    aux = list(piece)
    for element in list(piece):
         if (element[0] in list(range(x,(x+3)))) and (element[1] in list(range(y,(y+3)))):
            aux.remove(element)
    return len(aux)==0               

def get_x_y_from_grid(piece):
    for x in range(0,8):
        for y in range(0,8):
            if check_grid(piece, x, y):
                return x, y
    return 0, 0 

def translate_to_matrix(piece, x, y)->[]:
    val = [0] * 3
    for k in range(3):
        val[k] = [0] * 3

    for element in list(piece):
        val[element[0]-x][element[1]-y] = 1
    return val

def rotate90(matrix)->[]:
    val = [[0,0,0],[0,0,0],[0,0,0]]
    for i in range(3):
        for j in range(3):
            val[i][j] = matrix[2-j][i]
    return val

def translate_to_piece(matrix, x, y)->[]:
    val = []
    for i in range(0,3):
        for j in range(0,3):
            if matrix[i][j] == 1:
                val.append([(i+x), (j+y)])
    return val

def rotate(piece)->[]:
    x,y =get_x_y_from_grid(piece)


def up(piece)->[]:
    aux = list(piece)
    for element in list(piece):        
        if(element[0]==0):
            return piece

    for element in aux:
            element[0] = element[0] - 1 
    return aux

def down(piece)->[]:
    aux =list(piece)
    for element in list(piece):        
        if(element[0]==9):
            return piece

    for element in aux:
            element[0] = element[0] + 1        
    return aux

def left(piece)->[]:
    aux =list(piece)
    for element in list(piece):        
        if(element[1]==0):
            return piece

    for element in aux:
            element[1] = element[1] - 1        
    return aux


def right(piece)->[]:
    aux =list(piece)
    for element in list(piece):        
        if(element[1]==9):
            return piece

    for element in aux:
        element[1] = element[1] + 1        
    return aux
 
     
def print_screen(screen):
    os.system("clear")
    print("Mueve las pieza con el cursor o rotala con la tecla espacio")
    print("Para salir del programa pulsa la tecla 'ctrl'")
    print()
    for row  in range(0, 10):
        for col in range(0,10):
            print(screen[row][col], end="")
        print()
      
def on_press(key):
    global piece
    global screen

    if key is Key.down:
        piece = down(piece)
        show_screen(screen, piece)
    elif key is Key.up:
        piece = up(piece)
        show_screen(screen, piece)
    elif key is Key.left:
        piece = left(piece)
        show_screen(screen, piece)
    elif key is Key.right:
        piece = right(piece)
        show_screen(screen, piece)
    elif key is Key.space:
        x, y = get_x_y_from_grid(piece)
        matrix = translate_to_matrix(piece, x, y)
        matrix = rotate90(matrix)
        piece = translate_to_piece(matrix, x, y)
        show_screen(screen, piece)
    elif key is Key.ctrl:
        global end 
        end = True                                                
                         

listener = Listener(on_press=on_press)
listener.start()

end = False
screen = initial_screen()
piece = [[8,7],[9,7],[9,8],[9,9]]
show_screen(screen, piece)

while not end:
    pass
