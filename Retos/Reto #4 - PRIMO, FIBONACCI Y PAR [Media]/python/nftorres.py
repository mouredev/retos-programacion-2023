"""This script shows the solution to the exercise "Reto #4: PRIMO, FIBONACCI Y PAR" from Brais Moure's official website."""


class Number:
    """This class represents a number with methods to describe whether it is prime, fibonacci and even."""

    def __init__(self, number: int) -> None:
        """This method initializes the attributes of the number.

        Args:
            number (int): number
        """
        self.number: int = number
        self.prime: bool = False
        self.fibonacci: bool = False
        self.even: bool = False

    def is_prime(self) -> None:
        """This method checks if the number is prime."""
        self.factors: list = [
            f for f in range(1, (self.number + 1)) if self.number % f == 0
        ]
        self.prime = (
            True
            if (len(self.factors) == 2)
            and (1 in self.factors)
            and (self.number in self.factors)
            else False
        )

    def is_fibonacci(self) -> None:
        """This method checks if the number belongs to the fibonacci series."""
        self.fibonacci_series: list = [0, 1]
        for f in self.fibonacci_series:
            sum: int = self.fibonacci_series[-1] + self.fibonacci_series[-2]
            self.fibonacci_series.append(sum)
            if f <= self.number:
                self.fibonacci = True if self.number in self.fibonacci_series else False
            else:
                break

    def is_even(self) -> None:
        """This method checks if the number is even."""
        self.even = True if (-1) ** self.number > 0 else False

    def describe_number(self) -> str:
        """This method elaborates the description of the number.

        Returns:
            str: the description of the number.
        """
        self.description: str = f"{self.number} "

        self.description += "es primo" if self.prime else "no es primo"
        self.description += ", fibonacci" if self.fibonacci else ", no es fibonacci"
        self.description += " y es par" if self.even else " y es impar"

        return self.description


if __name__ == "__main__":
    # Initializing the program
    print("\nNúmeros by nftorres")
    number = Number(int(input("\nIngresa un número: ")))
    # Validating if the number is prime, fibonacci and odd or even.
    number.is_prime()
    number.is_fibonacci()
    number.is_even()
    # Displays the description of the number.
    print(number.describe_number())
