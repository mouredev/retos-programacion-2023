def get_column_number(column_name: str) -> int:
    col_number = 0
    for char in column_name:
        col_number = col_number * 26 + (ord(char) - ord("A") + 1)
    return col_number


if __name__ == "__main__":
    print(get_column_number("A"))
    print(get_column_number("Z"))
    print(get_column_number("AA"))
    print(get_column_number("CA"))
    print(get_column_number("AAA"))
