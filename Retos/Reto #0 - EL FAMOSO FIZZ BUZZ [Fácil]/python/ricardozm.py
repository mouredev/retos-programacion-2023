fizz = "fizz"
buzz = "buzz"

for element in range(1,101):
    multipo_3 = element % 3 == 0
    multipo_5 = element % 5 == 0

    if multipo_3:
        print(fizz)
    elif multipo_5:
        print(buzz)
    elif multipo_3 and multipo_5:
        print(fizz,buzz)
    else:
        print(element)