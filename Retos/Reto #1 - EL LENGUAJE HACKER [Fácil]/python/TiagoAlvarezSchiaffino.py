def leet_language(text):
    """
    Translate text into leet language.

    Args:
    text (str): Input text to be translated.

    Returns:
    str: Translated text in leet language.
    """

    leet = {"A": "4", "B": "I3", "C": "[", "D": ")", "E": "3", "F": "|=", "G": "&", "H": "#", "I": "1",
            "J": ",_|", "K": ">|", "L": "1", "M": "/\/\\", "N": " ^/", "O": "0", "P": " |*", "Q": "(_,)",
            "R": "I2", "S": "5", "T": "7", "U": "(_)", "V": "\/", "W": "\/\/", "X": "><", "Y": "j", "Z": "2",
            "1": "L", "2": "R", "3": "E", "4": "A", "5": "S", "6": "b", "7": "T", "8": "B", "9": "g", "0": "o"}

    leet_text = ""

    for char in text:
        if char.upper() in leet:
            leet_text += leet[char.upper()]
        else:
            leet_text += char

    return leet_text

text_to_translate = input("Enter the text to translate: ")

translated_text = leet_language(text_to_translate)

print(f"The text: {text_to_translate}\n Translates to: {translated_text}")