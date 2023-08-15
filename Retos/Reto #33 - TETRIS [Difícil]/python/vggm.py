from enum import Enum
from os import system
import platform

WIDTH = HEIGHT = 10

ROW = 0
COL = 1

CLEAN = 'cls' if platform.system() == 'Windows' else 'clear'


class Orientation(Enum):
  TOP = 'T'
  DOWN = 'D'
  LEFT = 'L'
  RIGHT = 'R'


class Board:
  def __init__(self) -> None:
    
    self.map = [[ 0 for _ in range( WIDTH ) ] for _ in range( HEIGHT ) ]
    self.T_center = [1,1]
    self.T_shape = [[0,1], [1,0], [1,1], [1,2]]
    self.T_orientation = Orientation.TOP
    self.update()
  
  # Check moves
  def can_move_top (self) -> bool:
    if self.T_orientation == Orientation.DOWN:
      return self.T_center[ROW] - 1 >= 0

    return self.T_center[ROW] - 2 >= 0
  
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
    return self.T_center[COL] not in [0, WIDTH] and \
      self.T_center[ROW] not in [0, HEIGHT]
  
  
  # Moves
  def __make_move (self, DEST: int, MOVE: int) -> None:
    self.T_center[DEST] += MOVE
    
    for coord in self.T_shape:
      coord[DEST] += MOVE
    
    self.update()
  
  def move_top (self) -> None:
    if self.can_move_top():
      self.__make_move(ROW, -1)
  
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
  def __from_top(self) -> None:
    self.T_shape = [self.T_center.copy()]
    self.T_shape.append([self.T_center[ROW], self.T_center[COL]+1])
    self.T_shape.append([self.T_center[ROW]+1, self.T_center[COL]])
    self.T_shape.append([self.T_center[ROW]-1, self.T_center[COL]])
    self.T_orientation = Orientation.RIGHT
    
  def __from_right(self) -> None:
    self.T_shape = [self.T_center.copy()]
    self.T_shape.append([self.T_center[ROW]+1, self.T_center[COL]])
    self.T_shape.append([self.T_center[ROW], self.T_center[COL]+1])
    self.T_shape.append([self.T_center[ROW], self.T_center[COL]-1])
    self.T_orientation = Orientation.DOWN
    
  def __from_down(self) -> None:
    self.T_shape = [self.T_center.copy()]
    self.T_shape.append([self.T_center[ROW], self.T_center[COL]-1])
    self.T_shape.append([self.T_center[ROW]+1, self.T_center[COL]])
    self.T_shape.append([self.T_center[ROW]-1, self.T_center[COL]])
    self.T_orientation = Orientation.LEFT
    
  def __from_left(self) -> None:
    self.T_shape = [self.T_center.copy()]
    self.T_shape.append([self.T_center[ROW]-1, self.T_center[COL]])
    self.T_shape.append([self.T_center[ROW], self.T_center[COL]+1])
    self.T_shape.append([self.T_center[ROW], self.T_center[COL]-1])
    self.T_orientation = Orientation.TOP
  
  def rotate(self) -> None:
    if self.can_rotate():
      
      rotation = {
        Orientation.TOP: self.__from_top,
        Orientation.RIGHT: self.__from_right,
        Orientation.DOWN: self.__from_down,
        Orientation.LEFT: self.__from_left
      }
      
      rotation[self.T_orientation]()
      self.update()
  
  def update(self) -> None:
    
    self.map = [ [ 0 for _ in range(WIDTH) ] for _ in range(HEIGHT) ]
    
    for row, col in self.T_shape:
      self.map[row][col] = 1
  
  def draw(self) -> None:
    system(CLEAN)
    outline = '🟢'
    print( outline * ( WIDTH + 2 ) )
    for row in self.map:
      print(outline, end='')
      for value in row:
        data = '🟪' if value == 1 else '⬛'
        print(data, end='')
      print(outline)
    print( outline * ( WIDTH + 2 ) )



def game( key: str ):
  movement = {
    'w': board.move_top,
    'a': board.move_left,
    's': board.move_down,
    'd': board.move_right,
    'r': board.rotate
  }
  
  movement.get(key, lambda : print('Not valid key!'))()
  board.draw()


if __name__ == '__main__':
  
  board = Board()
  board.draw()
  
  key = input("[w,a,s,d,r] para mover o 'q' para salir: ")
  while key != 'q':
    
    game(key)
    key = input("[w,a,s,d,r] para mover o 'q' para salir: ")
    