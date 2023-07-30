from termcolor import colored

def uppercase_decorator(func):
    def wrapper(*args, **kwargs):
        result = func(*args, **kwargs)
        return colored(result.upper(), 'green')
    return wrapper

class T9Converter:
    def __init__(self, input_t9):
        self.input_t9 = input_t9
        self.t9_mapping = {
            '2': 'ABC', '3': 'DEF', '4': 'GHI',
            '5': 'JKL', '6': 'MNO', '7': 'PQRS',
            '8': 'TUV', '9': 'WXYZ'
        }

    @uppercase_decorator
    def convert(self):
        result_text = ''
        blocks = self.input_t9.split('-')

        for block in blocks:
            if block and block.isdigit():
                digit = block[0]
                count = len(block)
                if digit in self.t9_mapping:
                    index = (count - 1) % len(self.t9_mapping[digit])
                    result_text += self.t9_mapping[digit][index]
                else:
                    result_text += digit

        return result_text

if __name__ == "__main__":
    input_t9 = "6-2-66-88-33-555"

    t9_converter = T9Converter(input_t9)
    converted_text = t9_converter.convert()

    print("Salida:", converted_text)




