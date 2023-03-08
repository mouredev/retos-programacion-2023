for i in range(1,101):
    # Si son múltiplos de 3 y de 5 a la vez por la palabra "fizzbuzz".
    if i % 3 == 0 and i % 5 == 0:
        print('fizzbuzz')
    # Si son múltiplos de 3 por la palabra "fizz".
    elif i % 3 == 0:
        print('fizz')
    # Si son múltiplos de 5 por la palabra "buzz".
    elif i % 5 == 0:
        print('buzz')
    else: 
        print(i)
