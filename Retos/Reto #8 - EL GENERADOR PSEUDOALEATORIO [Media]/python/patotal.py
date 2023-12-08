
import time

print (*[time.time_ns() % 101 for i in range(101)])