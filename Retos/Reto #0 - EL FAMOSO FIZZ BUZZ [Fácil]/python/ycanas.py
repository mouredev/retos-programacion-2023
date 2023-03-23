def fizz_buzz(n):
    for i in range(1, n+1):
        by_three = i%3 == 0
        by_five  = i%5 == 0

        if by_three and by_five:
            print("fizzbuzz")
        
        elif by_three:
            print("fizz")

        elif by_five:
            print("buzz")

        else:
            print(i)

fizz_buzz(100)
