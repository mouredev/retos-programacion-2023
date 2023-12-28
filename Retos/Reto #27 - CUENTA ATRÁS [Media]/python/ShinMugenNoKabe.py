import time


def countdown(start: int, seconds: int):
    if start < 0 or seconds < 0:
        raise ValueError("Introduce un número válido")
    
    for i in range(start, -1, -1):
        print(i)
        
        if i != 0:
            time.sleep(seconds)
        
        
if __name__ == "__main__":
    countdown(10, 1)
    print("----------")
    countdown(7, 3)
    print("----------")
    countdown(20, 0)