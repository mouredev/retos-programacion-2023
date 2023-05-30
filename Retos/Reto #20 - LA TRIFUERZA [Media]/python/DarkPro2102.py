"""
rows = 2
largest_row = 2(rows) - 1 = 2(2) - 1 = 3

   *
  ***
 *   *
*** ***


if rows = 3
largest_row = 5

     *
    ***
   *****
  *     *
 ***   ***
***** *****
"""

def print_triforce(rows: int):
    
    for row in range(rows * 2):
        if row < rows:
            tri = "*" * (2 * (row + 1) - 1)
            space = " " * ((2 * rows - 1) - row)
            print(f"{space}{tri}")
        else:
            new_row = row - rows
            tri = "*" * (2 * (new_row + 1) - 1)
            mid_space = " " * (2 * (rows - new_row) - 1)
            space = " " * ((2 * rows - 1) - row)
            print(f"{space}{tri}{mid_space}{tri}")

if __name__ == '__main__':

    print_triforce(10)