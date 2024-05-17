#!/usr/bin/python3

"""
# Reto #33: Tetris
/*
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
 *   recibiendo una acción cada vez que se llame, mostrando cómo se visualiza en la pantalla  de juego.
 * - Las acciones que se pueden aplicar a la pieza son: derecha, izquierda, abajo, rotar.
 * - Debes tener en cuenta los límites de la pantalla de juego.
 */
"""

__author__ = "Jorge Lambraño - jelambrar96"
__copyright__ = "Copyright 2024, retos-programacion-2023"
__credits__ = ["Brais Moure - mouredev"]
__license__ = "GPL"
__version__ = "1.0.1"
__maintainer__ = "Jorge Lambraño"
__email__ = "jelambrar@gmail.com"
__status__ = "Production"


import os
import random
import sys
import time

from threading import Thread
from pynput.keyboard import Key, KeyCode, Listener


COLUMNAS = 10
FILAS = 10
FONDO = "🔲"
PIEZA = "🔳"


S_SHAPE_TEMPLATE = [['🔲🔲🔲🔲🔲',
                     '🔲🔲🔲🔲🔲',
                     '🔲🔲🔳🔳🔲',
                     '🔲🔳🔳🔲🔲',
                     '🔲🔲🔲🔲🔲'],
                    ['🔲🔲🔲🔲🔲',
                     '🔲🔲🔳🔲🔲',
                     '🔲🔲🔳🔳🔲',
                     '🔲🔲🔲🔳🔲',
                     '🔲🔲🔲🔲🔲']]

Z_SHAPE_TEMPLATE = [['🔲🔲🔲🔲🔲',
                     '🔲🔲🔲🔲🔲',
                     '🔲🔳🔳🔲🔲',
                     '🔲🔲🔳🔳🔲',
                     '🔲🔲🔲🔲🔲'],
                    ['🔲🔲🔲🔲🔲',
                     '🔲🔲🔳🔲🔲',
                     '🔲🔳🔳🔲🔲',
                     '🔲🔳🔲🔲🔲',
                     '🔲🔲🔲🔲🔲']]

I_SHAPE_TEMPLATE = [['🔲🔲🔳🔲🔲',
                     '🔲🔲🔳🔲🔲',
                     '🔲🔲🔳🔲🔲',
                     '🔲🔲🔳🔲🔲',
                     '🔲🔲🔲🔲🔲'],
                    ['🔲🔲🔲🔲🔲',
                     '🔲🔲🔲🔲🔲',
                     '🔳🔳🔳🔳🔲',
                     '🔲🔲🔲🔲🔲',
                     '🔲🔲🔲🔲🔲']]

O_SHAPE_TEMPLATE = [['🔲🔲🔲🔲🔲',
                     '🔲🔲🔲🔲🔲',
                     '🔲🔳🔳🔲🔲',
                     '🔲🔳🔳🔲🔲',
                     '🔲🔲🔲🔲🔲']]

J_SHAPE_TEMPLATE = [['🔲🔲🔲🔲🔲',
                     '🔲🔳🔲🔲🔲',
                     '🔲🔳🔳🔳🔲',
                     '🔲🔲🔲🔲🔲',
                     '🔲🔲🔲🔲🔲'],
                    ['🔲🔲🔲🔲🔲',
                     '🔲🔲🔳🔳🔲',
                     '🔲🔲🔳🔲🔲',
                     '🔲🔲🔳🔲🔲',
                     '🔲🔲🔲🔲🔲'],
                    ['🔲🔲🔲🔲🔲',
                     '🔲🔲🔲🔲🔲',
                     '🔲🔳🔳🔳🔲',
                     '🔲🔲🔲🔳🔲',
                     '🔲🔲🔲🔲🔲'],
                    ['🔲🔲🔲🔲🔲',
                     '🔲🔲🔳🔲🔲',
                     '🔲🔲🔳🔲🔲',
                     '🔲🔳🔳🔲🔲',
                     '🔲🔲🔲🔲🔲']]

L_SHAPE_TEMPLATE = [['🔲🔲🔲🔲🔲',
                     '🔲🔲🔲🔳🔲',
                     '🔲🔳🔳🔳🔲',
                     '🔲🔲🔲🔲🔲',
                     '🔲🔲🔲🔲🔲'],
                    ['🔲🔲🔲🔲🔲',
                     '🔲🔲🔳🔲🔲',
                     '🔲🔲🔳🔲🔲',
                     '🔲🔲🔳🔳🔲',
                     '🔲🔲🔲🔲🔲'],
                    ['🔲🔲🔲🔲🔲',
                     '🔲🔲🔲🔲🔲',
                     '🔲🔳🔳🔳🔲',
                     '🔲🔳🔲🔲🔲',
                     '🔲🔲🔲🔲🔲'],
                    ['🔲🔲🔲🔲🔲',
                     '🔲🔳🔳🔲🔲',
                     '🔲🔲🔳🔲🔲',
                     '🔲🔲🔳🔲🔲',
                     '🔲🔲🔲🔲🔲']]

T_SHAPE_TEMPLATE = [['🔲🔲🔲🔲🔲',
                     '🔲🔲🔳🔲🔲',
                     '🔲🔳🔳🔳🔲',
                     '🔲🔲🔲🔲🔲',
                     '🔲🔲🔲🔲🔲'],
                    ['🔲🔲🔲🔲🔲',
                     '🔲🔲🔳🔲🔲',
                     '🔲🔲🔳🔳🔲',
                     '🔲🔲🔳🔲🔲',
                     '🔲🔲🔲🔲🔲'],
                    ['🔲🔲🔲🔲🔲',
                     '🔲🔲🔲🔲🔲',
                     '🔲🔳🔳🔳🔲',
                     '🔲🔲🔳🔲🔲',
                     '🔲🔲🔲🔲🔲'],
                    ['🔲🔲🔲🔲🔲',
                     '🔲🔲🔳🔲🔲',
                     '🔲🔳🔳🔲🔲',
                     '🔲🔲🔳🔲🔲',
                     '🔲🔲🔲🔲🔲']]

PIECES = {'S': S_SHAPE_TEMPLATE,
          'Z': Z_SHAPE_TEMPLATE,
          'J': J_SHAPE_TEMPLATE,
          'L': L_SHAPE_TEMPLATE,
          'I': I_SHAPE_TEMPLATE,
          'O': O_SHAPE_TEMPLATE,
          'T': T_SHAPE_TEMPLATE}


def create_canvan(filas, columnas):
    return [ [FONDO for _ in range(columnas)] for _ in range(filas)]


def isValidPosition(board, piece, adjX=0, adjY=0):
    # Return True if the piece is within the board and not colliding
    TEMPLATEWIDTH = 5
    TEMPLATEHEIGHT = 5
    for x in range(TEMPLATEWIDTH):
        for y in range(TEMPLATEHEIGHT):
            isAboveBoard = y + piece.y + adjY < 0
            if isAboveBoard or PIECES[piece.shape][piece.rotation][y][x] == FONDO:
                continue
            if not isOnBoard(board, x + piece.x + adjX, y + piece.y + adjY):
                return False
            if board[x + piece.x + adjX][y + piece.y + adjY] != FONDO:
                return False
    return True


def isOnBoard(fondo, x, y):
    if not y in range(len(fondo)):
        return False
    if not x in range(len(fondo[0])):
        return False
    return True



def dibujar(fondo, piece):
    fondo_nuevo = [ item[:] for item in fondo]
    TEMPLATEHEIGHT = 5
    TEMPLATEWIDTH = 5
    for y in range(TEMPLATEHEIGHT):
        for x in range(TEMPLATEWIDTH):
            if not isOnBoard(fondo, x + piece.x, y + piece.y):
                continue
            if PIECES[piece.shape][piece.rotation][y][x] == FONDO:
                continue
            if PIECES[piece.shape][piece.rotation][y][x] == PIEZA:
                fondo_nuevo[y + piece.y][x + piece.x] = PIEZA
    for item in fondo_nuevo:
        print("".join(item))


class PiezaTetris:
    def __init__(self, pieza_tetris=None, rotation=None, x=0, y=0):
        if pieza_tetris is None:
            pieza_tetris = random.choice([item for item in PIECES.keys()])
        if not pieza_tetris in  PIECES.keys():
            raise Exception("ERROR: PIEZA INVALIDA")         
        self.shape = pieza_tetris
        self.rotation = random.randint(0, len(PIECES[self.shape]) - 1)
        self.x = x
        self.y = y


class JuegoTetris:

    def __init__(self, pieza_tetris=None, filas=FILAS, columnas=COLUMNAS):
        self._pieza_tetris = pieza_tetris
        # banderas de movimiento
        self._move_down_flag = False
        self._move_left_flag = False
        self._move_right_flag = False
        self._rotate_flag = False
        # bandera de salida
        self._exit_flag = False


    def _on_press(self, key):
        # print("pressing")
        if Key.esc == key:
            self._exit_flag = True
        if key == Key.up or key == KeyCode.from_char('w'):
            self._rotate_flag = True 
        if key == Key.down or key == KeyCode.from_char('s'):
            self._move_down_flag = True 
        if key == Key.left or key == KeyCode.from_char('a'):
            self._move_left_flag = True 
        if key == Key.right or key == KeyCode.from_char('d'):
            self._move_right_flag = True 


    def _on_release(self, key):
        # print("releasing")
        if key == Key.up or key == KeyCode.from_char('w'):
            self._rotate_flag = False
        if key == Key.down or key == KeyCode.from_char('s'):
            self._move_down_flag = False 
        if key == Key.left or key == KeyCode.from_char('a'):
            self._move_left_flag = False
        if key == Key.right or key == KeyCode.from_char('d'):
            self._move_right_flag = False 


    def start(self):

        code = Listener(on_press=self._on_press, on_release=self._on_release)
        code.start()

        th = Thread(target=self._loop)
        th.start()

        th.join()
        code.join()



    def _loop(self):

        fondo = create_canvan(filas=FILAS, columnas=COLUMNAS)
        pieza = PiezaTetris(pieza_tetris=self._pieza_tetris, x=0, y=-2)

        while True:

            if self._move_left_flag and isValidPosition(fondo, pieza, adjX=-1, adjY=0):
                pieza.x -= 1
            if self._move_right_flag and isValidPosition(fondo, pieza, adjX=1, adjY=0):
                pieza.x += 1
            if self._move_down_flag and isValidPosition(fondo, pieza, adjX=0, adjY=1):
                pieza.y += 1
            if self._rotate_flag:
                pieza_rotada = PiezaTetris(pieza_tetris=pieza.shape, x=pieza.x, y=pieza.y)
                pieza_rotada.retation = (pieza.rotation + 1) % len(PIECES[pieza_rotada.shape])
                if isValidPosition(fondo, pieza_rotada, adjX=0, adjY=0):
                    pieza.rotation = pieza_rotada.rotation

            os.system('clear')
            dibujar(fondo, pieza)
            time.sleep(0.050) # 20 FPS

            if self._exit_flag:
                break




if __name__ == '__main__':
    jt = JuegoTetris()
    jt.start()