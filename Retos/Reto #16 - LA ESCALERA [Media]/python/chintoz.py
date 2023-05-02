def descendant(n_steps):
    spaces = ""
    print(spaces + "_")
    spaces = spaces + " "
    for i in range(n_steps):
        print(spaces + "|_")
        spaces = spaces + "  "


def ascendant(n_steps):
    spaces = ""
    for i in range(n_steps):
        spaces = spaces + "  "

    print(spaces + "_")
    for i in range(n_steps):
        spaces = spaces[:len(spaces) - 2]
        print(spaces + "_|")


if __name__ == '__main__':
    steps = int(input("Introduce el número de escalones que quieres pintar: "))
    if steps == 0:
        print("__")
        exit(0)
    if steps > 0:
        ascendant(steps)
    else:
        descendant(steps * -1)
