import abc
from typing import TypeAlias
import functools


PythagoreanTripleList: TypeAlias = list[tuple[int, int, int]]


class PythagoreanCalculator(abc.ABC):
    @abc.abstractmethod
    def calculate(self, max_number: int) -> PythagoreanTripleList:
        pass


@functools.lru_cache
def calculate_pythagorean_triples(max_number: int) -> PythagoreanTripleList:
    triples = []
    c, m = 0, 2
    while c < max_number:
        for n in range(1, m):
            a = m * m - n * n
            b = 2 * m * n
            c = m * m + n * n
            if c > max_number:
                break
            triples += [(a, b, c)]
        m += 1

    return triples


class PythagoreanTriplesCalculator(PythagoreanCalculator):
    def calculate(self, max_number: int) -> PythagoreanTripleList:
        return calculate_pythagorean_triples(max_number=max_number)


def main(calculator: PythagoreanCalculator) -> None:
    max_number = 10
    result = calculator.calculate(max_number)
    print(f"Pythagorean triples up to {max_number}: {result}")


if __name__ == "__main__":
    calculator = PythagoreanTriplesCalculator()
    main(calculator=calculator)
