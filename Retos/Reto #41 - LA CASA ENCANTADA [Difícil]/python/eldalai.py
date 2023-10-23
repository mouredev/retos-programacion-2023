import unittest
from unittest.mock import patch
import random


class Cell:
    def __init__(self):
        self.visile = False


class Door(Cell):
    def __init__(self):
        self.visile = True

    def __str__(self):
        return "🚪"


class Enigma(Cell):
    def __str__(self):
        return "❓" if self.visile else "⬜️"


class Candy(Cell):
    def __str__(self):
        return "🍭" if self.visile else "⬜️"


class Ghost(Cell):
    def __str__(self):
        return "👻" if self.visile else "⬜️"


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

    def __str__(self):
        output = ""
        for row_index, row in enumerate(self.cells):
            for col_index, item in enumerate(row):
                if (
                    row_index == self.player_row and
                    col_index == self.player_col
                ):
                    output += "😐"
                else:
                    output += str(item)
            output += '\n'
        return output

    def get_cells(self, row_index, col_index):
        if (row_index, col_index,) in self.special_cells:
            return self.special_cells[(row_index, col_index,)]
        else:
            if random.randint(1, 10) == 1:
                return Ghost()
            else:
                return Enigma()

    def setup_special_cells(self):
        door_pos_row = random.randint(0, 3)
        door_pos_col = random.randint(0, 3)
        self.special_cells = {
            (
                door_pos_row,
                door_pos_col,
            ): Door()
        }
        self.player_row = door_pos_row
        self.player_col = door_pos_col
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
        self.assertTrue(door.visile)

    def test__str__(self):
        door = Door()
        self.assertEqual(
            str(door),
            "🚪",
        )


class TestCandy(unittest.TestCase):
    def test_init(self):
        candy = Candy()
        self.assertIsNotNone(candy)
        self.assertFalse(candy.visile)

    def test__str__invisible(self):
        candy = Candy()
        self.assertEqual(
            str(candy),
            "⬜️",
        )

    def test__str__visible(self):
        candy = Candy()
        candy.visile = True
        self.assertEqual(
            str(candy),
            "🍭",
        )


class TestEnigma(unittest.TestCase):
    def test_init(self):
        engima = Enigma()
        self.assertIsNotNone(engima)
        self.assertFalse(engima.visile)

    def test__str__invisible(self):
        engima = Enigma()
        self.assertEqual(
            str(engima),
            "⬜️",
        )

    def test__str__visible(self):
        engima = Enigma()
        engima.visile = True
        self.assertEqual(
            str(engima),
            "❓",
        )


class TestGhost(unittest.TestCase):
    def test_init(self):
        ghost = Ghost()
        self.assertIsNotNone(ghost)
        self.assertFalse(ghost.visile)

    def test__str__invisible(self):
        ghost = Ghost()
        self.assertEqual(
            str(ghost),
            "⬜️",
        )

    def test__str__visible(self):
        ghost = Ghost()
        ghost.visile = True
        self.assertEqual(
            str(ghost),
            "👻",
        )


class TestCell(unittest.TestCase):
    def test_init(self):
        cell = Cell()
        self.assertIsNotNone(cell)
        self.assertFalse(cell.visile)


class TestHouse(unittest.TestCase):

    def test_init(self):
        house = House()
        self.assertEqual(len(house.cells), 4)
        for room_index in range(4):
            self.assertEqual(len(house.cells[room_index]), 4)

    @patch('random.randint', side_effect=[
        2, 3, 3, 1,
        1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1,
    ])
    def test_door_pos(self, randint_patched):
        house = House()
        self.assertIsInstance(
            house.cells[2][3],
            Door,
        )

    @patch('random.randint', side_effect=[
        2, 3, 3, 1,
        1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1,
    ])
    def test_character_pos(self, randint_patched):
        house = House()
        self.assertEqual(
            house.player_row,
            2,
        )
        self.assertEqual(
            house.player_col,
            3,
        )

    @patch('random.randint', side_effect=[
        2, 3,  # house
        2, 3,  # candy
        3, 1,  # candy
        1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1,
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

    @patch('random.randint', side_effect=[
        2, 3,  # house
        3, 1,  # candy
        0, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1,
    ])
    def test_ghosts_pos(self, randint_patched):
        house = House()
        self.assertIsInstance(
            house.cells[2][3],
            Door,
        )
        self.assertIsInstance(
            house.cells[3][1],
            Candy,
        )
        self.assertIsNone(
            house.cells[0][0]
        )
        self.assertIsInstance(
            house.cells[0][1],
            Ghost,
        )
        self.assertIsInstance(
            house.cells[3][3],
            Ghost,
        )

    @patch('random.randint', side_effect=[
        2, 3,  # house
        3, 1,  # candy
        0, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1,
    ])
    def test_ghosts_pos(self, randint_patched):
        house = House()
        self.assertEqual(
            str(house),
            (
                '⬜️⬜️⬜️⬜️\n' +
                '⬜️⬜️⬜️⬜️\n' +
                '⬜️⬜️⬜️😐\n' +
                '⬜️⬜️⬜️⬜️\n'
            )
        )

if __name__ == '__main__':
    unittest.main()
