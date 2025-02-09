import time

def count_down(count: int, seconds: int):
    if (count < 1 or seconds < 1):
        print("El numero debe ser un entero positivo.")
    else:
        while (count > 0):
            print(count)
            count -= 1
            time.sleep(seconds)

count_down(5, 1)
print("Pum!!!")
