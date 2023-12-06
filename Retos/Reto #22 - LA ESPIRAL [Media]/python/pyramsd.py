import math

def espiral(size):
    first_line = math.ceil(size / 2)

    for i in range(first_line):
        if i == 0:
            print(("=" * (size-1)) + "╗")
        else:
            print(("║" * (i-1) + "╔" + "=" * (size - (2*i) - 1)) + "╗" + "║" * i)

    for i in range(first_line, size):
        print("║" * (size-i-1) + "╚" + "=" * ((2*i) - size) + "╝" + "║" * (size-i-1))

espiral(5)
