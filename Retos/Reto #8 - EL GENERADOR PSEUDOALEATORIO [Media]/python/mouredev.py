import time


def random():
    return time.time_ns() % 101


for _ in range(0, 101):
    print(random())
