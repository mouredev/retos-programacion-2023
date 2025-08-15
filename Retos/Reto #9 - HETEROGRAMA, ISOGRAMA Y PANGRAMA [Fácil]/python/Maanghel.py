"""
Crea 3 funciones, cada una encargada de detectar si una cadena de
    texto es un heterograma, un isograma o un pangrama.
- Debes buscar la definición de cada uno de estos términos.
"""

from typing import Dict, Set

def is_pangram(text: str) -> bool:
    """
    Check if a given text is a pangram.

    A pangram is a sentence that contains every letter of the alphabet at least once.

    Args:
        text (str): The input text to evaluate.

    Returns:
        bool: True if the text is a pangram, False otherwise.
    """
    _validate(text)
    text = text.lower()
    alphabet: Set[str] = set("abcdefghijklmnopqrstuvwxyz")
    letters: Set[str] = {char for char in text if char.isalpha()}
    return letters >= alphabet

def is_heterogram(text: str) -> bool:
    """
    Check if a given text is a heterogram.

    A heterogram is a word or sentence in which no letter is repeated.

    Args:
        text (str): The input text to evaluate.

    Returns:
        bool: True if the text is a heterogram, False otherwise.
    """
    _validate(text)
    text = text.lower()
    seen_letters: Set[str] = set()
    for char in text:
        if char.isalpha():
            if char in seen_letters:
                return False
            seen_letters.add(char)
    return True

def is_isogram(text: str) -> bool:
    """
    Check if a given text is an isogram.

    An isogram is a word or sentence where each letter occurs the same number of times.

    Args:
        text (str): The input text to evaluate.

    Returns:
        bool: True if the text is an isogram, False otherwise.
    """
    _validate(text)
    text = text.lower()
    letters_count: Dict[str, int] = {}
    for char in text:
        if char.isalpha():
            if char in letters_count:
                letters_count[char] += 1
            else:
                letters_count[char] = 1
    return len(set(letters_count.values())) == 1

def _validate(data: str) -> None:
    """
    Validate the input data to ensure it is a non-empty string.

    Args:
        data (str): The input to validate.

    Raises:
        TypeError: If the input is not a string.
        ValueError: If the string is empty.
    """
    if not isinstance(data, str):
        raise TypeError("Solo se aceptan cadenas de textos.")
    if not data:
        raise ValueError("Las cadenas de textos no pueden estar vacias.")

if __name__ == "__main__":
    test_texts = [
        "Un jugoso zumo de piña y kiwi bien frio es exquisito y no lleva alcohol", # Pangrama
        "Logica", # Isograma
        "Adultero" # Heterograma
        ]

    for text in test_texts:
        print(f"Texto: '{text}'")
        print(f"Es pangrama: {is_pangram(text)}")
        print(f"Es heterograma: {is_heterogram(text)}")
        print(f"Es isograma: {is_isogram(text)}")
        print()
