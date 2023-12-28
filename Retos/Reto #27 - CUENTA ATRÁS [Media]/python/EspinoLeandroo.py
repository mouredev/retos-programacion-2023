import time

start = int(input("¿Desde qué número iniciará la cuenta regresiva? "))
pause = int(input("¿Cuántos segundos serán de pausa entre cada número? "))

while start >= 0:
    print(start)
    start -= 1
    time.sleep(pause)