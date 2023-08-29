import random

def create_piece():
    figures = [
        [
            [1, 1],
            [1, 1]
        ],
        [
            [1, 1, 1, 1]
        ],
        [
            [1, 1, 1],
            [0, 0, 1]
        ],
        [
            [1, 1, 1],
            [1, 0, 0]
        ],
        [
            [1, 0, 0],
            [1, 1, 1]
        ],
        [
            [0, 1, 0],
            [1, 1, 1]
        ],
        [
            [1, 1, 0],
            [0, 1, 1]
        ]
    ]
    return random.choice(figures)

def rotate(piece):
    return list(zip(*piece[::-1]))

def move_left(row, col):
    return row, max(col - 1, 0)

def move_right(row, col, piece_width):
    return row, min(col + 1, 10 - piece_width)

def move_down(row, col, piece_height):
    return min(row + 1, 10 - piece_height), col

def show(piece, row, col):
    for r in range(10):
        symbols = [
            "🔳" if 0 <= r - row < len(piece) and 0 <= c - col < len(piece[0]) and piece[r - row][c - col] == 1 else "🔲"
            for c in range(10)
        ]
        print(''.join(symbols))



def validate_position(func):
    def wrapper(row, col, piece_height, piece_width):
        new_row, new_col = func(row, col, piece_height, piece_width)
        if 0 <= new_row < 10 - piece_height + 1 and 0 <= new_col < 10 - piece_width + 1:
            return new_row, new_col
        else:
            print("Movimiento no válido.")
            return row, col
    return wrapper

@validate_position
def move_left(row, col, piece_height, piece_width):
    return row, max(col - 1, 0)

@validate_position
def move_right(row, col, piece_height, piece_width):
    return row, min(col + 1, 10 - piece_width)

@validate_position
def move_down(row, col, piece_height, piece_width):
    return min(row + 1, 10 - piece_height), col

def play():
    piece = create_piece()
    row = 0
    col = 0
    piece_height = len(piece)
    piece_width = len(piece[0])

    show(piece, row, col)

    while True:
        action = input("Ingrese (izquierda, derecha, abajo, rotar): ")

        if action == "izquierda":
            row, col = move_left(row, col, piece_height, piece_width)
        elif action == "derecha":
            row, col = move_right(row, col, piece_height, piece_width)
        elif action == "abajo":
            row, col = move_down(row, col, piece_height, piece_width)
        elif action == "rotar":
            piece = rotate(piece)
            piece_height = len(piece)
            piece_width = len(piece[0])
        else:
            print("Intente de nuevo.")
            continue

        show(piece, row, col)

if __name__ == "__main__":
    play()
