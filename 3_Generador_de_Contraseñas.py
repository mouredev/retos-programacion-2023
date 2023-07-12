"""
El algoritmo tiene como objetivo crear contraseñas de manera aleatoria con las características que el usuario considere adecuadas para su contraseña.
"""

import string as str
import random

class GeneradorPassword:
    def __init__(self, length: int = 8, capital_letters: bool = True, number: bool = True, symbols: bool = True):
        """
        Inicializa un objeto 'GeneradorPassword' con los parámetros especificados.

        Parámetros:
        - longitud (int): Longitud de la contraseña (por defecto es 8).
        - mayusculas (bool): Indica si se deben incluir letras mayúsculas (por defecto es True).
        - numero (bool): Indica si se deben incluir números (por defecto es True).
        - simbolo (bool): Indica si se deben incluir caracteres especiales (por defecto es True).
        """
        self.length = length
        self.capital_letters = capital_letters
        self.number = number
        self.symbols = symbols

    def generate_password(self) -> str:
        """
        Genera una contraseña aleatoria utilizando los parámetros especificados al inicializar el objeto.

        Retorna:
        - str: La contraseña generada.

        Si la longitud es menor a 8 o mayor a 300, se retorna un mensaje de error.
        """
        characters = list(str.ascii_lowercase)

        if self.capital_letters:
            characters.extend(str.ascii_uppercase)

        if self.number:
            characters.extend(str.digits)

        if self.symbols:
            characters.extend(str.punctuation)

        if 8 <= self.length <= 300:
            password = "".join(random.sample(characters, self.length))
            return password
        else:
            return "La longitud mínima debe ser de '8' caracteres y la máxima de '300'."

if __name__ == "__main__":
    generador = GeneradorPassword(length=58, capital_letters=True, number=True, symbols=True)
    print(generador.generate_password())