def dibujar_escalera(escalones: int):
    if escalones == 0:
        print("__")
        return

    if escalones > 0:
        for step in range(escalones, 0, -1):
            space = " " * (2 * step)
            if step == (escalones):
                print(f"{space}_")
            print(f"{space[:-2]}_|")

    else:
        for step in range(abs(escalones)):
            space = " " * (2 * step + 1)
            if step == 0:
                print(f"_")
            print(f"{space}|_")


dibujar_escalera(0)
