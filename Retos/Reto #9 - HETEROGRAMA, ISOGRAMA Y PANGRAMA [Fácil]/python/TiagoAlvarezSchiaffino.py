import re
from unidecode import unidecode

def char_counter(text: str) -> dict[str, int]:
    """
    Count the occurrences of each character in the text.

    Args:
        text (str): The input text.

    Returns:
        dict[str, int]: A dictionary containing character frequencies.
    """
    no_number_text = re.sub(r"\d+", "", text.lower().replace(" ", ""))
    no_punct_text = re.sub(r"[^\w\s]", "", no_number_text)
    unicode_text = unidecode(no_punct_text.replace("ñ", ".")).replace(".", "ñ")

    char_counter_dict = dict()

    for char in unicode_text:
        if char in char_counter_dict:
            char_counter_dict[char] += 1
        else:
            char_counter_dict[char] = 1

    return char_counter_dict

def is_heterogram(text: str) -> bool:
    """
    Check if the text is a heterogram.

    Args:
        text (str): The input text.

    Returns:
        bool: True if it is a heterogram, False otherwise.
    """
    for counter in char_counter(text).values():
        if counter > 1:
            return False
    return True

def is_isogram(text: str) -> bool:
    """
    Check if the text is an isogram.

    Args:
        text (str): The input text.

    Returns:
        bool: True if it is an isogram, False otherwise.
    """
    order = 0
    for counter in char_counter(text).values():
        if order is 0:
            order = counter
        if order is not counter:
            return False
    return True

def is_pangram(text: str) -> bool:
    """
    Check if the text is a pangram.

    Args:
        text (str): The input text.

    Returns:
        bool: True if it is a pangram, False otherwise.
    """
    return len(char_counter(text).keys()) == 27

# Examples
print(is_heterogram("Love"))
print(is_isogram("Anna"))
print(is_pangram("The quirky brown fox jumps over a lazy dog, añd enjoys pizza with pizazz!"))
