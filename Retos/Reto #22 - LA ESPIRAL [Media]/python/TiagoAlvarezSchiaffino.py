def draw_spiral(size):
    """
    Draw a spiral with dynamic side size using specified symbols.

    Args:
        size (int): The size of the side for the spiral.

    Symbols Used:
        ═ - Horizontal line
        ║ - Vertical line
        ╗ - Top right corner
        ╔ - Top left corner
        ╝ - Bottom right corner
        ╚ - Bottom left corner

    Example:
        draw_spiral(5)
        Output:
        ════╗
        ╔══╗║
        ║╔╗║║
        ║╚═╝║
        ╚═══╝
    """

    for row in range(0, size):
        spiral = ""
        horizontal = row == 0
        for col in range(0, size):
            if row + col == size - 1:
                spiral += "╗" if col >= row else "╚"
                horizontal = col < row
            elif row - col == 1 and row < (size / 2):
                spiral += "╔"
                horizontal = True
            elif row == col and row >= (size / 2):
                spiral += "╝"
                horizontal = False
            else:
                spiral += "═" if horizontal else "║"

        print(spiral)

# Test cases
draw_spiral(0)
draw_spiral(1)
draw_spiral(2)
draw_spiral(3)
draw_spiral(5)
draw_spiral(20)
draw_spiral(50)
