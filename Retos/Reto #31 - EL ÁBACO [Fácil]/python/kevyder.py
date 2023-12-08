def abacus_reader(abacus: list[str]) -> int:
    result = [str(9 - len(units.split("-")[-1])) for units in abacus]
    return int("".join(result))


if __name__ == "__main__":
    abacus = [
        "O---OOOOOOOO",
        "OOO---OOOOOO",
        "---OOOOOOOOO",
        "OO---OOOOOOO",
        "OOOOOOO---OO",
        "OOOOOOOOO---",
        "---OOOOOOOOO",
    ]

    result = abacus_reader(abacus)
    print(result)
