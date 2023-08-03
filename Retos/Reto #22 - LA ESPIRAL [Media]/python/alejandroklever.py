def spiral_matrix(n: int, is_first: bool = True) -> list[list[str]]:
    if n <= 0:
        return []

    if n == 1:
        return [["╗"]]

    if n == 2:
        return [
            ["═", "╗"],
            ["╚", "╝"]
        ]

    matrix = [[" " for _ in range(n)] for _ in range(n)]

    # draw top
    for i in range(n - 1):
        matrix[0][i] = "═"
    matrix[0][-1] = "╗"

    # draw right
    for i in range(1, n - 1):
        matrix[i][-1] = "║"
    matrix[-1][-1] = "╝"

    # draw bottom
    for i in range(n - 1):
        matrix[-1][i] = "═"
    matrix[-1][0] = "╚"
    
    # draw left
    for i in range(2, n - 1):
        matrix[i][0] = "║"
    matrix[1][0] = "╔"

    submatrix = spiral_matrix(n - 2, is_first=False)

    # copy the submatrix into the matrix
    for i in range(n-2):
        for j in range(n-2):
            matrix[i + 1][j + 1] = submatrix[i][j]

    return matrix

def spiral_matrix_to_str(matrix: list[list[str]]) -> str:
    return "\n".join(["".join(row) for row in matrix])

if __name__ == "__main__":
    while True:
        try:
            n = int(input("Introduce el tamaño de la espiral: "))
            break
        except ValueError:
            print("No has introducido un número")

    s = spiral_matrix(n)
    print(spiral_matrix_to_str(s))
