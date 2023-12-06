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
 *   recibiendo una acción cada vez que se llame, mostrando cómo se visualiza en la pantalla de juego.
 * - Las acciones que se pueden aplicar a la pieza son: derecha, izquierda, abajo, rotar.
 * - Debes tener en cuenta los límites de la pantalla de juego.
"""

from pynput.keyboard import Key, Listener, KeyCode

class Tetris:
    def __init__(self, rows, cols):
        # Board settings
        self.rows = rows
        self.cols = cols

        # Piece's information
        self.piece = [
            [1, 0, 0],
            [1, 1, 1],
        ]
        self.piece_width = len(self.piece[0])
        self.piece_height = len(self.piece)

        # Piece's position
        self.x = 0
        self.y = 0


    def print_options(self):
        print("\nEnter an option:")
        print(" - A: Move left")
        print(" - D: Move right")
        print(" - S: Move down")
        print(" - W: Rotate piece")
        print(" - ESC: Exit\n")


    def print_board(self):
        self.board = [[0 for col in range(self.cols)] for row in range(self.rows)]
        
        def create_board():
            # Initialize the board
            for i in range(len(self.board)):
                for j in range(len(self.board[i])):
                    if self.board[i][j] == 0:
                        self.board[i][j] = '🔲'

            # Print the piece
            for i in range(len(self.piece)):
                for j in range(len(self.piece[i])):
                    if self.piece[i][j] == 1:
                        self.board[self.y+i][self.x+j] = '🔳'

        create_board()

        for i in range(len(self.board)):
            print("".join(self.board[i]))

    # Piece's movements

    def move_left(self):
        can_move = self.x - 1 >= 0
        
        if can_move: self.x -= 1
        else: print("You've reached left limit.")


    def move_right(self):
        can_move = self.x + 1 + self.piece_width <= self.cols
    
        if can_move: self.x += 1
        else: print("You've reached rigth limit.")


    def move_down(self):
        can_move = self.y + 1 + self.piece_height <= self.rows

        if can_move: self.y += 1
        else: print("You've reached down limit.")


    def turn_piece(self):
        def rotate_90_degrees(piece): return list(zip(*piece[::-1]))

        # Check if piece can be turned
        if (
            (self.piece_width > self.piece_height and self.y + self.piece_width <= self.rows) or
            (self.piece_height > self.piece_width and self.x + self.piece_height <= self.cols) or
            (self.piece_width == self.piece_height)
        ):
            self.piece = rotate_90_degrees(self.piece)
            # Update piece's dimension
            self.piece_width = len(self.piece[0])
            self.piece_height = len(self.piece)
        else:
            print("Piece's dimension doesn't allow turning self piece.")


# Manage user's actions
def on_press(key):
    if key == Key.esc:
        # Stop listener
        return False
    elif key == KeyCode.from_char("a"):
        tetris.move_left()
    elif key == KeyCode.from_char("d"):
        tetris.move_right()
    elif key == KeyCode.from_char("s"):
        tetris.move_down()
    elif key == KeyCode.from_char("w"):
        tetris.turn_piece()

    tetris.print_options()
    tetris.print_board()

    if tetris.y + tetris.piece_height == tetris.rows:
        # Stop listener
        return False


if __name__ == "__main__":
    tetris = Tetris(10, 10)

    # Print the options and initialized board
    tetris.print_options()
    tetris.print_board()

    with Listener(on_press=on_press) as listener:
        listener.join()