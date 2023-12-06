import time


def count (start:  int, delay: int):
    while start > 0:
        print(start)
        time.sleep(delay)
        start -= 1

while True:
    try:
        number = int(input("En numero de empiezo: "))
        delay = int(input("Tiempo de retraso: "))
    except ValueError as e:
        print(f"Error: {e}")
    else:
        break

count(number, delay)


