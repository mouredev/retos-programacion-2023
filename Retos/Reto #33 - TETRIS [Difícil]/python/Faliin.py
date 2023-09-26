class Tetris:
    def __init__(self):
        self.board = [['🔲' for _ in range(10)] for _ in range(10)]
        self.tetromino = [[' ', '🔳', ' '],
                          ['🔳', '🔳', '🔳']]
        self.position = [0, 0]  # [fila, columna] posición de la parte superior izquierda de la pieza

    def print_board(self):
        for row in self.board:
            print(''.join(row))
        print("\n")

    def move(self, action):
        if action == "derecha":
            if self.can_move(0, 1):
                self.position[1] += 1
        elif action == "izquierda":
            if self.can_move(0, -1):
                self.position[1] -= 1
        elif action == "abajo":
            if self.can_move(1, 0):
                self.position[0] += 1
        elif action == "rotar":
            self.tetromino = self.rotate()
        self.update_board()

    def can_move(self, row_change, col_change):
        for i, row in enumerate(self.tetromino):
            for j, cell in enumerate(row):
                if cell == '🔳':
                    new_row = self.position[0] + i + row_change
                    new_col = self.position[1] + j + col_change
                    if (0 <= new_row < 10 and 0 <= new_col < 10) and self.board[new_row][new_col] == '🔲':
                        continue
                    else:
                        return False
        return True

    def rotate(self):
        rotated = list(zip(*self.tetromino[::-1]))
        return [list(row) for row in rotated]

    def update_board(self):
        self.board = [['🔲' for _ in range(10)] for _ in range(10)]
        for i, row in enumerate(self.tetromino):
            for j, cell in enumerate(row):
                if cell == '🔳':
                    self.board[self.position[0] + i][self.position[1] + j] = '🔳'


if __name__ == "__main__":
    game = Tetris()
    game.print_board()

    while True:
        action = input("Introduce una acción (derecha, izquierda, abajo, rotar) o 'salir' para terminar: ")
        if action == "salir":
            break
        if action in ["derecha", "izquierda", "abajo", "rotar"]:
            game.move(action)
            game.print_board()
        else:
            print("Acción no reconocida, por favor intenta de nuevo.")

