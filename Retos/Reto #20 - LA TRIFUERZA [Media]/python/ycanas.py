def draw_top(n):
    for i in range(n):
        print(' ' * (n * 2 - i - 1) + '*' * (2 * i + 1))

def draw_bottom(n):
    for i in range(n):
        print(' ' * (n - i - 1) + '*' * (2 * i + 1) + ' ' * (2 * n - (i * 2) - 1) + '*' * (2 * i + 1))

def draw_triforce(n):
    draw_top(n)
    draw_bottom(n)

draw_triforce(4)
