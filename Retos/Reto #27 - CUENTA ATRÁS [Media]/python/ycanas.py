import time

def count_down(init: int, seconds: int):
    if (type(init) == int and init > 0) and (type(seconds) == int and seconds > 0):
        for count in range(init):
            print(f"T-{init - count} Segundos")
            time.sleep(seconds)
        
        print("\nDespegue !!! 🚀")

    else:
        print("Error, los números deben ser enteros mayores que 0.")

count_down(7, 1)
