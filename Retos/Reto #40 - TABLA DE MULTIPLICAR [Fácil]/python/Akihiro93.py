while True:
    try:
        number = int(input("Introduce un numero: "))
    except:
        print("Error")
    else:
        break

for i in range(1, 11):
    print(f"{number} x {i} = {number * i}")
