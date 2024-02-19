def t9_interpreter(input_sequence: str) -> str:
    """
    Convert T9 keypresses to their letter representation.

    Args:
        input_sequence (str): T9 keypress sequence.

    Returns:
        str: Letter representation of the keypress sequence.
    """
    t9_mapping = {
        "1": [",", ".", "?", "!"],
        "2": ["A", "B", "C"],
        "3": ["D", "E", "F"],
        "4": ["G", "H", "I"],
        "5": ["J", "K", "L"],
        "6": ["M", "N", "O"],
        "7": ["P", "Q", "R", "S"],
        "8": ["T", "U", "V"],
        "9": ["W", "X", "Y", "Z"],
        "0": [" "],
    }

    def t9_to_letters(t9_number: str) -> str:
        """
        Convert a T9 keypress block to its corresponding letter.

        Args:
            t9_number (str): T9 keypress block.

        Returns:
            str: Corresponding letter.
        """
        length = len(t9_number) - 1
        index = int(t9_number[0])
        letter = t9_mapping[str(index)][length]
        return letter

    words = [t9_to_letters(block) for block in input_sequence.split("-")]
    return "".join(words)

if __name__ == "__main__":
    t9_input = "6-666-88-777-33-3-33-888"
    output = t9_interpreter(t9_input)
    print(output)