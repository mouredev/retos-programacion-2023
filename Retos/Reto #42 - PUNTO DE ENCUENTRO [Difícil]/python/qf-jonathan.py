import unittest


class Object:
    def __init__(self, init_pos: tuple[float, float], move_vec: tuple[float, float]) -> None:
        self.init_pos = init_pos
        self.move_vec = move_vec

    def pos_at_time(self, time: float) -> tuple[float, float]:
        return (pos + vec * time for pos, vec in zip(self.init_pos, self.move_vec))

    def __str__(self) -> str:
        return f"Object(position{self.init_pos}, vector{self.move_vec})"


def meeting_point(
    obj_a: Object, obj_b: Object, epsilon: float = 1e-7
) -> tuple[tuple[float, float], float]:
    (ax, ay), (vax, vay) = obj_a.init_pos, obj_a.move_vec
    (bx, by), (vbx, vby) = obj_b.init_pos, obj_b.move_vec
    (dx, dy), (dvx, dby) = (bx - ax, by - ay), (vax - vbx, vay - vby)

    if abs(dvx) > epsilon and (tx := dx / dvx) >= 0:
        x, y = obj_a.pos_at_time(tx)
        _, yb = obj_b.pos_at_time(tx)
        if abs(y - yb) < epsilon:
            return (x, y), tx

    if abs(dby) > epsilon and (ty := dy / dby) >= 0:
        x, y = obj_a.pos_at_time(ty)
        xb, _ = obj_b.pos_at_time(ty)
        if abs(x - xb) < epsilon:
            return (x, y), ty

    return (None, None), float("inf")


class TestMeetingPoint(unittest.TestCase):
    def assertMeetAt(
        self,
        result: tuple[tuple[float, float], float],
        expected: tuple[tuple[float, float], float],
        msg: str,
    ):
        (x, y), time = result
        (expected_x, expected_y), expected_time = expected
        self.assertAlmostEqual(x, expected_x, msg=msg)
        self.assertAlmostEqual(y, expected_y, msg=msg)
        self.assertAlmostEqual(time, expected_time, msg=msg)

    def assertNotMeet(self, result: tuple[tuple[float, float], float], msg: str):
        (x, y), time = result
        self.assertIsNone(x, msg=msg)
        self.assertIsNone(y, msg=msg)
        self.assertEqual(time, float("inf"), msg=msg)

    def test_objects_meet(self):
        cases = {
            (((0, 0), (2, 2)), ((1, 1), (-2, -2))): ((0.5, 0.5), 0.25),
            (((0, 0), (1, 1)), ((5, 0), (-1, 1))): ((2.5, 2.5), 2.5),
            (((0, 0), (1, 1)), ((0, 5), (1, -1))): ((2.5, 2.5), 2.5),
            (((2.001, 1.001), (1, 1)), ((2.001, 1.001), (-1, -1))): ((2.001, 1.001), 0),
            (((0, 0), (1.01, 1.01)), ((1, 1), (1, 1))): ((101, 101), 100),
            (((5, 5), (0.0001, -10000)), ((6, 5), (-0.0001, -10000))): ((5.5, -49999995), 5000),
            (((123, 726), (6, 9)), ((100023, 667547), (-4, -57.74884884885))): (
                (60063, 90636),
                9990,
            ),
            (((-1000000, 1000000), (100, -1)), ((1000000, -1000000), (-1, 100))): (
                (980198.019802, 980198.019802),
                19801.980198,
            ),
        }

        for (obj_a_params, obj_b_params), expected in cases.items():
            obj_a = Object(*obj_a_params)
            obj_b = Object(*obj_b_params)
            result = meeting_point(obj_a, obj_b)
            self.assertMeetAt(result, expected, msg=f"{obj_a} does not meet {obj_b} at {result}")

    def test_object_not_meet(self):
        cases = [
            (((0, 0), (1, 1)), ((5, 5), (1, 1))),
            (((0, 0), (0.99, 0.99)), ((1, 1), (1, 1))),
            (((0, 1), (0, 1)), ((0, 0), (0, -1))),
            (((123, 726), (6, 9)), ((100023, 667547), (-4, -57.75))),
        ]

        for obj_a_params, obj_b_params in cases:
            obj_a = Object(*obj_a_params)
            obj_b = Object(*obj_b_params)
            result = meeting_point(obj_a, obj_b)
            self.assertNotMeet(result, msg=f"{obj_a} should not not meet {obj_b}")


if __name__ == "__main__":
    unittest.main()
