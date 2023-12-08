"""This script shows the solution to exercise "Reto #0: EL FAMOSO FIZZ BUZZ" from Brais Moure's official website."""


def main() -> None:
    """
    Main function of the program. This function requests a text in natural language and translates it into basic language 'Leet'.
    """
    natural_text = input("\nMessage: ")
    leet_text = leet_translator(natural_text)
    print("Traduction:", leet_text)


def leet_translator(natural_text: str) -> str:
    """This function translate a natural language text into 'Basic Leet' language text.

    Args:
        natural_text (str): natural language text entered by the user

    Returns:
        str: translation of the text in "Basic Leet"
    """
    replace_characters = {
        "A": "4",
        "B": "8",
        "C": "<",
        "E": "3",
        "G": "9",
        "H": "#",
        "I": "1",
        "O": "0",
        "S": "5",
        "T": "7",
    }

    leet_text = "".join(
        replace_characters[c.upper()] if c.upper() in replace_characters else c
        for c in natural_text
    )

    return leet_text


if __name__ == "__main__":
    main()
