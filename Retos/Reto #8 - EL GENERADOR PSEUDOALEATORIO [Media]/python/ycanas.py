import time

def pseudorandom():
    seed = time.time_ns() % 100
    return ((13 * seed) + 73) % 101

number = pseudorandom()
print(number)
