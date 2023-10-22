import unittest

class Cell:
    ...

class House:
    def __init__(self):
        self.cells = [
            [
                None for _ in range(4)
            ]
            for _ in range(4)
        ]

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

if __name__ == '__main__':
    unittest.main()
