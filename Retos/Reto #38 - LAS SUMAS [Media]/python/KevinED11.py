from typing import Optional, TypeAlias, Callable, Never
import functools
import itertools
import unittest


IntTuple: TypeAlias = tuple[int, ...]
OptionalIntTuple: TypeAlias = Optional[IntTuple]
ListOptionalIntTuple: TypeAlias = list[OptionalIntTuple]
FindCombinationsFunction: TypeAlias = Callable[[
    IntTuple, int], ListOptionalIntTuple]


class InvalidTargetNumberException(Exception):
    """
    Exception raised when the target number is invalid
    """

    pass


class InvalidNumbersException(Exception):
    """
    Exception raised when the numbers are invalid
    """

    pass


def raise_invalid_numbers_exception(msg: str) -> Never:
    """
    Raises an InvalidNumbersException with the specified message.
    """
    raise InvalidNumbersException(msg)


def raise_invalid_target_number_exception(msg: str) -> Never:
    """
    Raises an `InvalidNumbersException` with the provided message.
    """
    raise InvalidTargetNumberException(msg)


def is_valid_numbers_argument(numbers: IntTuple) -> bool:
    if not (
        isinstance(numbers, tuple)
        and len(numbers) > 1
        and all(isinstance(number, int) for number in numbers)
    ):
        return False

    return True


def is_valid_target_number_argument(target_number: int) -> bool:
    if target_number < 1:
        return False

    return True


def validate_find_combinations_function_arguments(
    numbers: IntTuple, target_number: int
) -> None:
    if not is_valid_target_number_argument(target_number):
        raise_invalid_target_number_exception(
            "Invalid target number, must be a positive integer."
        )

    if not is_valid_numbers_argument(numbers):
        raise_invalid_numbers_exception(
            "Invalid numbers, must be a tuple, with length > 1 and only contain integers."
        )


def validate_find_combinations_arguments(
    fn: FindCombinationsFunction,
) -> FindCombinationsFunction:
    """
    A decorator function that takes in a function and returns a wrapped version of that function.
    """

    @functools.wraps(wrapped=fn)
    def wrapper(numbers: IntTuple, target_number: int) -> ListOptionalIntTuple:
        validate_find_combinations_function_arguments(
            numbers=numbers, target_number=target_number
        )

        return fn(numbers, target_number)

    return wrapper


@functools.lru_cache(maxsize=None)
@validate_find_combinations_arguments
def find_combinations_with_integrated_function(
    numbers: IntTuple, target_number: int
) -> ListOptionalIntTuple:
    """
    Find all combinations of numbers that sum to target_number
    """
    return [
        comb
        for i in range(len(numbers))
        for comb in itertools.combinations(numbers, i)
        if sum(comb) == target_number
    ]


class TestFindCombinations(unittest.TestCase):
    def setUp(self) -> None:
        self.correct_result = find_combinations_with_integrated_function(
            (1, 5, 3, 2), 6
        )
        self.result_not_found = find_combinations_with_integrated_function(
            (1, 2, 3, 4), 20
        )

    def test_find_combinations_with_integrated_function(self) -> None:
        with self.subTest("Correct result"):
            self.assertEqual(
                self.correct_result,
                [(1, 5), (1, 3, 2)],
            )

        with self.subTest("Expected correct return type"):
            self.assertIsInstance(self.correct_result, list)
            for obj in self.correct_result:
                self.assertIsInstance(obj, tuple)
                for value in obj:
                    self.assertIsInstance(value, int)

        with self.subTest("Expected length of result"):
            self.assertEqual(len(self.correct_result), 2)

        with self.subTest("result not found"):
            self.assertEqual(self.result_not_found, [])

        with self.subTest("Incorrect target number argument"):
            with self.assertRaises(InvalidTargetNumberException):
                find_combinations_with_integrated_function((1, 2, 3, 4), -1)

        with self.subTest("Incorrect numbers argument"):
            with self.assertRaises(InvalidNumbersException):
                find_combinations_with_integrated_function((1,), 5)


def main() -> None:
    try:
        result = find_combinations_with_integrated_function((1, 5, 3, 2), 6)
        print(result)
    except (InvalidNumbersException, InvalidTargetNumberException) as err:
        print(err)


if __name__ == "__main__":
    main()
    unittest.main()
