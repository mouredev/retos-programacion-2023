import time


def main(begin, steps):
    print(begin)
    for i in range(begin - 1, 0, -1):
        time.sleep(steps)
        print(i)


if __name__ == "__main__":
    begin = int(
        input("Ingrese el número desde el cual comenzara la cuenta regresiva: ")
    )
    steps = int(input("Ingrese el numero de segundos a esperar en cada paso: "))
    if begin > 0 and steps >= 0:
        main(begin, steps)
    else:
        print("Entradas invalidas")
