class TetrisPiece:
    def __init__(self):
        self.piece = [
            [" ", " ", "🔳"],
            ["🔳", "🔳", "🔳"]
        ]
        self.row = 0
        self.col = 0

    def display(self):
        for r in range(len(self.piece)):
            for c in range(len(self.piece[0])):
                print(self.piece[r][c], end="")
            print()

    def can_move(self, board, dr, dc):
        for r in range(len(self.piece)):
            for c in range(len(self.piece[0])):
                if self.piece[r][c] != " ":
                    new_r = self.row + r + dr
                    new_c = self.col + c + dc
                    if (
                        new_r < 0
                        or new_r >= len(board)
                        or new_c < 0
                        or new_c >= len(board[0])
                        or board[new_r][new_c] != "🔲"
                    ):
                        return False
        return True

    def place_piece(self, board):
        for r in range(len(self.piece)):
            for c in range(len(self.piece[0])):
                if self.piece[r][c] != " ":
                    board[self.row + r][self.col + c] = self.piece[r][c]

    def remove_piece(self, board):
        for r in range(len(self.piece)):
            for c in range(len(self.piece[0])):
                if self.piece[r][c] != " ":
                    board[self.row + r][self.col + c] = "🔲"

    def move(self, board, dr, dc):
        self.remove_piece(board)
        if self.can_move(board, dr, dc):
            self.row += dr
            self.col += dc
        self.place_piece(board)

    def rotate(self, board):
        self.remove_piece(board)
        original_piece = self.piece.copy()
        new_piece = [[original_piece[1][0], original_piece[0][0], original_piece[0][1]],
                     [original_piece[0][2], " ", " "]]
        if self.can_move(board, 0, 0):
            self.piece = new_piece
        self.place_piece(board)


def initialize_board(rows, cols):
    return [["🔲" for _ in range(cols)] for _ in range(rows)]


def display_board(board):
    for row in board:
        for cell in row:
            print(cell, end="")
        print()


def main():
    rows = 10
    cols = 10
    board = initialize_board(rows, cols)
    piece = TetrisPiece()

    while True:
        action = input("Enter action (right, left, down, rotate, exit): ")
        if action == "exit":
            break
        elif action == "right":
            piece.move(board, 0, 1)
        elif action == "left":
            piece.move(board, 0, -1)
        elif action == "down":
            piece.move(board, 1, 0)
        elif action == "rotate":
            piece.rotate(board)
        
        display_board(board)

if __name__ == "__main__":
    main()
