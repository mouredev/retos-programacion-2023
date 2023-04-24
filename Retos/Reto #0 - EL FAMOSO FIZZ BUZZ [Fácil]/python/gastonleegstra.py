for i in range(1,101):
    if i % 3 == 0:
        print("fizz")
    elif i % 5 == 0:
        print("buzz")
    elif i % 3 == 0 & i % 5 == 0:
        print('fizzbuzz')
    print(i)