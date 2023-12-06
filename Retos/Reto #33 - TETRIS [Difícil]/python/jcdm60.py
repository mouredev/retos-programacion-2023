# Reto #33: Tetris
#### Dificultad: Difícil | Publicación: 14/08/23 | Corrección: 21/08/23

## Enunciado

#
# Crea un programa capaz de gestionar una pieza de Tetris.
# - La pantalla de juego tiene 10 filas y 10 columnas representadas por símbolos 🔲
# - La pieza de tetris a manejar será la siguiente (si quieres, puedes elegir otra):
#   🔳
#   🔳🔳🔳
# - La pieza aparecerá por primera vez en la parte superior izquierda de la pantalla de juego.
#   🔳🔲🔲🔲🔲🔲🔲🔲🔲🔲
#   🔳🔳🔳🔲🔲🔲🔲🔲🔲🔲
#   🔲🔲🔲🔲🔲🔲🔲🔲🔲🔲
#   🔲🔲🔲🔲🔲🔲🔲🔲🔲🔲
#   🔲🔲🔲🔲🔲🔲🔲🔲🔲🔲
#   🔲🔲🔲🔲🔲🔲🔲🔲🔲🔲
#   🔲🔲🔲🔲🔲🔲🔲🔲🔲🔲
#   🔲🔲🔲🔲🔲🔲🔲🔲🔲🔲
#   🔲🔲🔲🔲🔲🔲🔲🔲🔲🔲
#   🔲🔲🔲🔲🔲🔲🔲🔲🔲🔲
# - Debes desarrollar una función capaz de desplazar y rotar la pieza en el tablero,
#   recibiendo una acción cada vez que se llame, mostrando cómo se visualiza en la pantalla  de juego.
# - Las acciones que se pueden aplicar a la pieza son: derecha, izquierda, abajo, rotar.
# - Debes tener en cuenta los límites de la pantalla de juego.
#

class TetrisPiece:
    def __init__(self):
        self.piece = [
            [1, 0, 0],
            [1, 1, 1]
        ]
        self.row = 0
        self.col = 0

    def rotate(self):
        self.piece = list(zip(*self.piece[::-1]))

    def move_left(self):
        self.col = max(self.col - 1, 0)

    def move_right(self):
        self.col = min(self.col + 1, 10 - len(self.piece[0]))

    def move_down(self):
        self.row = min(self.row + 1, 10 - len(self.piece))

    def display(self):
        for r in range(10):
            for c in range(10):
                if r >= self.row and r < self.row + len(self.piece) and c >= self.col and c < self.col + len(self.piece[0]):
                    if self.piece[r - self.row][c - self.col] == 1:
                        print("🔳", end='')
                    else:
                        print("🔲", end='')
                else:
                    print("🔲", end='')
            print()

def main():
    tetris_piece = TetrisPiece()
    tetris_piece.display()

    while True:
        action = input("Ingrese una acción (izquierda, derecha, abajo, rotar): ")

        if action == "izquierda":
            tetris_piece.move_left()
        elif action == "derecha":
            tetris_piece.move_right()
        elif action == "abajo":
            tetris_piece.move_down()
        elif action == "rotar":
            tetris_piece.rotate()
        else:
            print("Acción no válida. Intente de nuevo.")
            continue

        tetris_piece.display()

if __name__ == "__main__":
    main()
