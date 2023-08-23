
import os
from pynput import keyboard



class Piece:
    def __init__(self, piece: list[list[int]], xaxis:int = 0, yaxis:int = 0):
        self.piece = piece
        self.xaxis = xaxis
        self.yaxis = yaxis

def draw_grid(grid):
    """
    Draw grid
    Params: grid (list) of list of int
    """
    for row in grid:
        for item in row:
            if item == 0:
                print("🔲", end=" ")
            else:
                print("🔳", end=" ")
        print()

# config grid


def create_grid(limit=10):
    """
    Create grid
    Params: limit (int) limit of grid
    return: grid (list) of list of int
    """
    grid = []
    for i in range(limit):
        grid.append([0] * 10)
    return grid


# piece l
#  🔳
#  🔳🔳🔳
def create_piece_l():
    """
    Create piece L
    The piece is a dictionary with keys 'piece', 'xaxis', and 'yaxis'
    'piece' is a list of list of 3 values
    'xaxis' is an int of cord x
    'yaxis' is an int of cord y

    return: Piece
    """
    piece = []
    piece.append([1, 0, 0])
    piece.append([1, 1, 1])
    return Piece(piece=piece)

# rotate piece
def rotate_piece(piece: Piece):
    """
    Rotate piece
    Params: piece (list) of list of int
    return: new Piece with piece rotated 90 degrees clockwise
    """
    cord_x = piece.xaxis
    cord_y = piece.yaxis
    piece = piece.piece
    max_size = max_limit_internal_x(piece)
    new_piece = []
    # disable rotate if piece yaxis is max_size 
    if (cord_y + max_size) > main_limit:
        return Piece(piece=piece, xaxis=cord_x, yaxis=cord_y)

    for i in range(max_size):
        new_piece.append([])
        for j in range(len(piece)):
            new_piece[i].append(piece[len(piece)-j-1][i])

    return Piece(piece=new_piece, xaxis=cord_x, yaxis=cord_y)


def move(piece: Piece, action="rotate", limit=10):
    """
    Move piece
    Params: piece (list) of list of int
    Params: action (string) action to move like left, right, down, up
    Params: limit (int) limit of grid
    """
    cord_x = piece.xaxis
    cord_y = piece.yaxis
    piece = piece.piece
    # get max size of element in piece
    internal_max_size_x = max_limit_internal_x(piece)
    internal_max_size_y = max_limit_internal_y(piece)

    # disable move if piece yaxis is max_size
    if (cord_y + internal_max_size_y) > limit - 1:
        return Piece(piece=piece, xaxis=cord_x, yaxis=cord_y)

    # limit edge of grid
    if action == "left" and cord_x > 0:
        cord_x -= 1
    elif action == "right" and (cord_x + internal_max_size_x) < limit:
        cord_x += 1
    elif action == "down" and (cord_y + internal_max_size_y) < limit:
        cord_y += 1
    elif action == "up" and cord_y > 0:
        cord_y -= 1
    if (cord_x < 0):
        cord_x = 0
    if (cord_y < 0):
        cord_y = 0
    


    return Piece(piece=piece, xaxis=cord_x, yaxis=cord_y)


def max_limit_internal_x(piece: list[list[int]]):
    size = 0
    for i in range(len(piece)):
        if len(piece[i]) > size:
            size = len(piece[i])
    return size


def max_limit_internal_y(piece: list[list[int]]):
    return len(piece)


def draw(piece: Piece):
    """ 
    build grid list with values of int 0 or 1
    """
    
    grid = create_grid(limit=main_limit)
    cord_x = piece.xaxis
    cord_y = piece.yaxis
    piece = piece.piece
    for i in range(len(piece)):
        for j in range(len(piece[i])):
            if piece[i][j] == 1:
                position_x = cord_x + j
                position_y = cord_y + i
                grid[position_y][position_x] = 1
    draw_grid(grid)


def key_allowed(key):
    if key == keyboard.Key.left:
        return "left"
    elif key == keyboard.Key.right:
        return "right"
    elif key == keyboard.Key.down:
        return "down"
    elif key == keyboard.Key.up:
        return "up"
    elif key == keyboard.Key.space:
        return "rotate"
    else:
        return None


def clear_console():
    os.system('cls' if os.name == 'nt' else 'clear')


def on_press(key):
    global piece
    try:
        action = key_allowed(key)
        if (action != None):
            if action == "rotate":
                piece = rotate_piece(piece)
            else:
                piece = move(piece, action, main_limit)
            clear_console()
            draw(piece)
    except AttributeError:
        pass


# init game
main_limit = 10
piece = create_piece_l()
clear_console()
draw(piece)

listener = keyboard.Listener(on_press=on_press)
listener.start()
listener.join()
