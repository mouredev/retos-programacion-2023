for n in range(1,101):
    if n % 3 == 0:
        if n % 5 == 0:
            print('fizzbuzz\n')
        else:
            print('fizz\n')
    elif n % 5 == 0:
        print('buzz\n')
    else:
        print(f'{n}\n')