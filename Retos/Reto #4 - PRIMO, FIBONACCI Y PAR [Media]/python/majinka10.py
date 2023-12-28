import math

def is_fibonacci(n):
    if n>0:
        x,y,fib=-1,1,0
        while fib<n:
            fib=x+y
            x=y
            y=fib
        if fib==n:
            return True
        else: 
            return False
    else:
        return False

def is_prime(n):
  if n>1:
    for i in range(2,int(math.sqrt(n))+1):
        if (n%i) == 0:
            return False
    return True
  else:
      return False

def test_number(number):
    result=''
    result+= 'es primo, ' if is_prime(number) else 'no es primo, ' 
    result+= 'fibonacci ' if is_fibonacci(number) else 'no es fibonacci '
    result+= 'y es par' if number % 2 == 0 else 'y es impar'
    print(number, result)

test_number(2)
test_number(7)
test_number(0)