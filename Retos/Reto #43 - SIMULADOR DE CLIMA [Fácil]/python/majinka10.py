import random


def clima(dias: int, temperatura: int, rain_prob: float):
    print(f"Condiciones climáticas durante {dias} días")
    dias_llovio = []
    temp_min = 999
    temp_max = 0

    for _ in range(1, dias+1):
        if random.random() <= 0.1:
            if random.random() <= 0.5:
                temperatura += 2
                print(f"La temperatura aumentará 2° a {temperatura}°")
            else:
                temperatura -= 2
                print(f"La temperatura disminuirá 2° a {temperatura}°")
        if temperatura < temp_min:
            temp_min = temperatura
        elif temperatura > temp_max:
            temp_max = temperatura

        if random.random() <= rain_prob:
            print(f"El día {_} lloverá y tendrá una temperatura de {temperatura}°")
            temperatura -= 1
            dias_llovio.append((_, temperatura))
        else:
            print(f"El día {_} no lloverá y tendrá una temperatura de {temperatura}°")

        if temperatura > 25:
            rain_prob += 0.2
        elif temperatura < 5:
            rain_prob -= 0.2
        
    return f"La temperatura mínima en el periodo será de {temp_min}° y la máxima de {temp_max}°. Además lloverá por {len(dias_llovio)} días"

print(clima(random.choice(range(1, 31)), 10, 0.2))