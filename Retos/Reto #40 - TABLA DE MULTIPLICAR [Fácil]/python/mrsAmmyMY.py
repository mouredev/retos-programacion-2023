while True:

    num = int(input("Ingrese un número\n$ "))

    for prod in range(1, 11):
        result = num * prod
        print(f"{num} x {prod} = {result}")
