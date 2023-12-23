def main():
    print(rgb_to_hex(66, 135, 245))
    print(hex_to_rgb("4287f5"))


def to_hex(decimal_number: int):
    return hex(decimal_number)[2:]


def to_decimal(hex_number: str):
    return int(hex_number, 16)


def rgb_to_hex(red: int, green: int, blue: int):
    return f"#{to_hex(red)}{to_hex(green)}{to_hex(blue)}"


def hex_to_rgb(hex_number: str):
    color = tuple([to_decimal(hex_number[i:i + 2]) for i in (0, 2, 4)])

    return f"r: {color[0]}, g: {color[1]}, b: {color[2]}"


if __name__ == '__main__':
    main()
