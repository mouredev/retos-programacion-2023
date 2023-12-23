def fizzbuzz():
    """
    Print numbers from 1 to 100, replacing multiples of 3 with "fizz",
    multiples of 5 with "buzz", and multiples of both with "fizzbuzz".
    """
    for number in range(1, 101):
        if number % 15 == 0:  # Check if the number is a multiple of both 3 and 5
            print("fizzbuzz")
        elif number % 3 == 0:  # Check if the number is a multiple of 3
            print("fizz")
        elif number % 5 == 0:  # Check if the number is a multiple of 5
            print("buzz")
        else:
            print(number)

fizzbuzz()
