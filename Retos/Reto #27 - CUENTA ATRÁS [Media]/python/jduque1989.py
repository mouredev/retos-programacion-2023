import time

# Funcion para solicitar al usuario los parametros y validación

def data_input():
    while True:
        try:
            count_init = int(input("Enter a number to start countdown: "))
            step = int(input("Enter a step size: "))
            checker(count_init, step)
        except ValueError:
            print("Error, please enter a number")


# Funcion para revisar que cumpla la condición de enteros positivos

def checker(count_init, step):
    if count_init < 0 or step < 0:
        print("Error, please enter a positive number")
        data_input()
    else:
        count_down(count_init, step)
            
# Funcion de la cuenta regresiva

def count_down(count_init, step):
    while count_init >= 0:
        print(count_init)
        time.sleep(step)
        count_init -= 1
        if count_init == 0:
            print("Blast off!")
            break


data_input()
