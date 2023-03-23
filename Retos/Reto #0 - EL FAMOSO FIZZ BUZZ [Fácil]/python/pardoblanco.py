for n in range(1, 100):
    if n%3 == 0 and n%5 == 0:
        print("fizzbuzz\n")
    elif n%5 == 0:
        print("buzz\n")
    elif  n%3 == 0:
        print("fizz\n")
    else:
        print("{}\n".format(n))