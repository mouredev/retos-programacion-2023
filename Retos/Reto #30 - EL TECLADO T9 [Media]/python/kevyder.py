KEY_MAPPING = [
    [" "],
    [",", ".", "?", "!"],
    ["A", "B", "C"],
    ["D", "E", "F"],
    ["G", "H", "I"],
    ["J", "K", "L"],
    ["M", "N", "O"],
    ["P", "Q", "R", "S"],
    ["T", "U", "V"],
    ["W", "X", "Y", "Z"],
]


def t9_interpeter(input: str) -> str:
    output = str()
    for block in input.split("-"):
        number = int(block[0])
        index = len(block) - 1
        char = KEY_MAPPING[number][index]
        output += char

    return output


if __name__ == "__main__":
    test_case = "6-666-88-777-33-3-33-888"
    output = t9_interpeter(test_case)
    print(output)
