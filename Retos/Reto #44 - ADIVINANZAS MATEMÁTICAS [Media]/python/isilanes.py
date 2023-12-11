import asyncio
from enum import Enum
import random


TIMEOUT_SECONDS = 3.0


class Operation(Enum):
    ADDITION = "+"
    SUBTRACTION = "-"
    MULTIPLICATION = "*"
    DIVISION = "/"

    def run(self, first: int, second: int) -> int | float:
        if self == self.ADDITION:
            return first + second

        if self == self.SUBTRACTION:
            return first - second

        if self == self.MULTIPLICATION:
            return first * second

        if self == self.DIVISION:
            return first / second


def stage_to_digits(successes: int) -> tuple[int, int]:
    """
    Given an amount of correctly answered questions so far 'successes', return how many digits (at most)
    should the first and the second numbers have.

    The rule is that for stage = 0, both numbers should have 1 digit. Then, every
    5 questions, the maximum digits of one of the numbers should increase in 1,
    starting with the first number, and alternating. So, on stage 5 add a second
    digit to first number, then on stage 10 second digit to second number, then
    on stage 15 a third digit to the first number, etc.

    Args:
        successes (int):
            The amount of correct answers so far.

    Returns:
        Tuple of two integers, denoting maximum amount of digits for first and second numbers.
    """
    digits_first = (successes + 15) // 10
    digits_second = (successes + 10) // 10

    return digits_first, digits_second


def digits_to_random_value(digits: int) -> int:
    """
    Given an amount of digits, return a random integer with, at most,
    that many digits. I.e., if 'digits' is 2, then a random value
    between 1 and 99 (included) should be returned.

    Args:
        digits (int):
            Maximum amount of digits of return value.

    Returns:
        Random positive integer with at most 'digits' digits.
    """
    return random.randrange(0, 10**digits)


def response_is_correct(response: int | float, result: int | float) -> bool:
    """
    Given a user-input response 'response', and an expected result 'result',
    return whether they are the same (or close enough).

    Args:
        response (int or float):
            The number given by the user.
        result (int or float):
            The correct result expected.

    Returns:
        Boolean. Whether the two input numbers are equal, or not.
    """
    return abs(response - result) < 10**-3


async def main():
    """
    Run the main program.
    """
    print("Enter the solution for the following operations.")
    print("Provide up to 3 decimal places for non-integer solutions.")
    print("Press Enter to start...")
    input()

    there_was_timeout = False

    correct_answers = 0
    while True:
        digits_first, digits_second = stage_to_digits(correct_answers)
        first = digits_to_random_value(digits_first)
        second = digits_to_random_value(digits_second)
        operator = random.choice(list(Operation))

        if operator == Operation.DIVISION and second == 0:
            second = 1  # avoid division by 0

        prompt = f"{first} {operator.value} {second} = "
        result = operator.run(first, second)

        print(prompt)

        try:
            response = await asyncio.wait_for(
                asyncio.to_thread(input),
                timeout=TIMEOUT_SECONDS,
            )
            response = float(response.strip())
        except asyncio.TimeoutError:
            print(f"\n[TIMEOUT] Your {TIMEOUT_SECONDS} seconds run out!")
            there_was_timeout = True
            break

        if not response_is_correct(response, result):
            # The problem is unclear regarding how to handle errors. It states that the game
            # must end if a timeout is met. However, it doesn't say the same thing for incorrect answers.
            print(f"[ERROR] You provided {response:.3f}, but the correct result is {result:.3f}")
            continue

        correct_answers += 1

    print(f"You gave the correct answer to {correct_answers} questions.")

    # For some reason, when the user-input timeout is reached, input() is still
    # waiting for a newline or something, and the user has to press enter to proceed.
    if there_was_timeout:
        print("Press Enter to exit...")


if __name__ == "__main__":
    asyncio.run(main())
