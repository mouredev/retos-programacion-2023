import unittest
from unittest.mock import patch
import random


class Cell:
    ...


class Door(Cell):
    ...


class Candy(Cell):
    ...


class House:
    def __init__(self):
        self.setup_special_cells()
        self.cells = [
            [
                self.get_cells(row_index, col_index)
                for col_index in range(4)
            ]
            for row_index in range(4)
        ]

    def get_cells(self, row_index, col_index):
        if (row_index, col_index,) in self.special_cells:
            return self.special_cells[(row_index, col_index,)]
        else:
            return None

    def setup_special_cells(self):
        self.special_cells = {
            (
                random.randint(0, 3),
                random.randint(0, 3),
            ): Door()
        }
        candy_pos_row = random.randint(0, 3)
        candy_pos_col = random.randint(0, 3)
        while (candy_pos_row, candy_pos_col,) in self.special_cells:
            candy_pos_row = random.randint(0, 3)
            candy_pos_col = random.randint(0, 3)
        self.special_cells[
            (candy_pos_row, candy_pos_col)
        ] = Candy()



class TestDoor(unittest.TestCase):
    def test_init(self):
        door = Door()
        self.assertIsNotNone(door)


class TestCandy(unittest.TestCase):
    def test_init(self):
        candy = Candy()
        self.assertIsNotNone(candy)


class TestCell(unittest.TestCase):
    def test_init(self):
        cell = Cell()
        self.assertIsNotNone(cell)


class TestHouse(unittest.TestCase):

    def test_init(self):
        house = House()
        self.assertEqual(len(house.cells), 4)
        for room_index in range(4):
            self.assertEqual(len(house.cells[room_index]), 4)

    @patch('random.randint', side_effect=[2, 3, 3, 1])
    def test_door_pos(self, randint_patched):
        house = House()
        self.assertIsInstance(
            house.cells[2][3],
            Door,
        )

    @patch('random.randint', side_effect=[
        2, 3,  # house
        2, 3,  # candy
        3, 1,  # candy
    ])
    def test_candy_pos(self, randint_patched):
        house = House()
        self.assertIsInstance(
            house.cells[2][3],
            Door,
        )
        self.assertIsInstance(
            house.cells[3][1],
            Candy,
        )


if __name__ == '__main__':
    unittest.main()
