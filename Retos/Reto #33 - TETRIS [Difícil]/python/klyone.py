#!/usr/bin/env python3

board_size = 10
max_orientations = 4
empty_cell = "🔲"
filled_cell = "🔳"

class TetrisGame:
    def __init__(self):
        self.piece_pos = [0,0]
        self.piece_orientation = 0

    def generate_points_for_piece(self, new_pos=None, orientation=None):
        points = []

        if new_pos != None and orientation != None:
            pp = new_pos
            orien = orientation
        else:
            pp = self.piece_pos
            orien = self.piece_orientation

        points.append(pp)

        if orien == 0:
            points.append([pp[0]+1,pp[1]])
            points.append([pp[0]+1,pp[1]+1])
            points.append([pp[0]+1,pp[1]+2])
        elif orien == 1:
            points.append([pp[0],pp[1]-1])
            points.append([pp[0]+1,pp[1]-1])
            points.append([pp[0]+2,pp[1]-1])
        elif orien == 2:
            points.append([pp[0]-1,pp[1]])
            points.append([pp[0]-1,pp[1]-1])
            points.append([pp[0]-1,pp[1]-2])
        elif orien == 3:
            points.append([pp[0],pp[1]+1])
            points.append([pp[0]-1,pp[1]+1])
            points.append([pp[0]-2,pp[1]+1])
        else:
            points = []

        return points

    def is_valid_position(self, pos):
        if pos[0] < 0:
            return False
        if pos[0] >= board_size:
            return False
        if pos[1] < 0:
            return False
        if pos[1] >= board_size:
            return False
        return True

    def create_new_position(self, incx, incy):
        new_pos = [0,0]
        new_pos[0] = self.piece_pos[0] + incx
        new_pos[1] = self.piece_pos[1] + incy
        return new_pos

    def update_piece_position(self, new_pos, orientation):
        points = self.generate_points_for_piece(new_pos, orientation)
        valid = True

        for p in points:
            if not self.is_valid_position(p):
                valid = False
                break

        if valid:
            self.piece_pos = new_pos
            self.piece_orientation = orientation

    def up(self):
        new_pos = self.create_new_position(-1,0)
        self.update_piece_position(new_pos, self.piece_orientation)

    def down(self):
        new_pos = self.create_new_position(1,0)
        self.update_piece_position(new_pos, self.piece_orientation)

    def right(self):
        new_pos = self.create_new_position(0,1)
        self.update_piece_position(new_pos, self.piece_orientation)

    def left(self):
        new_pos = self.create_new_position(0,-1)
        self.update_piece_position(new_pos, self.piece_orientation)

    def rotate(self):
        if self.piece_orientation == 0:
            new_pos = self.create_new_position(0,1)
        elif self.piece_orientation == 1:
            new_pos = self.create_new_position(1,1)
        elif self.piece_orientation == 2:
            new_pos = self.create_new_position(1,-2)
        elif self.piece_orientation == 3:
            new_pos = self.create_new_position(-2,0)
        else:
            new_pos = self.create_new_position(0,0)

        self.update_piece_position(new_pos, (self.piece_orientation + 1) % max_orientations)

    def print_status(self):
        output = ""
        for i in range(board_size):
            for j in range(board_size):
                if [i,j] in self.generate_points_for_piece():
                    output = output + filled_cell
                else:
                    output = output + empty_cell
            output = output + "\n"
        print(output)

if __name__ == "__main__":
    game = TetrisGame()
    game.print_status()

    while True:
        action = input("Press action: ")

        if action == "u":
            game.up()
        elif action == "d":
            game.down()
        elif action == "r":
            game.right()
        elif action == "l":
            game.left()
        elif action == "x":
            game.rotate()
        elif action == "q":
            break
        else:
            print("Invalid action: up (u), down (d), right (r), left (l) or rotate (x)")
            print("Press q to stop program")
            continue

        game.print_status()
