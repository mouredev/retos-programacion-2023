def main():
    print(get_ternas(10))


def get_ternas(numero: int) -> list:

    ternas = []

    for m in range(1, numero//2):
        for n in range(1, numero//2):
            if m > n:
                a = m**2 - n**2
                b = 2*m*n
                c = m**2 + n**2

                if check_triple_pitagorico(a, b, c) and c <= numero:
                    ternas.append((a, b, c))

    return ternas


def check_triple_pitagorico(a: int, b: int, c: int) -> bool:
    if c**2 == a**2 + b**2:
        return True

    return False


if __name__ == "__main__":
    main()
