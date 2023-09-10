from itertools import permutations


def permutaciones(palabra: str):
    permutaciones = permutations(palabra)
    for p in permutaciones:
        print("".join(p))


def _permutaciones(palabra):
    n = len(palabra)
    for i in range(n):
        for j in range(i, n):
            palabra[i], palabra[j] = palabra[j], palabra[i]
            yield "".join(palabra)
            palabra[i], palabra[j] = palabra[j], palabra[i]


def permute(data, i, length):
    if i == length:
        print("".join(data))
    else:
        for j in range(i, length):
            # swap
            data[i], data[j] = data[j], data[i]
            permute(data, i + 1, length)
            data[i], data[j] = data[j], data[i]


def main():
    palabra = "sol"
    permutaciones(palabra)

    print("==" * 20)

    n = len(palabra)
    data = list(palabra)
    permute(data, 0, n)


if __name__ == "__main__":
    main()
