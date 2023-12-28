class Convertion():
    def __init__(self, decimal):
        self.decimal = decimal
        self.hexadecimal = {"0000": '0', "0001": '1', "0010": '2', "0011": '3', "0100": '4', "0101": '5', "0110": '6', "0111": '7', "1000": '8', "1001": '9', "1010": 'A', "1011": 'B', "1100": 'C', "1101": 'D', "1110": 'E', "1111": 'F'}

    
    def sdivision(self, divisor):
        number = self.decimal
        convertion = ""

        while number >= 1:
            convertion = str((number % divisor)) + convertion
            number = int(number / divisor)

        return convertion


    def to_hexadecimal(self):
        number = self.sdivision(2)
        hexadecimal = ""

        while not len(number) % 4 == 0:
            number = '0' + number

        for index in range(0, len(number), 4):
            value = number[index: index + 4]

            if value in self.hexadecimal.keys():
                hexadecimal += self.hexadecimal[value]

        return hexadecimal
    

    def to_octal(self):
        return self.sdivision(8)
    

cvn1 = Convertion(362)
print(f"Decimal: {cvn1.decimal}, hexadecimal: {cvn1.to_hexadecimal()}, octal: {cvn1.to_octal()}.")

cvn2 = Convertion(110)
print(f"Decimal: {cvn2.decimal}, hexadecimal: {cvn2.to_hexadecimal()}, octal: {cvn2.to_octal()}.")

cvn3 = Convertion(47)
print(f"Decimal: {cvn3.decimal}, hexadecimal: {cvn3.to_hexadecimal()}, octal: {cvn3.to_octal()}.")
