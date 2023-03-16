for counter in range (1,101):
    if (counter%3 == 0) and (counter%5 == 0):
        print ("fizzbuzz")
    elif counter%3 == 0:
        print ("fizz")
    elif counter%5 == 0:
        print ("buzz")
    else:
        print (counter)
