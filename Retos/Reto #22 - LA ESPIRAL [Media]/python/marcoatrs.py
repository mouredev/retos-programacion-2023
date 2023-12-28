def espiral(n: int):
    # Parte Superior
    guide = 0
    for step in range(1, n + 1, 2):
        p1 = "║" * max(0, guide - 1)
        p2 = "╔" if guide > 0 else ""
        p3 = "═" * (n - step)
        p4 = "╗"
        p5 = "║" * guide
        guide += 1
        print(f"{p1}{p2}{p3}{p4}{p5}")
    # Parte Inferior
    steps = range(2, n + 1, 2)
    guide = 0
    for step in steps:
        p1 = "║" * ((n - step) // 2)
        p2 = "╚" 
        sub = 2 if n % 2 == 0 else 1
        p3 = "═" * (step - sub)
        p4 = "╝"
        p5 = "║" * (len(steps) - 1 - guide)
        guide += 1
        print(f"{p1}{p2}{p3}{p4}{p5}")


espiral(5)
espiral(6)
espiral(45)
