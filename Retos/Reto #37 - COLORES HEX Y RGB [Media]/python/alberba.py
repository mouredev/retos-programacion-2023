
class Rgb:
    def __init__(self, r: int, g: int, b: int):
        self.r = r
        self.g = g
        self.b = b

hex_dict = {"0": 0, "1": 1, "2": 2, "3": 3, "4": 4,"5": 5, "6": 6, "7": 7, "8": 8, "9": 9, "A": 10,"B": 11, "C": 12, "D": 13, "E": 14, "F": 15}

def hex_to_rgb(hex: str):
    hex = hex.lstrip('#')
    for i in range(0, len(hex), 2):
        print(hex_dict.get(hex[i+1]) * 16 + hex_dict.get(hex[i]))

def rgb_to_hex(rgb: Rgb):
    print(f"#{hex(rgb.r)[2:]}{hex(rgb.g)[2:]}{hex(rgb.b)[2:]}")

hex_to_rgb("#FFFFFF")
rgb_to_hex(Rgb(255, 255, 255))
if __name__ == "__main__":
    input = input()
    if input[0] == "#":
        hex_to_rgb(input)
    else:
        rgb_to_hex(Rgb(int(input.split(" ")[0]), int(input.split(" ")[1]), int(input.split(" ")[2])))