def draw_steps(steps: int):

    if steps > 0:
        for step in range(steps + 1):
            spaces = "  " * (steps - step)
            step_draw = "_" if step == 0 else "_|"
            print(f"{spaces}{step_draw}")
    elif steps < 0:
        for step in range(abs(steps) + 1):
            spaces = " " * ((step * 2) - 1)
            step_draw = "_" if step == 0 else "|_"
            print(f"{spaces}{step_draw}")
    else:
        print("__")

draw_steps(0)
draw_steps(4)
draw_steps(20)
draw_steps(-4)
draw_steps(-20)