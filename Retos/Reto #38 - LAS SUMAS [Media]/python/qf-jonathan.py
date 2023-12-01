import unittest


def sum_to(arr: list[int], target: int) -> list[list[int]]:
    ans, st, sarr = [], [(0, [], target)], sorted(arr)
    while st:
        start, comb, rest = st.pop()
        if rest == 0:
            ans.append(comb)
        for i in range(start, len(sarr)):
            if (
                i < len(sarr)
                and (i <= start or sarr[i] != sarr[i - 1])
                and sarr[i] <= rest
            ):
                st.append((i + 1, comb + [sarr[i]], rest - sarr[i]))
    return sorted(ans)


class SumToTestCase(unittest.TestCase):
    def test_simple(self):
        self.assertEqual(sum_to([1, 5, 3, 2], 6), [[1, 2, 3], [1, 5]])
        self.assertEqual(
            sum_to([1, 2, 1, 1, 1, 1, 2, 1], 6),
            [[1, 1, 1, 1, 1, 1], [1, 1, 1, 1, 2], [1, 1, 2, 2]],
        )
        self.assertEqual(
            sum_to([1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 1, 2], 77),
            [
                [1, 1, 2, 2, 3, 5, 6, 7, 8, 9, 10, 11, 12],
                [1, 1, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12],
                [1, 2, 2, 4, 5, 6, 7, 8, 9, 10, 11, 12],
                [2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12],
            ],
        )

    def test_stress(self):
        self.assertEqual(len(sum_to([i + 1 for i in range(20)], 33)), 378)
        self.assertEqual(len(sum_to([i + 1 for i in range(30)], 77)), 39687)


if __name__ == "__main__":
    unittest.main()
