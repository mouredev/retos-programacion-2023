#!/usr/bin/env python3

def generate_spaces(step):
    if step == 0:
        return ""
    elif step > 0:
        return " " * (2*step)
    else:
        return " " * (2*(-step)-1)

def create_stairs(steps):
    stairs = ""
    if steps == 0:
        stairs += "__"
    else:
        rising = True
        first_step = True
        initial = steps
        final = -1
        if steps < 0:
            rising = False
            initial = 0
            final = steps - 1

        for i in range(initial, final, -1):
            stairs += generate_spaces(i)

            if rising:
                stairs += "_"

            if not first_step:
                stairs += "|"

            if not rising:
                stairs += "_"

            stairs += "\n"

            if first_step:
                first_step = False

    return stairs

if __name__ == "__main__":
    print(create_stairs(0))
    print(create_stairs(1))
    print(create_stairs(2))
    print(create_stairs(50))
    print(create_stairs(100))
    print(create_stairs(-1))
    print(create_stairs(-2))
    print(create_stairs(-50))
    print(create_stairs(-100))
