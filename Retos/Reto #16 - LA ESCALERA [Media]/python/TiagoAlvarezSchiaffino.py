def draw_stairs(steps: int):
    """
    Draw a staircase based on the number of steps.
    
    Args:
        steps (int): The number of steps. If positive, the stairs ascend from left to right.
                     If negative, the stairs descend from left to right.
                     If zero, two underscores are drawn.

    Returns:
        None
    """
    if steps == 0:
        print("__")
        return

    if steps > 0:
        for step in range(1, steps + 1):
            spaces = "  " * (steps - step)
            tread = "_" if step == 1 else "_|"
            print(f"{spaces}{tread}")
    else:
        for step in range(abs(steps)):
            spaces = " " * (2 * step - 1)
            tread = "_" if step == 0 else "|_"
            print(f"{spaces}{tread}")

if __name__ == "__main__":
    draw_stairs(0)
    draw_stairs(5)
    draw_stairs(-5)
