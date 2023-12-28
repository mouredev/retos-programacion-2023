import math

def check(number):
    result = ""

    # Check if this is prime:
    if number > 1:
        for value in range(2, number):
            if number % value == 0:
                result += "No es primo, "
                break
        else:
            result += "Es primo, "
    else:
        result += "No es primo "

    # Check if this is part of the fibonacci series
    result += "es fibonacci, " if isFibo(number) else "no es fibonacci, " 
    
    # Check if this is even
    result += "es par." if number % 2 == 0 else "es impar."

    print(result)
        
def isPerfectSquare(number):
    square = math.sqrt(number)
    return square * square == number

def isFibo(number):
    return isPerfectSquare(5*number*number + 4) or isPerfectSquare(5*number*number - 4)


if __name__ == '__main__':
   
   number = int(input('Type a number: '))
   check(number)