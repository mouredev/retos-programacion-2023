def print_triforce(rows: int):

    for row in range(0, rows * 2):
        if row < rows:
            start_space = " " * (((2 * rows) - 1) - row)
            print_row = "*" * ((2 * (row + 1)) - 1)
            print(f"{start_space}{print_row}")
        else:
            current_row = row - rows
            start_space = " " * ((rows - current_row) - 1)
            middle_space = " " * ((2 * (rows - current_row)) - 1)
            print_row = "*" * ((2 * (current_row + 1)) - 1)
            print(f"{start_space}{print_row}{middle_space}{print_row}")

print_triforce(1)
print_triforce(2)
print_triforce(3)
print_triforce(30)