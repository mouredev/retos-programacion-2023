import unittest

def pythagorean_triples(number: int) -> list[tuple[int, int, int]]:
    numbers = list(range(1, number + 1))
    triples = []
    for i, n in enumerate(numbers):
        for m in numbers[i + 1::]:
            result = (n**2 + m**2) ** 0.5
            if int(result) in numbers and result.is_integer():
                triples.append((n, m, int(result)))
    return triples

# Simple Test Cases
class TestPythagoreanTriples(unittest.TestCase):

    def test_with_small_range(self):
        # Test with a small range of numbers
        result = pythagorean_triples(10)
        expected = [(3, 4, 5), (6, 8, 10)]
        self.assertEqual(result, expected)

    def test_with_large_range(self):
        # Test with a larger range of numbers
        result = pythagorean_triples(20)
        expected = [(3, 4, 5), (5, 12, 13), (6, 8, 10), (8, 15, 17), (9, 12, 15), (12, 16, 20)]
        self.assertEqual(result, expected)

    def test_with_no_triples(self):
        # Test when there are no Pythagorean triples in the range
        result = pythagorean_triples(2)
        expected = []
        self.assertEqual(result, expected)


if __name__ == "__main__":
    unittest.main()
