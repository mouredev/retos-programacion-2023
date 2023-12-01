class HEX:
    def __init__(self, hex_color: str) -> None:
        self.hex_color = hex_color.upper()

    def __hex_to_decimal(self, hex: str) -> int:
        return int(hex, 16)

    def convert_to_rgb(self) -> tuple:
        self.red, self.green, self.blue = [
            self.__hex_to_decimal(self.hex_color[i : i + 2])
            for i in range(0, len(self.hex_color), 2)
        ]
        return (self.red, self.green, self.blue)

    def __str__(self) -> str:
        return f"#{self.hex_color}"


class RGB:
    def __init__(self, *rgb_color) -> None:
        self.red, self.green, self.blue = rgb_color

    def convert_to_hex(self) -> str:
        hex_list = [f"{val:02X}" for val in (self.red, self.green, self.blue)]
        hex_color = "".join(hex_list)
        return hex_color

    def __str__(self) -> str:
        return f"RGB({self.red}, {self.green}, {self.blue})"


if __name__ == "__main__":
    hex_color = HEX(hex_color="A74CE1")
    rgb_result = hex_color.convert_to_rgb()
    print(hex_color, rgb_result, sep="=")

    rgb_color = RGB(*rgb_result)
    hex_result = rgb_color.convert_to_hex()
    print(rgb_color, hex_result, sep="=")
