#codigo fizzbuzz

for i in range(1, 100):
    if (i % 3 == 0 and i % 5 == 0):
        print("fizzbuzz")
    else:
        if (i % 3 == 0):
            print("fizz")
        else:
            if (i % 5 == 0):
                print("buzz")
            else:
                print(i)