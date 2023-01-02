#!/usr/bin/env python3

def is_divisible_by_three(num):
    if num % 3 == 0:
        return True
    else:
        return False

def is_divisible_by_five(num):
    if num % 5 == 0:
        return True
    else:
        return False

def is_divisible_by_three_and_five(num):
    return is_divisible_by_three(num) and is_divisible_by_five(num)

def process_number(num):
    if is_divisible_by_three_and_five(num):
        return "fizzbuzz"
    if is_divisible_by_three(num):
        return "fizz"
    if is_divisible_by_five(num):
        return "buzz"
    return str(num)

if __name__ == "__main__":
    for i in range(1,101):
        print(process_number(i))
