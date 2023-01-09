x = range(1, 101)

def fizzbuzz():
    xprint = ''

    for number in x:
        if (number % 3 == 0) and (number % 5 == 0):
            xprint = xprint + 'fizzbuzz' + '\n'
        elif number % 3 == 0:
            xprint = xprint + 'fizz' + '\n'
        elif number % 5 == 0:
            xprint = xprint + 'buzz' + '\n'
        else:
            xprint = xprint + str(number) + '\n'
    print(xprint)

fizzbuzz()