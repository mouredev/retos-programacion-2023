"""This script shows the solution to exercise "Reto #0: EL FAMOSO FIZZ BUZZ" from Brais Moure's official website."""

from typing import Union


def main() -> None:
    """
    Main function of the program. This function iterates numbers from 1 to 100 and prints on the console each number after being verified.
    """
    for n in range(1, 101):
        print(f"{verifier(n)}")


def verifier(n: int) -> Union[int, str]:
    """
    This function checks whether a number is a multiple of 3, 5 or both.

    Parameters:
        n (int): number to check

    Returns:
        Union[int,str] if number is a multiple of 3, 5 or both, "fizz", "buzz" or "fizzbuzz" is returned respectively. In other cases, the original number is returned.
    """
    result = ""
    if n % 3 == 0:
        result += "fizz"
    if n % 5 == 0:
        result += "buzz"
    return result if result else n


if __name__ == "__main__":
    main()
