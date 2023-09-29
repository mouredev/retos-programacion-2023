def print_trifuerza(n: int) -> None:
    longitud = 2 * n

    for i in range(1, n + 1):
        text = "*" * (2 * i - 1)
        text = text.center(longitud * 2)
        print(text)

    for i in range(1, n + 1):
        text = "*" * (2 * i - 1)
        text = text.center(longitud)
        text = text * 2
        print(text)


def main():
    n = int(input("Ingrese el nivel de su Trifuerza: "))
    print_trifuerza(n)


if __name__ == "__main__":
    main()
