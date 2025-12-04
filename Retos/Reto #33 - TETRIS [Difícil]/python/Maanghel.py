"""
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
    recibiendo una acción cada vez que se llame, mostrando cómo se visualiza en
    la pantalla de juego.
- Las acciones que se pueden aplicar a la pieza son: derecha, izquierda, abajo, rotar.
- Debes tener en cuenta los límites de la pantalla de juego.
"""

from pynput import keyboard
import os

class Tetris:
    """
    Clase que representa un juego de Tetris.
    """
    def __init__(self) -> None:
        """
        Inicializa el juego de Tetris con el tablero y la pieza.
        
        returns:
            None
        """
        self.board_size = 10
        self.empty = "🔲"
        self.full = "🔳"

        self.piece = [
            [self.full, self.empty, self.empty],
            [self.full, self.full, self.full]
        ]

        self.piece_h = len(self.piece)
        self.piece_w = len(self.piece[0])

        self.row = 0
        self.col = 0

    def render(self) -> None:
        """
        Imprime el tablero completo con la pieza en su posición actual.

        returns:
            None
        """
        board = [[self.empty for _ in range(self.board_size)] for _ in range(self.board_size)]

        for r_piece, row_data in enumerate(self.piece):
            for c_piece, cell in enumerate(row_data):
                if cell == self.full:
                    board[self.row + r_piece][self.col + c_piece] = self.full

        for r in range(self.board_size):
            print("".join(board[r]))
        print()

    def clear_console(self) -> None:
        """
        Limpia la consola para una mejor visualización.

        returns:
            None
        """
        os.system('cls' if os.name == 'nt' else 'clear')

    def rotate(self) -> None:
        """
        Rota la pieza 90° en sentido horario, respetando límites.

        returns:
            None
        """
        rotated = [list(row) for row in zip(*self.piece[::-1])]
        new_h = len(rotated)
        new_w = len(rotated[0])

        if self.col + new_w > self.board_size:
            self.col = self.board_size - new_w
        if self.row + new_h > self.board_size:
            self.row = self.board_size - new_h

        self.piece = rotated
        self.piece_h = new_h
        self.piece_w = new_w

    def move_left(self) -> None:
        """
        Mueve la pieza hacia la izquierda si no supera los límites.

        returns:
            None
        """
        if self.col > 0:
            self.col -= 1

    def move_right(self) -> None:
        """
        Mueve la pieza hacia la derecha si no supera los límites.

        returns:
            None
        """
        if self.col + self.piece_w < self.board_size:
            self.col += 1

    def move_down(self) -> None:
        """
        Mueve la pieza hacia abajo si no supera los límites.

        returns:
            None
        """
        if self.row + self.piece_h < self.board_size:
            self.row += 1

    def action(self, key: keyboard.Key) -> None:
        """
        Maneja la acción correspondiente según la tecla presionada.

        args:
            key (keyboard.Key): Tecla presionada.

        returns:
            None
        """
        actions = {
            keyboard.Key.left: self.move_left,
            keyboard.Key.right: self.move_right,
            keyboard.Key.down: self.move_down,
            keyboard.Key.up: self.rotate
        }

        action_to_run = actions.get(key)
        if action_to_run:
            action_to_run()
            self.clear_console()
            self.render()


if __name__ == "__main__":
    print("Controla la pieza con flechas. Presiona ESC para salir.\n")

    game = Tetris()
    game.render()

    def on_press(key: keyboard.Key) -> None:
        """
        Maneja la pulsación de teclas.
        - Flechas para mover/rotar la pieza.
        - ESC para salir.
        """
        if key == keyboard.Key.esc:
            return False
        game.action(key)

    with keyboard.Listener(on_press=on_press) as listener:
        listener.join()
        print()
