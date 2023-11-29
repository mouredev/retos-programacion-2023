def fizz_buzz(num):
    for item in range(1,num+1):
        if item % 3 == 0 and item % 5 == 0:
            print("FizzBuzz")
        elif item % 3 == 0:
            print("Fizz")
        elif item % 5 == 0:
            print("Buzz")
        else: 
            print(item)

fizz_buzz(100)
