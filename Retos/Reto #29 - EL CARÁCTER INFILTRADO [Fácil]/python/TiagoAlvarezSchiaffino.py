def infiltrated_characters(first_text: str, second_text: str) -> list:
    """
    Find infiltrated characters in two almost identical strings.

    Args:
        first_text (str): The first string.
        second_text (str): The second string.

    Returns:
        list: A list of infiltrated characters.
    """
    infiltrated_chars = []

    if len(first_text) == len(second_text):
        infiltrated_chars = [first_text[index] for index in range(len(second_text)) if second_text[index] != first_text[index]]

    return infiltrated_chars

if __name__ == "__main__":
    example1 = "Me llamo mouredev"
    example2 = "Me llemo mouredov"
    example3 = "Me llamo.Brais Moure"
    example4 = "Me llamo brais moure"

    print(infiltrated_characters(example1, example2))
    print(infiltrated_characters(example3, example4))