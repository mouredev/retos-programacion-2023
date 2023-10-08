import unittest


def pythagorean_tiples(k: int):
    base_triples, all_triples, m = [], set(), 2
    while m * m < k:
        n, c = 1, 0
        while n < m and (c := m * m + n * n) <= k:
            a, b = m * m - n * n, 2 * m * n
            base_triples.append(sorted([a, b, c]))
            n += 1
        m += 1

    for a, b, c in base_triples:
        all_triples.update([(a * i, b * i, c * i) for i in range(1, k // c + 1)])

    return sorted(all_triples)


class TestPitagoreanTripple(unittest.TestCase):
    def test_basic(self):
        self.assertEqual(pythagorean_tiples(10), [(3, 4, 5), (6, 8, 10)])
        self.assertEqual(
            pythagorean_tiples(15), [(3, 4, 5), (5, 12, 13), (6, 8, 10), (9, 12, 15)]
        )
        self.assertEqual(
            pythagorean_tiples(17),
            [(3, 4, 5), (5, 12, 13), (6, 8, 10), (8, 15, 17), (9, 12, 15)],
        )
        self.assertEqual(
            pythagorean_tiples(20),
            [
                (3, 4, 5),
                (5, 12, 13),
                (6, 8, 10),
                (8, 15, 17),
                (9, 12, 15),
                (12, 16, 20),
            ],
        )

    def test_stress(self):
        self.assertEqual(len(pythagorean_tiples(100)), 52)
        self.assertEqual(len(pythagorean_tiples(1000)), 881)
        self.assertEqual(len(pythagorean_tiples(10000)), 12471)
        self.assertEqual(len(pythagorean_tiples(100000)), 161436)
        self.assertEqual(len(pythagorean_tiples(123456)), 203405)


if __name__ == "__main__":
    unittest.main()
