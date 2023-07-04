import time


class NegativeNumberError(Exception):
    def __init__(self, message: str) -> None:
        super().__init__(message)


def countdown(initial_count: int = 10, pause_duration: int = 1) -> None:
    if not isinstance(initial_count, int) or not isinstance(pause_duration, int):
        raise TypeError("Only integers numbers are allowed")
    
    if initial_count < 0 or pause_duration < 0:
        raise NegativeNumberError("Negative numbers are not allowed")

    while initial_count >= 0:
        print(initial_count)
        if initial_count == 0:
            break

        initial_count -= 1

        time.sleep(pause_duration)


def main() -> None:
    try:
        countdown(initial_count=10, pause_duration=2)
    except (NegativeNumberError, TypeError) as e:
        print(e)


if __name__ == "__main__":
    main()
