#!/usr/bin/env python3

def generate_triangle(n):
    if n < 2:
        return ["*"]
    else:
        size = 2 * n - 1
        middle = int(size / 2)
        line = ("X" * size)

        triangle = []
        for i in range(n):
            middle_start = middle - i
            middle_end = middle + i

            pre = line[:middle_start]
            inter = ("*" * (2*(i+1)-1))
            pos = line[middle_end+1:]

            triangle.append((pre + inter + pos).replace("X", " "))

        return triangle

def export_triangle(triangle, double=False, sep=0):
    final_triangle = ""
    i = 1
    for t in triangle:
        final_triangle += " " * sep
        final_triangle += t
        if double:
            final_triangle += " "
            final_triangle += t
        if i != len(triangle):
            final_triangle += "\n"
        i += 1
    return final_triangle

def generate_triforce(n):
    triforce = ""
    triforce += export_triangle(generate_triangle(n), sep=n) + "\n"
    triforce += export_triangle(generate_triangle(n), double=True)
    return triforce

if __name__ == "__main__":
    print(generate_triforce(2))
    print(generate_triforce(3))
    print(generate_triforce(5))
    print(generate_triforce(7))
    print(generate_triforce(10))
