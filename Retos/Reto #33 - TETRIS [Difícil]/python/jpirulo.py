import tkinter as tk

class TetrisGame:
    def __init__(self):
        self.window = tk.Tk()
        self.window.title("Tetris")
        self.canvas = tk.Canvas(self.window, width=300, height=600, bg="black")
        self.canvas.pack()
        
        self.board = [[0] * 10 for _ in range(10)]
        self.current_piece = [[0, 1, 0], [1, 1, 1]]
        self.piece_row = 0
        self.piece_col = 0
        
        self.draw_board()
        self.draw_piece()
        
        self.window.bind("<Left>", self.move_left)
        self.window.bind("<Right>", self.move_right)
        self.window.bind("<Down>", self.move_down)
        self.window.bind("<Up>", self.rotate_piece)
        
        self.window.after(1000, self.move_down)
        self.window.mainloop()
    
    def draw_board(self):
        self.canvas.delete("all")
        for row in range(10):
            for col in range(10):
                if self.board[row][col] == 1:
                    self.canvas.create_rectangle(col * 30, row * 30, (col + 1) * 30, (row + 1) * 30, fill="blue")
    
    def draw_piece(self):
        for row in range(len(self.current_piece)):
            for col in range(len(self.current_piece[0])):
                if self.current_piece[row][col] == 1:
                    self.canvas.create_rectangle(
                        (self.piece_col + col) * 30,
                        (self.piece_row + row) * 30,
                        (self.piece_col + col + 1) * 30,
                        (self.piece_row + row + 1) * 30,
                        fill="red"
                    )
    
    def move_left(self, event):
        if self.piece_col > 0 and not self.check_collision(0, -1):
            self.piece_col -= 1
            self.draw_board()
            self.draw_piece()
    
    def move_right(self, event):
        if self.piece_col + len(self.current_piece[0]) < 10 and not self.check_collision(0, 1):
            self.piece_col += 1
            self.draw_board()
            self.draw_piece()
    
    def move_down(self, event=None):
        if self.piece_row + len(self.current_piece) < 10 and not self.check_collision(1, 0):
            self.piece_row += 1
            self.draw_board()
            self.draw_piece()
            self.window.after(1000, self.move_down)
    
    def rotate_piece(self, event):
        rotated_piece = [[0] * len(self.current_piece) for _ in range(len(self.current_piece[0]))]
        for row in range(len(self.current_piece)):
            for col in range(len(self.current_piece[0])):
                rotated_piece[col][len(self.current_piece) - row - 1] = self.current_piece[row][col]
        if (
            self.piece_col + len(rotated_piece[0]) <= 10 and
            self.piece_row + len(rotated_piece) <= 10 and
            not self.check_collision(0, 0, rotated_piece)
        ):
            self.current_piece = rotated_piece
            self.draw_board()
            self.draw_piece()
    
    def check_collision(self, row_offset, col_offset, piece=None):
        if piece is None:
            piece = self.current_piece
        for row in range(len(piece)):
            for col in range(len(piece[0])):
                if piece[row][col] == 1:
                    board_row = self.piece_row + row + row_offset
                    board_col = self.piece_col + col + col_offset
                    if (
                        board_row >= 10 or
                        board_col < 0 or board_col >= 10 or
                        self.board[board_row][board_col] == 1
                    ):
                        return True
        return False

if __name__ == "__main__":
    game = TetrisGame()
