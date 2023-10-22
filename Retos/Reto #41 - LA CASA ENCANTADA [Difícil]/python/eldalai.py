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
        door_pos_row = random.randint(0, 3)
        door_pos_col = random.randint(0, 3)
        self.cells = [
            [
                (
                    Door()
                    if row_index == door_pos_row and col_index == door_pos_col
                    else None
                )
                for col_index in range(4)
            ]
            for row_index in range(4)
        ]


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

    @patch('random.randint', side_effect=[2, 3])
    def test_door_pos(self, randint_patched):
        house = House()
        self.assertIsInstance(
            house.cells[2][3],
            Door,
        )


if __name__ == '__main__':
    unittest.main()
