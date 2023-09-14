def draw_tri(n: int):
    size = 2 * n - 1
    sep = " " * n
    for i in range(n - 1):
        string = " " * (n - 1 - i)
        string += "*"
        if i != 0:
            string = f'{string}{" " * (2 * i - 1)}*'
        print(f'{sep}{string}')
    final = f'{sep}{"*" * size}'
    print(final)


def draw_2_tri(n: int):
    size = 2 * n - 1
    for i in range(n - 1):
        string = f'{" " * (n - 1 - i)}*'
        if i != 0:
            string = f'{string}{" " * (2 * i - 1)}*'
        sep = " " * (size + 1 - len(string))
        print(f"{string}{sep}{string}")
    final = "*" * size
    print(f"{final} {final}")


def triforce(n: int):
    draw_tri(n)
    draw_2_tri(n)


triforce(3)
