sequence = 1

while sequence < 101:
    if sequence % 3 == 0 & sequence % 5 == 0:    
        print("fizzbuzz")
    elif sequence % 3 == 0:
        print("fizz")
    elif sequence % 5 == 0:
        print("buzz")
    else:
        print(sequence)
    sequence = sequence + 1
