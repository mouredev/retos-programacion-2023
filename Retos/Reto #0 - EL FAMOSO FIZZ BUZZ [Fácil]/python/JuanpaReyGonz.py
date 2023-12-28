def run():
    for numeros in range(1, 101):
        if numeros % 3 == 0 and numeros % 5 == 0:
            print("fizzbuzz")
        elif numeros % 3 == 0:
            print("fizz")
        elif numeros % 5 == 0:
            print("buzz")
        else:
            print(numeros)


if __name__ == '__main__':
    run()
