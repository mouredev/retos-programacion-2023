for n in range(1, 101):
    if (n % 3 == 0) & (n % 5 == 0):
        print('fizzbuzz')
    if n % 3 == 0:
        print('fizz')
    elif n % 5 == 0:
        print('buzz')
    else:
        print(n)