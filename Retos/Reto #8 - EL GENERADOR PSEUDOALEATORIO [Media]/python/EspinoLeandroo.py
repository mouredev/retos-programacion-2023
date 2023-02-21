import time

semilla = int(time.time() * 1000)

def random():
    global semilla
    semilla = (1103515245 * semilla + 12345) % (2**31)
    return semilla % 101

for i in range(10):
    print(random())