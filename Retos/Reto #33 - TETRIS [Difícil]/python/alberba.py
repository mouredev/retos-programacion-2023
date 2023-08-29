import keyboard
import time

piece_coords = [[0, 0], [0, 1], [1, 1], [2, 1]]

def print_table(piece_coords):
    for y in range(10):
        row = ""
        for x in range(10):
            if [x, y] in piece_coords:
                row += "🔳"
            else:
                row += "🔲"
        print(row)
    print()
    
def game():
    piece_coords = [[0, 0], [0, 1], [1, 1], [2, 1]]
    print_table(piece_coords)
    
    max_y = max(coord[1] for coord in piece_coords)
    while max_y < 9:
        if keyboard.is_pressed("down"):
            print("hola")
            piece_coords = move_down(piece_coords)
            print_table(piece_coords)
            time.sleep(0.1)
        if keyboard.is_pressed("right"):
            piece_coords = move_right(piece_coords)
            print_table(piece_coords)
            time.sleep(0.1)
        if keyboard.is_pressed("left"):
            piece_coords = move_left(piece_coords)
            print_table(piece_coords)
            time.sleep(0.1)
        max_y = max(coord[1] for coord in piece_coords)
        

def move_down(piece_coords: list[list]) -> list:
    return list(map(lambda x: [x[0], x[1] + 1], piece_coords))

def move_right(piece_coords) -> list:
    if max(coord[0] for coord in piece_coords) < 9:
        return list(map(lambda x: [x[0] + 1, x[1]], piece_coords))
    else:
        return piece_coords

def move_left(piece_coords) -> list:
    if min(coord[0] for coord in piece_coords) > 0:
        return list(map(lambda x: [x[0] - 1, x[1]], piece_coords))
    else:
        return piece_coords
game()
