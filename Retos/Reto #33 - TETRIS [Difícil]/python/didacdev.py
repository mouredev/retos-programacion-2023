from enum import Enum
import keyboard

ARROWS = ['up', 'down', 'left', 'right']


# 10x10 board
board = [['🔲' for x in range(10)] for y in range(10)]


class ChipStates(Enum):
    LEFT = 0
    UP = 1
    RIGHT = 2
    DOWN = 3


class ChipPositions(Enum):
    # Initial position
    LEFT = [(0, 0), (1, 0), (1, 1), (1, 2)]
    UP = [(0, 1), (0, 0), (1, 0), (2, 0)]
    RIGHT = [(1, 2), (0, 2), (0, 1), (0, 0)]
    DOWN = [(2, 0), (2, 1), (1, 1), (0, 1)]


class Chip:
    # Initial position
    # It is possible to use any of the 4 positions
    chip_position = ChipPositions.LEFT.value
    # Initial state
    # It is possible to use any of the 4 states, but it must be the same as the initial position
    chip_state = ChipStates.LEFT


# Initial chip
chip = Chip()


# -------------------------------------------------------------------------------------#
# ------------------------------------  Functions  ------------------------------------#
# -------------------------------------------------------------------------------------#

# ------------------ Board ------------------
def add_chip(chip_position):
    for position in chip_position:
        board[position[0]][position[1]] = '🔳'


def clean_board():
    for position in chip.chip_position:
        board[position[0]][position[1]] = '🔲'

# ------------------ Moves ------------------


def move_down():
    for i in range(len(chip.chip_position)):
        chip.chip_position[i] = (chip.chip_position[i]
                                 [0] + 1, chip.chip_position[i][1])


def move_left():
    for i in range(len(chip.chip_position)):
        if is_left_move_valid():
            chip.chip_position[i] = (chip.chip_position[i]
                                     [0], chip.chip_position[i][1] - 1)


def move_right():
    for i in range(len(chip.chip_position)):
        if is_right_move_valid():
            chip.chip_position[i] = (chip.chip_position[i]
                                     [0], chip.chip_position[i][1] + 1)


def change_state():
    match chip.chip_state:
        case ChipStates.LEFT:
            chip.chip_state = ChipStates.UP
            chip.chip_position = [(chip.chip_position[0][0], chip.chip_position[0][1] + 1), (chip.chip_position[1][0] - 1, chip.chip_position[1][1]),
                                  (chip.chip_position[2][0], chip.chip_position[2][1] - 1), (chip.chip_position[3][0] + 1, chip.chip_position[3][1] - 2)]
        case ChipStates.UP:
            chip.chip_state = ChipStates.RIGHT
            chip.chip_position = [(chip.chip_position[0][0] + 1, chip.chip_position[0][1] + 1), (chip.chip_position[1][0], chip.chip_position[1][1] + 2),
                                  (chip.chip_position[2][0] - 1, chip.chip_position[2][1] + 1), (chip.chip_position[3][0] - 2, chip.chip_position[3][1])]
        case ChipStates.RIGHT:
            chip.chip_state = ChipStates.DOWN
            chip.chip_position = [(chip.chip_position[0][0] + 1, chip.chip_position[0][1] - 2), (chip.chip_position[1][0] + 2, chip.chip_position[1][1] - 1),
                                  (chip.chip_position[2][0] + 1, chip.chip_position[2][1]), (chip.chip_position[3][0], chip.chip_position[3][1] + 1)]
        case ChipStates.DOWN:
            chip.chip_state = ChipStates.LEFT
            chip.chip_position = [(chip.chip_position[0][0] - 2, chip.chip_position[0][1]), (chip.chip_position[1][0] - 1, chip.chip_position[1][1] - 1),
                                  (chip.chip_position[2][0], chip.chip_position[2][1]), (chip.chip_position[3][0] + 1, chip.chip_position[3][1] + 1)]

# ------------------ Validations ------------------


def is_finished():
    for position in chip.chip_position:
        if position[0] == 9:
            return True
    return False


def is_right_move_valid():
    for position in chip.chip_position:
        if position[1] == 9:
            return False
    return True


def is_left_move_valid():
    for position in chip.chip_position:
        if position[1] == 0:
            return False
    return True

# ------------------ Game ------------------


def start_game():
    add_chip(chip.chip_position)

    for i in range(10):
        row = ""
        for j in range(10):
            row += board[i][j]
        print(row)


# -------------------------------------------------------------------------------------#
# ------------------------------------  Main  -----------------------------------------#
# -------------------------------------------------------------------------------------#


def main():

    start_game()

    while not is_finished():
        key_event = keyboard.read_event()
        key = key_event.name
        event_type = key_event.event_type

        print()

        if event_type == keyboard.KEY_DOWN:  # Solo manejar eventos de tecla presionada

            if key in ARROWS:
                clean_board()
                if 'up' in key:
                    change_state()
                elif 'down' in key:
                    move_down()
                elif 'left' in key:
                    move_left()
                elif 'right' in key:
                    move_right()

            add_chip(chip.chip_position)

            for i in range(10):
                row = ""
                for j in range(10):
                    row += board[i][j]
                print(row)

    print()
    print("#---------------#")
    print("# Game finished #")
    print("#---------------#")


if __name__ == "__main__":
    main()
