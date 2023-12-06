from time import sleep


def cuenta_atras(start: int, step: int):
    if (not isinstance(start, int)) or (not isinstance(step, int)):
        print("Los números deben ser de tipo entero")
        return
    if start < 0 or step < 0:
        print("Solo se aceptan números positivos")
        return
    for num in range(start, 0, -1):
        print(num)
        sleep(step)
    print(0)


cuenta_atras(6, 1)
