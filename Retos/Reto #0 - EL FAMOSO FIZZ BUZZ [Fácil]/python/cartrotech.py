# fizz buzz

for i in range(100):

    result = ''
    if (i+1)%3 == 0 and (i+1)%5 == 0:
        result = 'fizzbuzz'

    elif (i+1)%3 == 0:
        result = 'fizz'

    elif (i+1)%5 == 0:
        result = 'buzz'

    else:
        result = str(i+1)

    print(result)

