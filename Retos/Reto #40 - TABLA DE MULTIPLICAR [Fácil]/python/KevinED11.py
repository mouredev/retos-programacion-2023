from typing import Protocol


class MultiplicationTableWriterFn(Protocol):
    def __call__(self, number: int) -> None:
        ...


def validate_user_input(func: MultiplicationTableWriterFn) -> MultiplicationTableWriterFn:
    def wrapper(number: int) -> None:
        if number < 1:
            raise ValueError("Number must be greater than 0")
        func(number)

    return wrapper


def read_input() -> int:
    try:
        return int(input("Enter a number: "))
    except ValueError:
        raise


@validate_user_input
def write_multiplication_table_to_console(number: int) -> None:
    count = 1
    while count <= 10:
        print(f"{number} x {count} = {number * count}")
        count += 1


def main(writer_fn: MultiplicationTableWriterFn) -> None:
    user_input = read_input()
    writer_fn(user_input)


if __name__ == "__main__":
    main(write_multiplication_table_to_console)
