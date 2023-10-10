import time


def random() -> int:
    return (time.time_ns()) % 101
    

print(random())
