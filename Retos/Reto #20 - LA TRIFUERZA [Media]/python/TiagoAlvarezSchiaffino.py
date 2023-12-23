def draw_tri(n: int):
    """
    Draw the top part of the Triforce.

    Args:
        n (int): The number of rows in the triangles.

    Example:
        For n=2:
            *
           ***
    """
    size = 2 * n - 1
    sep = " " * n
    for i in range(n - 1):
        string = " " * (n - 1 - i)
        string += "*"
        if i != 0:
            string = f"{string}{" " * (2 * i - 1)}*"
        print(f"{sep}{string}")
    final = f"{sep}{"*" * size}"
    print(final)

def draw_2_tri(n: int):
    """
    Draw the bottom two parts of the Triforce.

    Args:
        n (int): The number of rows in the triangles.

    Example:
        For n=2:
          * *
         *   *
        *******
    """
    size = 2 * n - 1
    for i in range(n - 1):
        string = f"{" " * (n - 1 - i)}*"
        if i != 0:
            string = f"{string}{" " * (2 * i - 1)}*"
        sep = " " * (size + 1 - len(string))
        print(f"{string}{sep}{string}")
    final = "*" * size
    print(f"{final}{final}")

def triforce(n: int):
    """
    Draw the complete Triforce.

    Args:
        n (int): The number of rows in the triangles.

    Example:
        For n=3:
            *
           ***
          *   *
         * * * *
    """
    draw_tri(n)
    draw_2_tri(n)

# Example
triforce(3)
