"""
Escribe un programa que reciba un texto y transforme lenguaje natural a
    "lenguaje hacker" (conocido realmente como "leet" o "1337"). Este lenguaje
    se caracteriza por sustituir caracteres alfanuméricos.
- Utiliza esta tabla (https://www.gamehouse.com/blog/leet-speak-cheat-sheet)
    con el alfabeto y los números en "leet".
    (Usa la primera opción de cada transformación. Por ejemplo "4" para la "a")
"""

class LeetTranslator:
    """
    A class used to translate natural language text into leet speak (1337).

    It uses a predefined dictionary to substitute alphanumeric characters
    with their leet equivalents, following a standard leet-speak convention.
    """
    def __init__(self):
        self.leet_alphabet = {
            "a": "4", "b": "l3", "c": "[", "d": ")",
            "e": "3", "f": "|=", "g": "&", "h": "#",
            "i": "1", "j": ",_|", "k": ">|", "l": "£",
            "m": "/\\/\\", "n": "^/", "o": "0", "p": "|*",
            "q": "(_,)", "r": "I2", "s": "5", "t": "7",
            "u": "(_)", "v": "\\/", "w" : "\\/\\/", "x": "><",
            "y": "j", "z": "2", "1": "L", "2": "R", "3": "E",
            "4": "A", "5": "S", "6": "b", "7": "T", "8": "B",
            "9": "g", "0": "o"
        }

    def translate_to_leet(self, text: str) -> str:
        """
        Transforms a given alphanumeric string into leet speak (1337),
        replacing letters and digits with their hacker equivalents.

        Only the first substitution option is used for each character.

        Args:
            text (str): Input text to translate.

        Returns:
            str: Translated text in leet speak.
        """
        self._validate_data(text)
        new_text = [self.leet_alphabet.get(char, char) for char in text.lower()]
        return "".join(new_text).strip()

    def _validate_data(self, text: str) -> None:
        """
        Validates the input text to ensure it is a non-empty alphanumeric string.

        Spaces are allowed, but the text must consist only of letters, numbers,
        and whitespace.

        Args:
            text (str): The input text to validate.

        Raises:
            TypeError: If the input is not a string.
            ValueError: If the string is empty or contains non-alphanumeric characters.
        """
        if not isinstance(text, str):
            raise TypeError("El valor ingresado debe ser un string.")
        if not text:
            raise ValueError("La cadena no puede estar vacia.")
        if not text.replace(" ", "").isalnum():
            raise ValueError("El texto solo puede contener valores alfa numericos.")


if __name__ == "__main__":
    leet_translator = LeetTranslator()
    try:
        text_in_leet = leet_translator.translate_to_leet("Hola Mundo")
        print("Texto Original: 'Hola Mundo'")
        print(f"Texto Traducido: '{text_in_leet}'")
    except (ValueError, TypeError) as e:
        print(f"Error: {e}")
