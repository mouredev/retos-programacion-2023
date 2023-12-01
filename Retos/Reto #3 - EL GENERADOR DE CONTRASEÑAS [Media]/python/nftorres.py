"""This script shows the solution to the exercise "Reto #3: EL GENERADOR DE CONTRASEÑAS" from Brais Moure's official website."""
from random import choice
import string


class PasswordGenerator:
    """This class represents a password generator that generates a password based on user-specified conditions such as length, inclusion of uppercase letters, digits or symbols."""

    def __init__(self) -> None:
        """This methos initializes the default password conditions."""
        self.length: int = 12
        self.uppercase: bool = False
        self.digits: bool = False
        self.symbols: bool = False

    def ask_conditions(self) -> None:
        """This method asks the user how they want their password. For example, if you want it to contain capital letters, digits, or symbols."""
        condition1: int = int(input("1. Length: "))
        self.length = condition1 if 4 < condition1 <= 40 else 12

        condition2: str = input("2. Uppercase Letters (y/n): ")
        self.uppercase = condition2.lower() == "y"

        condition3: str = input("3. Digits (y/n): ")
        self.digits = condition3.lower() == "y"

        condition4: str = input("4. Symbols (y/n): ")
        self.symbols = condition4.lower() == "y"

    def generate_password(self) -> str:
        """This method generates a password based on user-specified conditions.

        Returns:
            str: The generated password.
        """
        characters: str = string.ascii_lowercase
        if self.uppercase:
            characters += string.ascii_uppercase
        if self.digits:
            characters += string.digits
        if self.symbols:
            characters += string.punctuation

        generated_password: str = "".join(
            choice(characters) for _ in range(self.length)
        )

        return generated_password


if __name__ == "__main__":
    generator = PasswordGenerator()
    print("\nPassword Generator by nftorres")
    print("\nhow do you want your password?")
    generator.ask_conditions()
    password = generator.generate_password()
    print("\nYour Password:", password)
