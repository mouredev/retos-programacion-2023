
def bothMultiple(number):
    return (number % 5 == 0) and (number % 3 == 0)

def multipleOf3(number):
    return number % 3 == 0

def multipleOf5(number):
    return number % 5 == 0

def run():

    mult3 = "fizz"
    mult5 = "buzz"
    for i in range(1, 101):
        if bothMultiple(i):
            print(mult3 + mult5)

        elif multipleOf3(i):
            print(mult3)

        elif multipleOf5(i):
            print(mult5)

        else:
            print(i)


if __name__ == '__main__':
    run()


