def draw_triforce(size: int) -> None:
    result = []
    draw = "*" * (2*size-1)
    reboot_draw = False
    for i in range(2*size):
        if i >= size:
            if not reboot_draw:
                draw = "*" * (2 * size - 1)
                reboot_draw = True
            result.append(" " * i + draw)
            draw = draw[:-2]
        else:
            result.append(" " * i + draw + " " * (2 * i + 1) + draw)
            draw = draw[:-2]

    for i in result[::-1]:
        print(i)

if __name__ == "__main__":
    draw_triforce(4)