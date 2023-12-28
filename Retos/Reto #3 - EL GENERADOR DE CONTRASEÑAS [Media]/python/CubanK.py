#!/usr/bin/env python3
# -*- coding: utf-8 -*-

# Reto #3: EL GENERADOR DE CONTRASEÑAS
# /**
#  * Escribe un programa que sea capaz de generar contraseñas de forma aleatoria.
#  * Podrás configurar generar contraseñas con los siguientes parámetros:
#  * - Longitud: Entre 8 y 16.
#  * - Con o sin letras mayúsculas.
#  * - Con o sin números.
#  * - Con o sin símbolos.
#  * (Pudiendo combinar todos estos parámetros entre ellos)
#   */


from os import name, system
from time import sleep
from random import randrange, choice
from string import ascii_letters, ascii_lowercase, digits, punctuation


def clear():
    if name == 'nt':
        system('cls')
    else:
        system('clear')
    # sleep(1)



class Generator():
    def __init__(self, min_len: int = 8, max_len: int = 16, capital: bool = True, numbers: bool = True, symbols: bool = True) -> None:
        self.__min_len = min_len
        self.__max_len = max_len
        self.__capital = capital
        self.__numbers = numbers
        self.__symbols = symbols

    @property
    def min_len(self) -> int:
        return self.__min_len

    @min_len.setter
    def min_len(self, min_len: int) -> None:
        if 0 < min_len <= self.max_len:
            self.__min_len = min_len
            print(f"Using lenght: [{self.min_len} - {self.max_len}]")
        else:
            print(f"Minimum length must be less than maximum length")

    @property
    def max_len(self) -> int:
        return self.__max_len

    @max_len.setter
    def max_len(self, max_len: int) -> None:
        if 1 < max_len >= self.min_len:
            self.__max_len = max_len
            print(f"Using lenght: [{self.min_len} - {self.max_len}]")
        else:
            print(f"maximum length must be great than minimum length")

    @property
    def capital(self) -> bool:
        return self.__capital

    @capital.setter
    def capital(self, capital: bool) -> None:
        self.__capital = capital

    @property
    def numbers(self) -> bool:
        return self.__numbers

    @numbers.setter
    def numbers(self, numbers: bool) -> None:
        self.__numbers = numbers
        print(f"Using numbers: {self.numbers}")

    @property
    def symbols(self) -> bool:
        return self.__symbols

    @symbols.setter
    def symbols(self, symbols: bool) -> None:
        self.__symbols = symbols
        print(f"Using symbols: {self.symbols}")

    def __repr__(self) -> str:
        return f"""
    Range: [{self.min_len} - {self.max_len}]
    Using Capitals: {self.capital}
    Using Numbers: {self.numbers}
    Using Symbols: {self.symbols}
    """

    def generate(self) -> str:
        length = randrange(start=self.min_len, stop=self.max_len + 1, step=1)
        source = ascii_letters if self.capital else ascii_lowercase
        source += (digits if self.numbers else '') + (punctuation if self.symbols else '')
        password = ''
        print(
            f"Generating password with:\n Length: {length}\n Options:{self}")
        
        password = ''.join(choice(source) for i in range(length))

        print(f"Password generated: {password}")

        return password

    def main_menu(self):
        option = ''
        while option != 'q':
            print("""
(1) - Generate password
(2) - View options
(3) - Configuration
(q) - Exit""")
            option = input()
            clear()
            match option:
                case '1':
                    self.generate()
                case '2':
                    print(f"Options: {self}")
                case '3':
                    self.config_menu()
                case 'q':
                    continue
                case _:
                    print(f"Invalid option: {option}")

    def config_menu(self):
        option = ''
        while option != 'q':
            print("""
(0) - View values
(1) - Change minimum length
(2) - Change maximum length
(3) - Use capital letters?
(4) - Use numbers?
(5) - Use symbols?
(q) - Back to main""")
            option = input()
            match option:
                case '0':
                    print(f"Options: {self}")
                case '1':
                    try:
                        value = int(input("Please insert a integer:\n"))
                    except ValueError:
                        print(f"Invalid value. No change")
                        continue
                    self.min_len = value
                case '2':
                    try:
                        value = int(input("Please insert a integer:\n"))
                    except ValueError:
                        print(f"Invalid value. No change")
                        continue
                    self.max_len = value
                case '3':
                    try:
                        value = int(input("Please press 1 for Yes or 0 for No.:\n"))
                    except ValueError:
                        print(f"Invalid value. No change")
                        continue
                    self.capital = bool(value)
                case '4':
                    try:
                        value = int(input("Please press 1 for Yes or 0 for No.:\n"))
                    except ValueError:
                        print(f"Invalid value. No change")
                        continue
                    self.numbers = bool(value)
                case '5':
                    try:
                        value = int(input("Please press 1 for Yes or 0 for No.:\n"))
                    except ValueError:
                        print(f"Invalid value. No change")
                        continue
                    self.symbols = bool(value)
                case 'q':
                    continue
                case _:
                    print(f"Invalid option: {option}")


if __name__ == '__main__':
    my_generator = Generator()
    my_generator.main_menu()
