
def prime_number(number):
    if number == 0 or number == 1 or number == 4:
        return False
    
    for i in range(2, int(number/2)+1):
        if number % i == 0:
            return False
        
    return True

def even_number(number):
    return number % 2 == 0

def fibonacci_number(number):
    fibonacci_list = [0,1]
    a = 0
    b = 1
    c = 0
    while number > c:
        c = a + b
        a = b
        b = c
        fibonacci_list.append(c)

    return number in fibonacci_list

def get_characteristics(number):
    if prime_number(number):
        print("The number", number, "is prime", end=", ")
    else:
        print("The number", number, "is not prime", end=", ")
        
    if fibonacci_number(number):
        print("is Fibonacci", end=" and ")
    else:
        print("is not Fibonacci", end=" and ")
        
    if even_number(number):
        print("is even.")
    else:
        print("is odd.")

number = input("Enter an integer to check if it is prime, fibonacci and even/odd: ")

while number.isdigit() is False:
    number = input("Please, enter an integer: ")

get_characteristics(int(number))
