from time import sleep


def countdown(init:int, delay=1):
    if init < 0:
        print('El numero tiene que ser positivo')

    for number in range(init, -1, -1):
        sleep(delay)
        print(number)


if __name__ == "__main__":
    countdown(-1)
    countdown(3)
    countdown(3,2)
    
