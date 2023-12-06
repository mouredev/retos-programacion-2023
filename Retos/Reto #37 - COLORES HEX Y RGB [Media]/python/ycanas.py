class Color():

    def __init__(self):
        self.__hexadecimal = {
            0:  '0', 1:  '1', 2:  '2', 3:  '3',
            4:  '4', 5:  '5', 6:  '6', 7:  '7',
            8:  '8', 9:  '9', 10: 'A', 11: 'B',
            12: 'C', 13: 'D', 14: 'E', 15: 'F',
        }

        self.__decimal = {self.__hexadecimal[key]: key for key in self.__hexadecimal}


    def toHEX(self, RGB):
        HEX = "#"

        for channel in RGB:
            if channel in range(0, 16):
                HEX = HEX + '0' + self.__hexadecimal[channel]
        
            else:
                 C = int(channel / 16)
                 R = channel % 16
                 HEX = HEX + self.__hexadecimal[C] + self.__hexadecimal[R]

        return HEX
    

    def toRGB(self, HEX):
        RGB = []

        for i in range(3):
            numbers = HEX[(i * 2) + 1: ((i + 1) * 2) + 1]
            dec = self.__decimal[numbers[0]] * 16 + self.__decimal[numbers[1]]
            RGB.append(dec)

        return RGB
    

color = Color()

print(color.toHEX([255, 255, 255]))
print(color.toHEX([36,  89,  194]))
print(color.toHEX([5,   231, 167]))
print(color.toRGB("#FF6B9C"))
print(color.toRGB("#898989"))
print(color.toRGB("#23FFAF"))
