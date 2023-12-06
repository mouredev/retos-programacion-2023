import time

def countdown_from(num: int, secs: int):
    
    if not isinstance(num, int) or not isinstance(secs, int):
        raise ValueError("We need only integers!")
    
    if num <= 0 or secs <= 0:
        raise ValueError("We need only positive integers greater than zero!")
    
    for n in range(num, -1, -1):
        if n >0:
            print(n)
            time.sleep(secs)
        else:
            print(n)
            break
                                              
if __name__ == "__main__":

    num = -1
    secs = 2
    countdown_from(num, secs)
