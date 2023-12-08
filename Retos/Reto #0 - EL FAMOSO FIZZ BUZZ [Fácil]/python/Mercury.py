for numero in range(1, 101):
    print('{}{}'.format('fizz' if numero % 3 == 0 else '',
                        'buzz' if numero % 5 == 0 else '') or numero,
          '\n')
