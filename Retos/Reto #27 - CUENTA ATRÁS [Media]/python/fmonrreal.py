import time

def count_down(start,seconds):
    for number in range(start,0,-1):
        print(number)
        time.sleep(seconds)
    print("Fin de la cuenta regresiva")

while True:
    try:
        start = int(input("Ingrese numero en el que comienza la cuenta: "))
    except ValueError:
        print("Error. Solo se puede escribir un número entero positivo")
    else:
        break
while True:
    try:
        seconds = int(input("Ingrese los segundos que tienen que transcurrir entre cada cuenta: "))
    except ValueError:
        print("Error. Solo se puede escribir un número entero positivo")
    else:
        break

count_down(start,seconds)