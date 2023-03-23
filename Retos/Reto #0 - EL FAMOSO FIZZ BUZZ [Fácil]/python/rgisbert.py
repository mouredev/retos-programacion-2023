def fizzBuzz(n):
    isMultipleOf3 = n % 3 == 0
    isMultipleOf5 = n % 5 == 0

    if (isMultipleOf3 and isMultipleOf5):
        return 'fizzbuzz'
    if (isMultipleOf3):
        return 'fizz'
    if (isMultipleOf5):
        return 'buzz'
    return n


for num in range(1, 101):
    print(fizzBuzz(num))
