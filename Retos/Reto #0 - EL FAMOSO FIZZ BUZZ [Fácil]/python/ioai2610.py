n = range(1,101,1)
for x in n:
    if (x % 3 == 0) & (x % 5 ==0):
        x = 'fizzbuz'
    elif x % 5 == 0:
        x = 'buzz'
    elif x % 3 == 0:
        x = 'fizz'
    print(x)