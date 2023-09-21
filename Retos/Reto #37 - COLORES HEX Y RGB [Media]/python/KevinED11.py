from typing import Callable, Self
from abc import ABC, abstractmethod


RGB = tuple[int, int, int]
HEX = str


class HexColorFormatError(Exception):
    pass


class RGBColorFormatError(Exception):
    pass


class ValidateRGBColorFormat:
    def __init__(self, fn: Callable[[Self, RGB], HEX]) -> None:
        self.fn = fn

    def __call__(self, color: RGB) -> HEX:
        if not (
            isinstance(color, tuple)
            and len(color) == 3
            and all(isinstance(value, int) 
                    and 0 <= value <= 255 for value in color)
        ):
            raise RGBColorFormatError(
                f"Invalid RGB color format: {color}, correct format is (r, g, b)"
            )

        return self.fn(self, color)


class ValidateHEXColorFormat:
    def __init__(self, fn: Callable[[Self, HEX], RGB]) -> None:
        self.fn = fn

    def __call__(self, color: HEX) -> RGB:
        if not (isinstance(color, str) and color.startswith("#") and len(color) == 7):
            raise HexColorFormatError(
                f"Invalid HEX color format: {color}, correct format is #RRGGBB"
            )

        return self.fn(self, color)


class IRGBConverter(ABC):
    @ValidateRGBColorFormat
    @abstractmethod
    def convert(self, color: RGB) -> HEX:
        pass


class IHEXConverter(ABC):
    @ValidateHEXColorFormat
    @abstractmethod
    def convert(self, color: HEX) -> RGB:
        pass


class HexToRGBConverter(IHEXConverter):
    @ValidateHEXColorFormat
    def convert(self, color: HEX) -> RGB:
        return tuple(int(color[i: i + 2], 16) for i in (1, 3, 5))


class RGBToHexConverter(IRGBConverter):
    @ValidateRGBColorFormat
    def convert(self, color: RGB) -> HEX:
        r, g, b = color
        return f"#{r:02x}{g:02x}{b:02x}"


class Main:
    @staticmethod
    def run() -> None:
        rgb_converter = RGBToHexConverter()
        hex_converter = HexToRGBConverter()

        result = rgb_converter.convert((255, 0, 0))
        print(result)

        result2 = hex_converter.convert("#FF0000")
        print(result2)


if __name__ == "__main__":
    Main.run()
