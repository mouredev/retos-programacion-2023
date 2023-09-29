def create_board(num_row, num_col):
    
    board = list()

    for row in range(0, num_row):
        board.append([])
        for col in range(0, num_col):
            board[row].append("🔲")

    return board


def display_board(board: list):
    
    for row in board:
        for element in row:
            print(element, end="")
        print("")


def rotate_shape(shape: list):
    
    buffer = list()

    row_size = len(shape)
    col_size = len(shape[0])

    for i in range(0, col_size):
        buffer.append([])
        for j in range(0, row_size):
            buffer[i].append(shape[row_size - 1 - j][i])

    return buffer


def display_shape(shape: list):
    
    row_size = len(shape)
    col_size = len(shape[0])

    for i in range(0, row_size):
        for j in range(0, col_size):
            print(shape[i][j], end="")
        print("")


def insert_shape(position, shape: list, board: list):
    
    row_size = len(shape)
    col_size = len(shape[0])

    posx = position[0]
    posy = position[1]

    for row in range(0, row_size):
        board[posy + row][posx : posx + col_size] = shape[row]


def erase_shape(position, shape: list, board: list):
    
    row_size = len(shape)
    col_size = len(shape[0])

    posx = position[0]
    posy = position[1]

    for row in range(0, row_size):
        for col in range(0, col_size):
            board[posy + row][posx + col] = "🔲"


def move_shape(current_position,previous_position, action, shape, board):
    
    posx = current_position[0]
    posy = current_position[1]

    erase_shape(previous_position, shape, tetris_board)

    rotated_shape = shape

    if action == "top":
        posy -= 1
    elif action == "bottom":
        posy += 1
    elif action == "left":
        posx -= 1
    elif action == "right":
        posx += 1
    elif action == "rotate":
        rotated_shape = rotate_shape(shape)

    shape_row_size = len(rotated_shape)
    shape_col_size = len(rotated_shape[0])

    board_row_size = len(board)
    board_col_size = len(board[0])

    limit = False

    if posx >= 0 and (board_col_size - posx) >= shape_col_size:
        current_position[0] = posx
    else:
        limit = True
        print("⚠️  Limite en x")

    if posy >= 0 and (board_row_size - posy) >= shape_row_size:
        current_position[1] = posy
    else:
        limit = True
        print("⚠️  Limite en y")

    if limit != True:
        shape = rotated_shape

    insert_shape(current_position, shape, board)

    return shape


tetris_board = create_board(10, 10)

shape1 = [["🔳", "🔲", "🔲"], ["🔳", "🔳", "🔳"]]

shape2 = [["🔳", "🔲"], ["🔳", "🔳"]]

shape3 = [["🔳", "🔳", "🔲"], ["🔲", "🔳", "🔳"]]


shape_selected = shape1
current_position = [0, 0]
previous_position = [0, 0]

action_keys = {"w": "top", 
               "s": "bottom", 
               "a": "left", 
               "d": "right", 
               "r": "rotate",
               "q":"exit"}

action = ''

while action != "exit":

    shape_selected = move_shape(
        current_position,
        previous_position,
        action,
        shape_selected,
        tetris_board,
    )

    
    display_board(tetris_board)
    print(current_position)
    
    print("🕹  Para ejecutar una acción --> Presiona la tecla que se indica entre corchetes seguido de la tecla enter.")
    input_key = input("[w] Arriba\n[s] Abajo\n[a] Izquierda\n[d] Derecha\n[r] Rotar\n[q] Salir\n")
    
    try:
        action = action_keys[input_key]
    except KeyError:
        print("🚫 Tecla Incorrecta")
        action = ''

    previous_position = current_position.copy()
