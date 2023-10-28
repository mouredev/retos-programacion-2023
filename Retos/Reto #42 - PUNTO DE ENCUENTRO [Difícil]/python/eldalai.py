import unittest

# m = (y2 - y1) - (x2 - y1)
# y = m x + b

def calc_m(x, y, dx, dy):
    x1 = x
    x2 = x + dx
    y1 = y
    y2 = y + dy
    return (y2 - y1) / (x2 - x1)

def calc_b(x, y, m):
    # y = m x + b
    # b = y - m x
    return y - (m * x)

def join(x1, y1, dx1, dy1, x2, y2, dx2, dy2):
    m1 = calc_m(x1, y1, dx1, dy1)
    m2 = calc_m(x2, y2, dx2, dy2)
    if m1 == m2:
        raise Exception('Son paralelas')
    b1 = calc_b(x1, y1, m1)
    b2 = calc_b(x2, y2, m2)
    x = (b2 - b1) / (m1 - m2)
    y = m1 * x + b1
    return x, y

class TestPuntoEncuentro(unittest.TestCase):
    def test_calc_m(self):
        x = 3
        y = 2
        dx = 1
        dy = 2
        m = calc_m(x, y, dx, dy)
        self.assertEqual(m, 2.0)

    def test_calc_b(self):
        x = 3
        y = 2
        dx = 1
        dy = 2
        m = calc_m(x, y, dx, dy)
        b = calc_b(x, y, m)
        self.assertEqual(b, -4.0)

    def test_join_ok(self):
        x1 = 3
        y1 = 2
        dx1 = 2
        dy1 = 1
        x2 = 4
        y2 = 1
        dx2 = 1
        dy2 = 2
        resultx, resulty = join(x1, y1, dx1, dy1, x2, y2, dx2, dy2)
        self.assertEqual(resultx, 5.0)
        self.assertEqual(resulty, 3.0)

    def test_join(self):
        x1 = 3
        y1 = 7
        dx1 = 1
        dy1 = -1
        x2 = 4
        y2 = 1
        dx2 = 1
        dy2 = 1
        resultx, resulty = join(x1, y1, dx1, dy1, x2, y2, dx2, dy2)
        self.assertEqual(resultx, 6.5)
        self.assertEqual(resulty, 3.5)

    def test_join_error(self):
        x1 = 1
        y1 = 1
        dx1 = 1
        dy1 = 1
        x2 = 4
        y2 = 1
        dx2 = 1
        dy2 = 1
        with self.assertRaises(Exception):
            join(x1, y1, dx1, dy1, x2, y2, dx2, dy2)

def main():
    x1 = int(input("Coordenada x1: "))
    y1 = int(input("Coordenada y1: "))
    dx1 = int(input("Incremento x1: "))
    dy1 = int(input("Incremento y1: "))
    x2 = int(input("Coordenada x2: "))
    y2 = int(input("Coordenada y2: "))
    dx2 = int(input("Incremento x2: "))
    dy2 = int(input("Incremento y2: "))
    try:
        resultx, resulty = join(x1, y1, dx1, dy1, x2, y2, dx2, dy2)
        print(f"las rectas se unen en {resultx}, {resulty}")
    except Exception as e:
        print(str(e))


if __name__ == '__main__':
    main()
