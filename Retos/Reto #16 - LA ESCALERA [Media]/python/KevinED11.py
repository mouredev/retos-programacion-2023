def number_stairs() -> int:
    try:
      return int(input("Place number stairts to write: "))
    except ValueError:
        raise ValueError("Place a integer number")


def mode_draw_stair(number: int = 4) -> str:
    return "ascendente" if number > 0 else "descendente" if number < 0 else "zero"


def print_stair(number_stair: int, mode: str) -> None:
    if mode == "zero":
        print("__")
        return
    elif mode == "ascendente":
        for i in range(1, number_stair + 1):
            print(" "*(number_stair-i) + "_"*i + "|")
        return
    elif mode == "descendente":
        for i in range(1, abs(number_stair) + 1):
            print(" " * (i - 1) + "_" * (abs(number_stair) - i + 1) + "|")

        return


def main() -> None:
    number_stairs_to_draw = number_stairs()
    mode = mode_draw_stair(number_stairs_to_draw)
    print(f"{mode=}")

    print_stair(number_stairs_to_draw, mode=mode)


if __name__ == "__main__":
    main()
