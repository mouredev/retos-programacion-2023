import time
numbers = list(range(1,101))
number = time.time_ns() % len(numbers)
print(number)