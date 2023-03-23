def fizzbuzz(n: int) -> None:
    # avoid recursion because of python's stack limit (1000)
    for i in range(1, n+1):
        match (i % 3 == 0, i % 5 == 0):
            case (True, True):
                print("fizzbuzz")
            case (True, False):
                print("fizz")
            case (False, True):
                print("buzz")
            case _:
                print(i)


def main() -> None:
    """
    Caution: this only runs on >=3.10
    PEP: https://peps.python.org/pep-0622/
    """
    n = 100
    fizzbuzz(n)


if __name__ == '__main__':
    main()
