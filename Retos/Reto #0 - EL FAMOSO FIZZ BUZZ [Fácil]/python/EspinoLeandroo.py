def is_multiple_of_3_function(n):
    #A number is divisible by 3 if the sum of its digits is a multiple of 3.
    number = str(n)
    sum = 0
    for element in number:
        sum += int(element)
    return sum % 3 == 0

def is_multiple_of_5_function(n):
    #A number is divisible by 5 if it ends in 0 or 5.
    number = str(n)
    last_digit = number[-1]
    return (last_digit == '5' or last_digit == '0')


for i in range(100):
    is_multiple_of_3 = is_multiple_of_3_function(i)
    is_multiple_of_5 = is_multiple_of_5_function(i)
    
    if(is_multiple_of_3 and is_multiple_of_5):
        print("fizzbuzz")
    elif(is_multiple_of_3):
        print("fizz")
    elif(is_multiple_of_5):
        print("buzz")
    else:
        print(i)
