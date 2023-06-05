import time

def random(n:int):
    a = time.time()
    rnd = a-int(a)
    time.sleep(0.51)
    return int(rnd * n)+1

for i in range(0,10):
    print(random(100))