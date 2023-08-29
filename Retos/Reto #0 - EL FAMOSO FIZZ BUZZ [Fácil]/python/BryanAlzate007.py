def lista_reto():
    for i in range(1, 101):
        if i %3 == 0 and i %5 == 0:
            print("FizzBuzz")
        elif i %3 == 0:
            print("fizz")
        elif i % 5 == 0:
            print("buzz") 
    else:
        print(i)

lista_reto()