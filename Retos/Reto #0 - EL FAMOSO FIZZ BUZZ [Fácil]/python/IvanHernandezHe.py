def FizzBuzz(limit):
    for i in range(1,limit+1):
        print("FizzBuzz" if ((i%3==0) & (i%5==0)) else "Fizz" if (i%3==0) else "Buzz" if (i%5==0) else i)
        
FizzBuzz(100)