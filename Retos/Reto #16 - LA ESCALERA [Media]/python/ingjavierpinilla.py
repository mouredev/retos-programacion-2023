def print_stair_up(n: int):
    print(" " * (2 * n), end="")
    print("_")
    for i in range((2 * n - 2), -1, -2):
        print(" " * i, end="")
        print("_|")


def print_stair_down(n: int):
    print("_")
    for i in range(1, (2 * n), 2):
        print(" " * i, end="")
        print("|_")


def print_stair(n: int):
    if n > 0:
        print_stair_up(n)
    elif n < 0:
        print_stair_down(-n)
    else:
        print("__")


if __name__ == "__main__":
    print_stair(-25)
