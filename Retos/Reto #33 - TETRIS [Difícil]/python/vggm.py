from typing import List
import pygame as pg
from enum import Enum

BLACK = (0, 0, 0)
GREEN = (0, 0xFF, 0)

WIDTH = HEIGHT = 10

SCREEN_WIDTH = SCREEN_HEIGHT = 600
SCREEN_SIZE = (SCREEN_HEIGHT, SCREEN_WIDTH)

ROW = 0
COL = 1


class Orientation(Enum):
  TOP = 'T'
  DOWN = 'D'
  LEFT = 'L'
  RIGHT = 'R'


class Board:
  def __init__(self, window) -> None:
    
    self.T_center = [1,1]
    self.T_shape = [[0,1], [1,0], [1,1], [1,2]]
    self.T_orientation = Orientation.TOP

    self.rotation = {
        Orientation.TOP: self.__from_top,
        Orientation.RIGHT: self.__from_right,
        Orientation.DOWN: self.__from_down,
        Orientation.LEFT: self.__from_left
      }

    self.window = window
  
  # Check moves  
  def can_move_down (self) -> bool:
    if self.T_orientation == Orientation.TOP:
      return self.T_center[ROW] + 1 < HEIGHT

    return self.T_center[ROW] + 2 < HEIGHT
  
  def can_move_left (self) -> bool:
    if self.T_orientation == Orientation.RIGHT:
      return self.T_center[COL] - 1 >= 0

    return self.T_center[COL] - 2 >= 0
  
  def can_move_right (self) -> bool:
    if self.T_orientation == Orientation.LEFT:
      return self.T_center[COL] + 1 < WIDTH

    return self.T_center[COL] + 2 < WIDTH
  
  def can_rotate(self) -> bool:
    return self.T_center[COL] not in [0, WIDTH-1] and \
      self.T_center[ROW] not in [0, HEIGHT-1]
  
  
  # Moves
  def __make_move (self, DEST: int, MOVE: int) -> None:
    self.T_center[DEST] += MOVE
    
    for coord in self.T_shape:
      coord[DEST] += MOVE 
  
  def move_down (self) -> None:
    if self.can_move_down():
      self.__make_move(ROW, 1)
  
  def move_left (self) -> None:
    if self.can_move_left():
      self.__make_move(COL, -1)
  
  def move_right (self) -> None:
    if self.can_move_right():
      self.__make_move(COL, 1)
  
  
  # Rotation
  def __make_rotation ( self, configs: List[tuple] ) -> None:
    self.T_shape = [self.T_center.copy()]
    
    for row, col in configs:
      self.T_shape.append([self.T_center[ROW]+row, self.T_center[COL]+col])
  
  def __from_top(self) -> None:
    self.__make_rotation( [(0,1), (1,0), (-1,0)] )
    self.T_orientation = Orientation.RIGHT
    
  def __from_right(self) -> None:
    self.__make_rotation( [(1,0), (0,1), (0,-1)] )
    self.T_orientation = Orientation.DOWN
    
  def __from_down(self) -> None:
    self.__make_rotation( [(0,-1), (1,0), (-1,0)] )
    self.T_orientation = Orientation.LEFT
    
  def __from_left(self) -> None:
    self.__make_rotation( [(-1,0), (0,1), (0,-1)] )
    self.T_orientation = Orientation.TOP
  
  def rotate(self) -> None:
    if self.can_rotate():
      self.rotation[self.T_orientation]()

  def draw(self) -> None:
    
    self.window.fill(BLACK)
    
    for y, x in self.T_shape:
      pg.draw.rect(self.window, GREEN, pg.Rect( x * SCREEN_WIDTH / WIDTH, y * SCREEN_HEIGHT / HEIGHT, SCREEN_WIDTH / WIDTH - 2, SCREEN_HEIGHT / HEIGHT -2 ))
    
    pg.display.flip()


if __name__ == '__main__':
  
  pg.init()
  pg.display.set_caption('Tetris')

  window = pg.display.set_mode( SCREEN_SIZE )
  
  board = Board(window)
  board.draw()
  
  moves = {
    pg.K_UP: board.rotate,
    pg.K_DOWN: board.move_down,
    pg.K_LEFT: board.move_left,
    pg.K_RIGHT: board.move_right
  }
  
  end = False
  while not end:
    
    for event in pg.event.get():
      if event.type == pg.QUIT:
        end = True
      
      if event.type == pg.KEYDOWN:
        
        if event.key == pg.K_ESCAPE:
          end = True

        if event.key in moves.keys():
          moves[event.key]()
    
    board.draw()
    