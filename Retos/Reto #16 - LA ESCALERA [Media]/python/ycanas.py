def draw_staircase(steps: int):
    if steps > 0:
        for i in range(steps + 1):
            draw = "_" if i == 0 else "_|"
            length = ((steps * 2) + 2)
            change = i * 2

            for j in range(length - change):
                print(draw) if j == ((steps * 2) + 1) - 2 * i else print(' ', end='')
    
    elif steps < 0:
        for i in range(abs(steps) + 1):
            draw = " _" if i == 0 else "|_"
            length = (2 * i) + 1

            for j in range(length):
                print(draw) if j == 2 * i else print(' ', end='')

    else:
        print("__")

print("\nAscendente: ")
draw_staircase(4)

print("\nDescendente: ")
draw_staircase(-4)

print("\n0: ")
draw_staircase(0)
