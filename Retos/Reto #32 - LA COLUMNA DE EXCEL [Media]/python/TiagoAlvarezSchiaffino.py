import string
from functools import reduce

def calculate_column_number(column_name: str) -> int:
    """
    Calculate the column number of an Excel sheet based on its name.

    Args:
        column_name (str): The name of the Excel sheet column.

    Returns:
        int: The column number.
    """
    alphabet = string.ascii_uppercase
    return reduce(lambda acc, char: acc * len(alphabet) + alphabet.index(char) + 1, column_name.upper(), 0)

def main():
    """
    Main function to interactively input and calculate Excel column numbers.
    """
    column_name = input("Enter the column name: ")
    column_number = calculate_column_number(column_name)
    print(f"The column number for {column_name} is: {column_number}")

if __name__ == "__main__":
    main()
