def triples(x: int) -> list[int]:
    res = []
    for i in range(1, x + 1):
        for j in range(i + 1, x + 1):
            act = i**2 + j**2
            if int(act**0.5) == act**0.5 and act**0.5 > j and act**0.5 <= x:
                res.append([i, j, int(act**0.5)])
    return res


# O(n^2)
def main():
    print("Triples pitagoricos hasta 10")
    print(*triples(10))
    print("Triples pitagoricos hasta 15")
    print(*triples(15))
    print("Triples pitagoricos hasta 20")
    print(*triples(20))
    print("Triples pitagoricos hasta 100")
    print(*triples(100))


if __name__ == "__main__":
    main()
