import time
import threading

def countdown(start: int, seconds: int):

    if type(start) == int and type(seconds) == int and start > 0 and seconds > 0:
        for number in range(start, -1, -1):
            print(number)
            time.sleep(seconds)
    else:
        raise Exception("Los parámetros tienen que ser enteros positivos")

# Asíncrono
threading.Thread(target=countdown, args=(10, 1)).start()

# Síncrono
# countdown(10, 1)

print("Boom!!! 💥")