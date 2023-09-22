#!/usr/bin/env python3

class RGBColor:
    def __init__(self, red, green, blue):
        self.r = red
        self.g = green
        self.b = blue

    def __str__(self):
        return "r: {}, g: {}, b: {}".format(str(self.r), str(self.g), str(self.b))

    def convert(self):
        hex = 0
        hex = (self.r << 16)
        hex |= (self.g << 8)
        hex |= (self.b)
        return HexColor(hex)

class HexColor:
    def __init__(self, hex):
        self.h = hex

    def __str__(self):
        return "#{:06X}".format(self.h)

    def convert(self):
        b = self.h & 0xff
        g = (self.h >> 8) & 0xff
        r = (self.h >> 16) & 0xff

        return RGBColor(r, g, b)

if __name__ == "__main__":
    rgb1 = RGBColor(0xFE,0x14,0x56)
    print(rgb1)

    hex1 = HexColor(0xFE1456)
    print(hex1)

    print(hex1.convert())
    print(rgb1.convert())
