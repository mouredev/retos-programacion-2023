# Mi solución del ejercicio1

for i in range(1, 101, 1):
    if i %3 == 0 and i %5 == 0:
        print("fizzbuzz\n")

    elif i %3 == 0:
        print("fizz\n")
    elif i %5 == 0:
        print("buzz\n")
    else:
        print(f"{i}\n")