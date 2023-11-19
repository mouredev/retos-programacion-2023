import keyboard
import threading
import time
import random
import os
from enum import Enum
import copy


COLOURS = ("🟦", "🟥", "🟪", "🟩", "🟧", "🟨")
EMPTY_BOX = "⬜"


class Movement(Enum):
    ''' 
    MOVEMENT
    ---- 
    The class `Movement` is an enumeration that represents different types of movements.
    '''
    DOWN = 0
    RIGHT = 1
    LEFT = 2
    ROTATE = 3


class Board():
    ''' 
    BOARD
    ----
    The `Board` class represents a game board and manages the movement and placement of pieces on the
    board.'''

    BOARD = [[EMPTY_BOX]*10 for _ in range(20)]

    def __init__(self):
        self.boxes = self.BOARD
        self.piece = Piece()

        self.print_board()

    def print_board(self) -> None:
        os.system('cls')
        print('ESC to exit')
        # Hacer una copia temporal del tablero
        temp_board = copy.deepcopy(self.boxes)

        for position in self.piece.shape.position:
            temp_board[position[1]][position[0]] = self.piece.colour

        for row in temp_board:
            print("".join(map(str, row)))

        print('\n')

    def update_board(self):
        for position in self.piece.shape.position:
            self.boxes[position[1]][position[0]] = self.piece.colour

        self.piece.change_piece()

    def move_piece(self, movement: Movement) -> None:
        if movement == Movement.ROTATE:
            self.piece.rotation_state = 0 if self.piece.rotation_state == 3 else self.piece.rotation_state+1

        if self._is_valid_move(movement):
            for box_index, box in enumerate(self.piece.shape.position):
                match movement:
                    case Movement.DOWN:
                        box[1] += 1
                    case Movement.RIGHT:
                        box[0] += 1
                    case Movement.LEFT:
                        box[0] -= 1
                    case Movement.ROTATE:
                        box[0] += self.piece.shape.rotation[self.piece.rotation_state][box_index][0]
                        box[1] += self.piece.shape.rotation[self.piece.rotation_state][box_index][1]
                        self._rotation_control(box)

        self._full_row_control()
        self.print_board()

    # Control functions

    def _is_valid_move(self, movement: Movement) -> bool:
        for box in self.piece.shape.position:
            match movement:
                case Movement.DOWN:
                    if box[1] >= (len(self.boxes)-1) or self.boxes[box[1] + 1][box[0]] != EMPTY_BOX:
                        self.update_board()
                        return False
                case Movement.RIGHT:
                    if box[0] >= (len(self.boxes[0])-1) or self.boxes[box[1]][box[0] + 1] != EMPTY_BOX:
                        return False
                case Movement.LEFT:
                    if box[0] <= 0 or self.boxes[box[1]][box[0] - 1] != EMPTY_BOX:
                        return False

        return True

    def _rotation_control(self, box) -> None:
        if box[0] < 0:
            for item in self.piece.shape.position:
                item[0] += 1

        if box[0] > len(self.boxes[0])-1:
            for item in self.piece.shape.position:
                item[0] -= 1

        if box[1] > len(self.boxes)-1:
            for item in self.piece.shape.position:
                item[1] -= 1

    def _full_row_control(self):
        full_rows = []
        for i, row in enumerate(self.boxes):
            if all(cell != EMPTY_BOX for cell in row):
                full_rows.append(i)

        for row_index in full_rows:
            # Removing the entire row and adding a new empty row at the top
            del self.boxes[row_index]
            self.boxes.insert(0, [EMPTY_BOX] * 10)


class Piece:
    def __init__(self):
        self.colour = COLOURS[random.randint(0, len(COLOURS)-1)]
        self.shape = self._random_shape()
        self.rotation_state = 0

    def _random_shape(self):
        '''The function randomly selects and returns an instance of a shape class from a list of available
        shapes.

        Returns
        -------
            an instance of a randomly selected shape class.

        '''
        # List of available shapes
        pieces = [_JBlock, _IBlock, _LBlock,
                  _SquareBlock, _TBlock, _ZBlock, _SBlock]

        # Selecting random shape class
        selected_piece = random.choice(pieces)

        # Returning and instantiating random shape
        return selected_piece()

    def change_piece(self):
        # Selecting random colour
        self.colour = COLOURS[random.randint(0, len(COLOURS)-1)]
        # Selecting random shape
        self.shape = self._random_shape()
        # Reseting rotation state
        self.rotation_state = 0


class _JBlock:
    '''🟦⬜⬜\n
        🟦🟦🟦\n
        ⬜⬜⬜'''

    def __init__(self):
        self.position = [[0, 0], [0, 1], [1, 1], [2, 1]]
        self.rotation = [[(0, -2), (-1, -1), (0, 0), (1, 1)],
                         [(2, 0), (1, -1), (0, 0), (-1, 1)],
                         [(0, 2), (1, 1), (0, 0), (-1, -1)],
                         [(-2, 0), (-1, 1), (0, 0), (1, -1)]]


class _IBlock:
    '''🟦🟦🟦🟦'''

    def __init__(self):
        self.position = [[0, 1], [1, 1], [2, 1], [3, 1]]
        self.rotation = [[(-1, -2), (0, -1), (1, 0), (2, 1)],
                         [(2, -1), (1, 0), (0, 1), (-1, 2)],
                         [(1, 2), (0, 1), (-1, 0), (-2, -1)],
                         [(-2, 1), (-1, 0), (0, -1), (1, -2)]]


class _LBlock:
    '''⬜⬜🟦 \n
    🟦🟦🟦\n
    ⬜⬜⬜'''

    def __init__(self):
        self.position = [[2, 0], [2, 1], [1, 1], [0, 1]]
        self.rotation = [[(2, 0), (1, 1), (0, 0), (-1, -1)],
                         [(0, 2), (-1, 1), (0, 0), (1, -1)],
                         [(-2, 0), (-1, -1), (0, 0), (1, 1)],
                         [(0, -2), (1, -1), (0, 0), (-1, 1)]]


class _SquareBlock:
    '''🟦🟦\n
    🟦🟦'''

    def __init__(self):
        self.position = [[1, 0], [2, 0], [1, 1], [2, 1]]
        self.rotation = [[(0, 0), (0, 0), (0, 0), (0, 0)],
                         [(0, 0), (0, 0), (0, 0), (0, 0)],
                         [(0, 0), (0, 0), (0, 0), (0, 0)],
                         [(0, 0), (0, 0), (0, 0), (0, 0)]]


class _TBlock:
    '''🟦🟦🟦\n
    ⬜🟦⬜'''

    def __init__(self):
        self.position = [[1, 0], [0, 1], [1, 1], [2, 1]]
        self.rotation = [[(1, -1), (-1, -1), (0, 0), (1, 1)],
                         [(1, 1), (1, -1), (0, 0), (-1, 1)],
                         [(-1, 1), (1, 1), (0, 0), (-1, -1)],
                         [(-1, -1), (-1, 1), (0, 0), (1, -1)]]


class _ZBlock:
    def __init__(self):
        self.position = [[0, 0], [1, 0], [1, 1], [2, 1]]
        self.rotation = [[(0, -2), (1, -1), (0, 0), (1, 1)],
                         [(2, 0), (1, 1), (0, 0), (-1, 1)],
                         [(0, 2), (-1, 1), (0, 0), (-1, -1)],
                         [(-2, 0), (-1, -1), (0, 0), (1, -1)]]


class _SBlock:
    def __init__(self):
        self.position = [[2, 0], [1, 0], [1, 1], [0, 1]]
        self.rotation = [[(2, 0), (1, -1), (0, 0), (-1, -1)],
                         [(0, 2), (1, 1), (0, 0), (1, -1)],
                         [(-2, 0), (-1, 1), (0, 0), (1, 1)],
                         [(0, -2), (-1, -1), (0, 0), (-1, 1)]]


key_mapping = {
    'flecha abajo': Movement.DOWN,
    'down': Movement.DOWN,
    's': Movement.DOWN,
    'flecha derecha': Movement.RIGHT,
    'right': Movement.RIGHT,
    'd': Movement.RIGHT,
    'flecha izquierda': Movement.LEFT,
    'left': Movement.LEFT,
    'a': Movement.LEFT,
    'space': Movement.ROTATE
}


def main():
    '''## Summary
    The `main` function is the entry point of the program. It initializes the game board, prints the initial board, and then enters a loop to handle user input and update the game state until the game is over or the user presses the 'esc' key.

    ## Example Usage
    ```python
    main()
    ```
    ## Code Analysis
    ### Inputs
    - None
    ### Flow
    1. Initialize the game board.
    2. Print the initial board.
    3. Set the initial values for the `key` and `game_over` variables.
    4. Enter a loop that continues until the user presses the 'esc' key or the game is over.
    5. Read the user's keyboard input.
    6. If the input is a key press event, check if it is a valid key for moving the game piece.
    7. If it is a valid key, move the game piece accordingly on the game board.
    8. Check if the game is over by iterating through the first row of the game board and checking if any cell is not empty.
    9. If the game is over, set the `game_over` variable to True to exit the loop.
    ### Outputs
    - None
    '''
    # Initializing the game
    board = Board()

    key = None
    game_over = False

    def auto_fall():
        nonlocal game_over
        while not game_over:
            # Ajusta el intervalo de tiempo según tus preferencias
            time.sleep(1)
            board.move_piece(Movement.DOWN)

    auto_fall_thread = threading.Thread(target=auto_fall)
    auto_fall_thread.start()

    # The Key 'escape' exit the game
    while (key != 'esc' and not game_over):
        listener = keyboard.read_event()

        if listener.event_type == keyboard.KEY_DOWN:
            key = listener.name
            if key in key_mapping:
                board.move_piece(key_mapping[key])

        for cell in board.boxes[0]:
            if cell != EMPTY_BOX:
                game_over = True
                break

    game_over = True
    auto_fall_thread.join()
    print("Game Over")


if __name__ == '__main__':
    main()
