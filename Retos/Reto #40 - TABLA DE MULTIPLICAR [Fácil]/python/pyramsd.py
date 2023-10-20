def mul_table(n):
    
    while True:
        try:
            n = int(input("Numero: "))
            break
        except ValueError:
            print("Valor no numerico")

    for i in range(1, 11):
        print(f"{n} x {i} = {n*i}")
    
mul_table()
