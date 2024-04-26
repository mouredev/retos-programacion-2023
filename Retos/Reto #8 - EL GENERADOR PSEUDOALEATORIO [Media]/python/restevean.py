import time


# Classical method known as the linear congruential generator (LCLG)
def pseudo_random_generator(seed=42):
    if seed is None:
        seed = int(time.time() * 1000) % 2 ** 32
    a = 1664525
    c = 1013904223
    m = 2**32
    xn = seed
    while True:
        xn = (a * xn + c) % m
        yield xn % 101  # Devuelve un número entre 0 y 100


gen = pseudo_random_generator()
for _ in range(10):
    print(next(gen))
