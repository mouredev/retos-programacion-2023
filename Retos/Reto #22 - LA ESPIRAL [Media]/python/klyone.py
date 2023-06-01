#!/usr/bin/env python3

symbols = {
    "h" : "═",
    "v" : "║",
    "d" : "╗",
    "u" : "╔",
    "D" : "╝",
    "U" : "╚",
}

def generate_spiral_from_side(n):
    str = ""
    seq_h = 0
    seq_v = 0
    horizontal = 1
    i = n-1

    while i >= 0:
        if horizontal == 1:
            str += ("h" * i)

            if seq_h == 0:
                str += "d"
                seq_h = 1
            else:
                seq_h = 0
                str += "U"

            horizontal = 0
            i = i - 1
        else:
            str += ("v" * i)

            if seq_v == 0:
                str += "D"
                seq_v = 1
            else:
                str += "u"
                seq_v = 0
            horizontal = 1

    return str

def generate_spiral(n):
    cursor = [0, 0]
    spiral = []
    direction_v = 0
    direction_h = 0

    str = generate_spiral_from_side(n)

    for s in str:
        symb = symbols[s]
        cur = cursor.copy()
        spiral.append([symb, cur])

        if s == "h":
            if direction_h == 0:
                cursor[1] = cursor[1] + 1
            else:
                cursor[1] = cursor[1] - 1
        if s == "D":
            direction_h = 1
            cursor[1] = cursor[1] - 1
        if s == "d":
            direction_v = 0
            cursor[0] = cursor[0] + 1
        if s == "U":
            direction_v = 1
            cursor[0] = cursor[0] - 1
        if s == "u":
            direction_h = 0
            cursor[1] = cursor[1] + 1
        if s == "v":
            if direction_v == 0:
                cursor[0] = cursor[0] + 1
            else:
                cursor[0] = cursor[0] - 1

    return spiral

def draw_spiral(spiral):
    imax = -1
    jmax = -1

    for s in spiral:
        if s[1][0] > imax:
            imax = s[1][0]
        if s[1][1] > jmax:
            jmax = s[1][1]

    spiral_str = []

    for i in range(imax+1):
        spiral_str.append("X" * (jmax+1))

    for s in spiral:
        symb = s[0]
        pos = s[1]

        tmp = list(spiral_str[pos[0]])
        tmp[pos[1]] = symb
        spiral_str[pos[0]] = "".join(tmp)

    for s in spiral_str:
        print(s.replace("X", " "))

if __name__ == "__main__":
    draw_spiral(generate_spiral(1))
    draw_spiral(generate_spiral(2))
    draw_spiral(generate_spiral(3))
    draw_spiral(generate_spiral(4))
    draw_spiral(generate_spiral(5))
    draw_spiral(generate_spiral(10))
    draw_spiral(generate_spiral(30))
