for n in range(1, 101):
    if n % 15 == 0: print(n, ' fizzbuzz')
    elif n % 3 == 0: print(n, ' fizz')
    elif n % 5 == 0: print(n, ' buzz')
    else: print(n)
    print('\n')
