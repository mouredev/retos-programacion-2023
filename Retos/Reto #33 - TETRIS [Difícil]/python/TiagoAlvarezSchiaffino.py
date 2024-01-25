from enum import Enum
import keyboard

class Movement(Enum):
    DOWN = 1
    RIGHT = 2
    LEFT = 3
    ROTATE = 4

def tetris():
    """
    Tetris game management function.
    """
    screen = [["🔳", "🔲", "🔲", "🔲", "🔲", "🔲", "🔲", "🔲", "🔲", "🔲"],
              ["🔳", "🔳", "🔳", "🔲", "🔲", "🔲", "🔲", "🔲", "🔲", "🔲"],
              ["🔲", "🔲", "🔲", "🔲", "🔲", "🔲", "🔲", "🔲", "🔲", "🔲"],
              ["🔲", "🔲", "🔲", "🔲", "🔲", "🔲", "🔲", "🔲", "🔲", "🔲"],
              ["🔲", "🔲", "🔲", "🔲", "🔲", "🔲", "🔲", "🔲", "🔲", "🔲"],
              ["🔲", "🔲", "🔲", "🔲", "🔲", "🔲", "🔲", "🔲", "🔲", "🔲"],
              ["🔲", "🔲", "🔲", "🔲", "🔲", "🔲", "🔲", "🔲", "🔲", "🔲"],
              ["🔲", "🔲", "🔲", "🔲", "🔲", "🔲", "🔲", "🔲", "🔲", "🔲"],
              ["🔲", "🔲", "🔲", "🔲", "🔲", "🔲", "🔲", "🔲", "🔲", "🔲"],
              ["🔲", "🔲", "🔲", "🔲", "🔲", "🔲", "🔲", "🔲", "🔲", "🔲"]]

    print_screen(screen)

    rotation = 0

    while True:
        event = keyboard.read_event()

        if event.name == "esc":
            break
        elif event.event_type == keyboard.KEY_DOWN:
            if event.name == "down":
                (screen, rotation) = move_piece(screen, Movement.DOWN, rotation)
            elif event.name == "right":
                (screen, rotation) = move_piece(screen, Movement.RIGHT, rotation)
            elif event.name == "left":
                (screen, rotation) = move_piece(screen, Movement.LEFT, rotation)
            elif event.name == "space":
                (screen, rotation) = move_piece(screen, Movement.ROTATE, rotation)

def move_piece(screen: list, movement: Movement, rotation: int) -> (list, int):
    """
    Move and rotate the Tetris piece on the board.

    Args:
        screen (list): Current game screen.
        movement (Movement): Movement action (DOWN, RIGHT, LEFT, ROTATE).
        rotation (int): Current rotation state.

    Returns:
        tuple: Updated game screen and rotation state.
    """
    new_screen = [["🔲"] * 10 for _ in range(10)]

    rotation_item = 0
    rotations = [[(1, 1), (0, 0), (-2, 0), (-1, -1)],
                 [(0, 1), (-1, 0), (0, -1), (1, -2)],
                 [(0, 2), (1, 1), (-1, 1), (-2, 0)],
                 [(0, 1), (1, 0), (2, -1), (1, -2)]]

    new_rotation = rotation
    if movement is Movement.ROTATE:
        new_rotation = 0 if rotation == 3 else rotation + 1

    for row_index, row in enumerate(screen):
        for column_index, item in enumerate(row):
            if item == "🔳":
                new_row_index, new_column_index = 0, 0

                if movement is Movement.DOWN:
                    new_row_index = row_index + 1
                    new_column_index = column_index
                elif movement is Movement.RIGHT:
                    new_row_index = row_index
                    new_column_index = column_index + 1
                elif movement is Movement.LEFT:
                    new_row_index = row_index
                    new_column_index = column_index - 1
                elif movement is Movement.ROTATE:
                    new_row_index = row_index + rotations[new_rotation][rotation_item][0]
                    new_column_index = column_index + rotations[new_rotation][rotation_item][1]
                    rotation_item += 1

                if new_row_index > 9 or new_column_index > 9 or new_column_index < 0:
                    print("\nCannot perform the movement")
                    return (screen, rotation)
                else:
                    new_screen[new_row_index][new_column_index] = "🔳"

    print_screen(new_screen)

    return (new_screen, new_rotation)

def print_screen(screen: list):
    """
    Print the game screen.

    Args:
        screen (list): Current game screen.
    """
    print("\nTetris Screen:\n")
    for row in screen:
        print("".join(map(str, row)))

tetris()
