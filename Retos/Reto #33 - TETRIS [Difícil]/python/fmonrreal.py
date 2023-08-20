import os
class Tetris:
    def __init__(self):
        self.piece = [
            [1, 0, 0],
            [1, 1, 1]
        ]
        self.row = 0
        self.col = 0

    def rotate(self):
        if self.col == 8 and len(  self.piece)==3:
            self.col = self.col - 1
        if self.row == 8 and len(self.piece)==2:
            self.row = self.row - 1
        self.piece = list(zip(*self.piece[::-1]))
        
    def move_left(self):
        self.col = max(self.col - 1, 0)

    def move_right(self):
        self.col = min(self.col + 1, 10 - len(self.piece[0]))

    def move_down(self):
        self.row = min(self.row + 1, 10 - len(self.piece))
    
    def move_up(self):
        self.row = max(self.row - 1, 0)

    def display(self):
        line=""
        max_row=self.row + len(self.piece)
        max_col=self.col+len(self.piece[0])
        for row in range(10):
            for col in range(10):
                if self.row <= row < max_row and self.col <= col < max_col:
                    if self.piece[row - self.row][col - self.col] == 1:
                        line+="🔳"
                    else:
                        line+="🔲"
                else:
                    line+="🔲"
            print(line)
            line=""

def main():
    tetris_game = Tetris()
    tetris_game.display()
 
    while True:
        action = input("Mover i(izquierda), d(derecha), ab(abajo), ar(arriba) / r(rotar):")

        if action == "i":
            tetris_game.move_left()
        elif action == "d":
            tetris_game.move_right()
        elif action == "ab":
            tetris_game.move_down()
        elif action == "ar":
            tetris_game.move_up()
        elif action == "r":
            tetris_game.rotate()
        else:
            print("No valido")
            continue

        os.system('cls' if os.name == 'nt' else 'clear')
        tetris_game.display()

if __name__ == "__main__":
    main()
