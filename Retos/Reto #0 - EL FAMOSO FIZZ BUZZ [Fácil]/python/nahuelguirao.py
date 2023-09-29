def fizz_buzz():
    for num in range(1,101):
        #Conditions
        if num % 3 == 0 and num % 5 == 0:
            print("fizz_buzz")
        elif num % 3 == 0:
            print("fizz")
        elif num % 5 == 0:
            print("buzz")
        else:
            print(num)

fizz_buzz()