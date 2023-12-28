import random


def ficticio(temperatura:int, prob_lluvia:int, dias:int):
    dias_lluvia = 0
    temperatura_min = temperatura
    temperatura_max = temperatura

    for dia in range(1, dias + 1):

        print(f"Día {dia}: {temperatura} grados y {prob_lluvia}% de probabilidad de lluvia")

        if temperatura < temperatura_min:
            temperatura_min = temperatura
        elif temperatura > temperatura_max:
            temperatura_max = temperatura

        if prob_lluvia == 100:
            dias_lluvia += 1
            temperatura -= 1
        else:
            if random.randint(1, 10) == 1:
                temperatura += 2 if random.randint(1, 2) == 1 else -2

        
        if temperatura > 25:

            prob_lluvia += 20
            if prob_lluvia > 100:
                prob_lluvia = 100

        elif temperatura < 5:

            prob_lluvia -= 20
            if prob_lluvia < 0:
                prob_lluvia = 0

    print(f"Días lluviosos: {dias_lluvia}")
    print(f"Temperatura mínima: {temperatura_min}")
    print(f"Temperatura máxima: {temperatura_max}")

ficticio(24, 100, 365)
        