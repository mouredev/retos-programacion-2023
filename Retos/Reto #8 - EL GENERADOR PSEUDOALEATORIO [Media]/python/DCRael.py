def pseudo_random(seed, a, c, m):
    x = seed
    while True:
        x = (a * x + c) % m
        yield x

a = 1664525
c = 1013904223
m = 2**32
seed = 1234

generator = pseudo_random(seed, a, c, m)
for i in range(10):
    num = (next(generator) % 100) + 1
    print(num)
    