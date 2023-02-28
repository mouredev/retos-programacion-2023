import time
import psutil

def pseudo_random():
    result = 0
    sent = psutil.net_io_counters().bytes_sent
    recv = psutil.net_io_counters().bytes_recv
    timer = int(time.time() * 1000)
    result = (sent * recv)/ timer * 100
    while result >= 100:
        result = result - 100
    return int(result)


print(pseudo_random())