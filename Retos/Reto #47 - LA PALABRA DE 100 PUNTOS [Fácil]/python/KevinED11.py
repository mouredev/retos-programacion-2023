from typing import Protocol
import dataclasses


def score() -> dict[str, int]:
    spanish_alphabet = "abcdefghijklmnñopqrstuvwxyz"
    return {letter: i + 1 for i, letter in enumerate(spanish_alphabet)}


def calculate_points(word: str) -> int:
    if not word.isalpha():
        raise ValueError("\nLa palabra debe contener solo letras.")

    points = score()
    return sum(points[letter] for letter in word.lower())


class PointCalculator(Protocol):
    def __call__(self, word: str) -> int:
        ...


@dataclasses.dataclass
class Program:
    point_calculator: PointCalculator

    def calculate(self) -> None:
        target_score = 100
        while True:
            word = input("Introduce una palabra: ")
            try:
                result = self.point_calculator(word=word)
            except ValueError as e:
                print(e)
                continue

            print(f"La palabra '{word}' tiene {result} puntos.")

            if result == target_score:
                print("¡Felicidades! Has alcanzado o superado los 100 puntos.")
                break


class Main:
    @staticmethod
    def run() -> None:
        program = Program(point_calculator=calculate_points)
        program.calculate()


if __name__ == "__main__":
    Main.run()
