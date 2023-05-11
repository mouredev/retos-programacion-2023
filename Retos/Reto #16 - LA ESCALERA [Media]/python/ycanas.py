def draw_staircase(steps: int):
    if steps > 0:
        for i in range(steps + 1):
            draw = "_" if i == 0 else "_|"
            spaces = (steps * 2) - (2 * i)
            print(" " * spaces + draw)
    
    elif steps < 0:
        for i in range(abs(steps) + 1):
            draw = " _" if i == 0 else "|_"
            spaces = (2 * i)
            print(" " * spaces + draw)

    else:
        print("__")

print("\nAscendente: ")
draw_staircase(4)

print("\nDescendente: ")
draw_staircase(-4)

print("\n0: ")
draw_staircase(0)
