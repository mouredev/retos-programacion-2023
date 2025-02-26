num = 1

while num <= 100:
    if num % 3 == 0 and num % 5 == 0:
        print('fizz buzz\n')
    elif num % 3 == 0:
        print('fizz\n')
    elif num % 5 == 0:
        print('buzz\n')
    else:
        print(f'{num}\n')
        
    num+=1