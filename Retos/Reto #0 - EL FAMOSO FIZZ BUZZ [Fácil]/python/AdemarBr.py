for cont in range(1, 101):
    if cont % 3 == 0 and cont % 5 == 0:
        print("fizzbuzz")
    elif cont % 3 == 0:
        print("fizz")
    elif cont % 5 == 0:
        print("buzz")
    else:
        print(cont)


""" 
cont = 1

while cont <= 100:
    if (cont % 3 == 0) and  (cont % 5 == 0):
        print("fizzbuzz")
    elif (cont % 3 == 0):
        print("fizz")
    elif (cont % 5 == 0):
        print("buzz")
    else: print(cont)
    cont += 1 
"""