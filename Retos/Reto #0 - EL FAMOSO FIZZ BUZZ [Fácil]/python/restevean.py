"""
 Write a function that a list of numbers from 1 to 100, replacing:
    - Multiples of 3 by the word "fizz".
    - Multiples of 5 by the word "buzz".
    - Multiples of 3 and 5 by the word "fizzbuzz".
"""


def fizzbuzz_1():
    numbers = []
    for num in range(1, 101):
        if num % 3 == 0 and num % 5 == 0:
            numbers.append("fizzbuzz")
        elif num % 3 == 0:
            numbers.append("fizz")
        elif num % 5 == 0:
            numbers.append("buzz")
        else:
            numbers.append(num)

    return numbers


def fizzbuzz_2():
    for i in range(1, 101):
        if i % 3 == 0 and i % 5 == 0:
            print("fizzbuzz")
        elif i % 3 == 0:
            print("fizz")
        elif i % 5 == 0:
            print("buzz")
        else:
            print(i)


if __name__ == "__main__":
   print(fizzbuzz_1())
   fizzbuzz_2()
