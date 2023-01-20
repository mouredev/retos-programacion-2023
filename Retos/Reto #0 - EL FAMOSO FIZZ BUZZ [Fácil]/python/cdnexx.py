for i in range(100):
    n = i + 1
    if n % 3 == 0 and n % 5 == 0:
        print(f'({n}) fizzbuzz\n')
    elif n % 3 == 0:
        print(f'({n}) fizz\n')
    elif n % 5 == 0:
        print(f'({n}) buzz\n')
    else:
        print(f'({n})\n')
