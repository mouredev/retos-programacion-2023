import argparse


class Convert:
    """Class that gets a number in the constructor method and can convert from decimal to octal and hexadecimal
        * Usage: python3 orazioc17.py {number_to_convert}
    """
    __octal = 8
    __hexadecimal = 16
    __hex_dict = {
        0: '0', 1: '1', 2: '2', 3: '3', 4: '4', 5: '5', 6: '6', 7: '7', 8: '8', 9: '9', 10: 'A', 11: 'B',
        12: 'C', 13: 'D', 14: 'E', 15: 'F'
    }

    def __init__(self, number: int):
        self.number = number

    def __convertion_process(self, base: int) -> int | str:
        """Apply the loops here to follow the principle DRY

           Base will be 8 when converting to octal and 16 when converting to hexadecimal
        """

        number = self.number

        number_list = []
        while (number / base != 0):
            quotient = int(number / base)
            remainder = int(number % base)
            number = quotient
            number_list.append(str(remainder)) if base == 8 else number_list.append(
                self.__hex_dict[remainder])

        number_list.reverse()
        return int(''.join(number_list)) if base == 8 else ''.join(number_list)

    def convert(self) -> tuple[int, str]:
        """Method to return both convertions, first the octal and then the hexadecimal"""
        return self.__convertion_process(self.__octal), self.__convertion_process(self.__hexadecimal)

    @property
    def get_octal(self) -> int:
        """Method to get only the octal as a property"""
        return self.__convertion_process(self.__octal)

    @property
    def get_hex(self) -> str:
        """Method to get only the hex as a property"""
        return self.__convertion_process(self.__hexadecimal)

    def __str__(self) -> str:
        """Method to return both convertions as a formatted string"""
        return f'Octal: {self.__convertion_process(self.__octal)}, Hex: {self.__convertion_process(self.__hexadecimal)}'


parser = argparse.ArgumentParser(
    prog='DecimalConverter',
    description='Find the Octal and the Hexadecimal of a decimal number. Usage: python3 orazioc17.py {number_to_convert}',
    epilog='Program to convert a decimal number to octal and hexadecimal'
)

parser.add_argument(
    'number',
    type=int,
    help='The number that will be converted'
)


if __name__ == '__main__':

    # Receiving the number
    args = parser.parse_args()
    convert = Convert(args.number)
    print(convert)  # Printing the already formatted string with the results
