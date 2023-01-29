import math

def checkNumber(number):
    isPrime = True
    isFibonacci = False
    isEven = False
    
    for i in range(2, number):
        if number % i == 0:
            isPrime = False
            break


    print("Es un número primo" if isPrime else "No es un número primo")
    
    
    firstDifferenceSquare = round(math.sqrt(5 * number * number + 4))
    secondDifferenceSquare = round(math.sqrt(5 * number * number - 4))
    
    isFibonacci = firstDifferenceSquare * firstDifferenceSquare == (5 * number * number + 4) or  secondDifferenceSquare * secondDifferenceSquare == (5 * number * number - 4)
    print("Es un número de fibonacci" if isFibonacci else "No es un número de fibonacci")
    
    
    
    if (number % 2 == 0): 
        isEven = True
    
    print("Es un número par" if isEven else "No es un número par")        


checkNumber(22)

