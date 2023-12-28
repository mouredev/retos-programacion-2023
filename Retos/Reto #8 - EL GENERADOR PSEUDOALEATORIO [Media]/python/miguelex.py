import time

seed = int(time.time() * 1000)


def RandonNumber(a, m):
    global seed
    q = m / a
    r = m % a

    seed = a * (seed % q) - r * (seed / q)

    if seed <= 0:
        seed += m

    return int(seed)


count = int(input("Cuantos numeros quieres generar?: "))
a = int(time.time() * 1000)
m = int(time.time() * 10000)

for i in range(1, count + 1):
    print(f'Número aleatorio {i} es: {1 + RandonNumber(a, m) % 100}')
    time.sleep(3)
