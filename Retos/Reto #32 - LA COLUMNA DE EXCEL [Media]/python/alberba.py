import string

def get_columns_number_xlsx(column_letters: str) -> int:
    column_number = 0
    alphabet_list = list(string.ascii_uppercase)

    for letter in column_letters:
        column_number = (column_number * len(alphabet_list)) + (alphabet_list.index(letter) + 1)

    return column_number

print(get_columns_number_xlsx("AA"))
print(get_columns_number_xlsx("ZZZZ"))