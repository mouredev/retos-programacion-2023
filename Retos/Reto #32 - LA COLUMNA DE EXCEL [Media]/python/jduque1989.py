# Transform letters to numbers for example A=1 and Z=26

# get AA = 27

def is_valid_column(column):
    """Check if the input is a valid column string."""
    return column.isalpha()


def ask_column():
    column = input("Enter a column: ").upper().strip()
    while not is_valid_column(column):
        column = input("Enter a valid column: ").upper().strip()
    return len(column), column


def letter_to_number(ch):
    return ord(ch) - ord('A') + 1


size, ch = ask_column()


suma = 0
for index, letter in enumerate(ch):
    number = letter_to_number(letter)
    number = number * (26 ** (size - index - 1))
    print(number)
    suma += number
    # print(suma)

print(f"{ch} = {suma}")
