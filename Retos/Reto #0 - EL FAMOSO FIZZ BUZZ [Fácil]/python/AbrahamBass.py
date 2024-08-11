def fizz_buzz():
    for i in range(1, 101):
        # Si i es múltiplo de 3 y de 5, imprime "fizzbuzz"
        if i % 3 == 0 and i % 5 == 0:
            print("fizzbuzz")
        # Si i es múltiplo de 3, imprime "fizz"
        elif i % 3 == 0:
            print("fizz")
        # Si i es múltiplo de 5, imprime "buzz"
        elif i % 5 == 0:
            print("buzz")
        # Si i no es múltiplo de 3 ni de 5, imprimime el número
        else:
            print(i)

fizz_buzz()