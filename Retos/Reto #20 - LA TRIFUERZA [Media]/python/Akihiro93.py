def trifuerza (n):
    n = (2*n) - 1
    #triangulo de arriba
    e = (n * 2) + 1
    i = 1
    c = (e/2) + 1
    while e > c:
        temp = (" " * (e)) + ("*" * i)
        print(temp)
        i += 2
        e -= 1
    # triángulos de abajo
    i = 1
    while n > 0:
        temp = (" " * n) + ("*" * i)
        espacios = " " * (n-1)
        print(temp, espacios, temp)
        n -= 1
        i += 2

while True:
    try:
        entrada = int(input("El numero base: "))
    except ValueError as e:
        print("ERROR: ", e)
    else:
        break

trifuerza(entrada)