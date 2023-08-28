'''
Crea un programa capaz de gestionar una pieza de Tetris.
- La pantalla de juego tiene 10 filas y 10 columnas representadas por símbolos 🔲
- La pieza de tetris a manejar será la siguiente (si quieres, puedes elegir otra):
  🔳
  🔳🔳🔳
- La pieza aparecerá por primera vez en la parte superior izquierda de la pantalla de juego.
  🔳🔲🔲🔲🔲🔲🔲🔲🔲🔲
  🔳🔳🔳🔲🔲🔲🔲🔲🔲🔲
  🔲🔲🔲🔲🔲🔲🔲🔲🔲🔲
  🔲🔲🔲🔲🔲🔲🔲🔲🔲🔲
  🔲🔲🔲🔲🔲🔲🔲🔲🔲🔲
  🔲🔲🔲🔲🔲🔲🔲🔲🔲🔲
  🔲🔲🔲🔲🔲🔲🔲🔲🔲🔲
  🔲🔲🔲🔲🔲🔲🔲🔲🔲🔲
  🔲🔲🔲🔲🔲🔲🔲🔲🔲🔲
  🔲🔲🔲🔲🔲🔲🔲🔲🔲🔲
- Debes desarrollar una función capaz de desplazar y rotar la pieza en el tablero,
  recibiendo una acción cada vez que se llame, mostrando cómo se visualiza en la pantalla  de juego.
- Las acciones que se pueden aplicar a la pieza son: derecha, izquierda, abajo, rotar.
- Debes tener en cuenta los límites de la pantalla de juego.
'''
import keyboard

columns = 10 # number of board columns
rows = 10 # number of board rows
pieces = [ # possible pieces
    [
        [
            ['🔳','🔲','🔲'],
            ['🔳','🔳','🔳']
        ],[
            ['🔳','🔳'],
            ['🔳','🔲'],
            ['🔳','🔲']
        ],[
            ['🔳','🔳','🔳'],
            ['🔲','🔲','🔳']
        ],[
            ['🔲','🔳'],
            ['🔲','🔳'],
            ['🔳','🔳']
        ]
    ]
    # more pieces can fit here
]

def tetris():
    piece = pieces[0] # piece in current rotation
    position = [0, 0] # position of piece in screen
    rotation = 0 # rotation of the pieces: 0, 1, 2 or 3
    screen = generate_empty_screen() # here we have the screen of the game
    
    screen = draw_piece(screen, piece[rotation], position)
    print_screen(screen)
    
    while True:
        event = keyboard.read_event()
        if event.event_type == keyboard.KEY_DOWN:
            key = event.name
            
            if key == 'flecha abajo':
                print('DOWN')
                if position[0] + len(piece[rotation]) < rows:
                    position[0] += 1
            elif key == 'flecha izquierda':
                print('LEFT')
                if position[1] > 0:
                    position[1] -= 1
            elif key == 'flecha derecha':
                print('RIGHT')
                if position[1] + len(piece[rotation][0]) < columns:
                    position[1] += 1
            elif key == 'flecha arriba':
                print('ROTATE')
                if position[0] + len(piece[rotation][0]) <= rows and position[1] + len(piece[rotation]) <= columns: # can fit rotated piece in current position
                    rotation = 0 if rotation == 3 else rotation + 1
            elif key == 'esc':
                print('EXIT')
                break
            
            if key == 'flecha abajo' or key == 'flecha izquierda' or key == 'flecha derecha' or key == 'flecha arriba':
                screen = draw_piece(screen, piece[rotation], position)
                print_screen(screen)
                pass

def draw_piece(screen, piece, position):
    screen = generate_empty_screen()
    for i in range(len(piece)):
        for j in range(len(piece[0])):
            screen[position[0] + i][position[1] + j] = piece[i][j]
    return screen
    
def generate_empty_screen():
    return [['🔲' for _ in range(columns)] for _ in range(rows)]
    
def print_screen(screen):
    for row in screen:
        print(''.join(row))
    
tetris() # start game