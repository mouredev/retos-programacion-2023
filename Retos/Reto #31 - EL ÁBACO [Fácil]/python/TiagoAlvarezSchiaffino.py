abacus_numbers = {
    "O---OOOOOOOO": "1",
    "OO---OOOOOOO": "2",
    "OOO---OOOOOO": "3",
    "OOOO---OOOOO": "4",
    "OOOOO---OOOO": "5",
    "OOOOOO---OOO": "6",
    "OOOOOOO---OO": "7",
    "OOOOOOOO---O": "8",
    "OOOOOOOOO---": "9",
    "---OOOOOOOOO": "0"
}

def abacus_reader(abacus):
    """
    Read the number represented by the abacus.

    Args:
        abacus (list): List representing the abacus.

    Returns:
        int: The number represented by the abacus.
    """
    number = 0
    for element in abacus:
        if element in abacus_numbers:
            number = number * 10 + int(abacus_numbers[element])
    return number

if __name__ == "__main__":
    abacus_example = [
        "O---OOOOOOOO",
        "OOO---OOOOOO",
        "---OOOOOOOOO",
        "OO---OOOOOOO",
        "OOOOOOO---OO",
        "OOOOOOOOO---",
        "---OOOOOOOOO"
    ]

    result = abacus_reader(abacus_example)
    print(result)