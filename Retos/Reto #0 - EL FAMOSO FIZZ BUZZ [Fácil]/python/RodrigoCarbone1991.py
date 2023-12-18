for i in range(1, 101):
    if i % 3 == 0 and i % 5 == 0:
        print("\n""fizzbuzz")
    elif  i % 3 == 0:
        print("\n""fizz")
    elif i % 5 == 0:
        print("\n""buzz")
    else:
        print("\n", i)