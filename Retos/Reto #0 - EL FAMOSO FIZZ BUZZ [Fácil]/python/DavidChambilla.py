for i in range(1,101):
    if i % 3 == 0 and i % 5 ==0:
        print(i, "fizzbuzz")
    elif i % 3 == 0:
        print(i, "fizz")
    elif i % 5 == 0:
        print(i, "buzz")
    else:
        print(i)