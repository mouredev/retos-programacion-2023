def times_tables(number: int) -> str:
    result = []

    for n in range(1, 11):
        result.append(f"{number} x {n} = {n * number}")

    return "\n".join(result)


if __name__ == "__main__":
    multiplications = times_tables(5)
    print(multiplications)
