import os
import signal
import sys

import keyboard


class Piece:
    def __init__(self):
        self.piece = [["🔳", "🔲", "🔲"],
                      ["🔳", "🔳", "🔳"]]
        self.x = 0
        self.y = 0

def play_tetris():

    piece = Piece()
    board = [["🔲","🔲","🔲","🔲","🔲","🔲","🔲","🔲", "🔲","🔲"] for _ in range(10)]

    keyboard.add_hotkey("down", lambda: move_piece(board, piece, y_move=1))
    keyboard.add_hotkey("left", lambda: move_piece(board, piece, x_move=-1))
    keyboard.add_hotkey("right", lambda: move_piece(board, piece, x_move=1))
    keyboard.add_hotkey("up" , lambda: rotate_piece(board, piece))

    print_boad(draw_piece_in_board(board, piece))

    while True:
        board = [["🔲","🔲","🔲","🔲","🔲","🔲","🔲","🔲", "🔲","🔲"] for _ in range(10)]
        pass


def move_piece(board: list, piece: Piece, x_move: int = 0, y_move: int = 0):
    move_piece_x(board, piece, x_move=x_move)
    move_piece_y(board, piece, y_move=y_move)
    print_boad(draw_piece_in_board(board, piece))
    board = [["🔲","🔲","🔲","🔲","🔲","🔲","🔲","🔲", "🔲","🔲"] for _ in range(10)]


def draw_piece_in_board(board: list, piece: Piece) -> list:
    board_copy = board
    for y, row in enumerate(piece.piece):
        for x, sqr in enumerate(row):
           board_copy[y + piece.y][x + piece.x] = sqr
    return board_copy


def move_piece_y(board: list, piece: Piece, y_move: int = 0):
    board_size = len(board)
    piece_size = len(piece.piece)
    piece.y = min(board_size - piece_size, piece.y + y_move)


def move_piece_x(board: list, piece: Piece, x_move: int = 0):
    if x_move < 0:
        piece.x = max(0, piece.x - 1)
        return
    board_size = len(board[0])
    piece_size = len(piece.piece[0])
    piece.x = min(board_size - piece_size, piece.x + x_move)


def print_boad(board: list):
    os.system("cls")
    for row in board:
        print(*row)


def rotate_piece(board: list, piece: Piece) -> list:
    rot_piece = []
    for y in range(len(piece.piece[0])):
        rot_piece.append([])
        for x in range(len(piece.piece)):
            rot_piece[y].append(piece.piece[len(piece.piece) - x - 1][y])
    piece.piece = rot_piece
    move_piece(board, piece)


if __name__ == "__main__":
    signal.signal(signal.SIGINT, lambda s, f: sys.exit(0))
    play_tetris()
