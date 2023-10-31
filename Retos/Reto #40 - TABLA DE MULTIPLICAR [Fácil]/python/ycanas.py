def tabla(n):
    max = len(str(n * 10))
    for i in range(1, 11):
        print(f"{n} x {str(i):>2s} = {str(n * i):>{max}s}")


while True:
    try:
        n = int(input("Ingrese un número entero: "))
        tabla(n)
        break

    except:
       print("[Error] Ingrese un número entero.")
