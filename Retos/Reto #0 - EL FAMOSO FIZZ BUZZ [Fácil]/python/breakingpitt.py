#!/usr/bin/env python3
# -*- coding: utf-8 -*-

FIZZBUZZ = "FizzBuzz"
FIZZ = "Fizz"
BUZZ = "Buzz"

def fizzbuzz(limit):
    for number in range(1, limit + 1):
        divisible_by_3 = number % 3 == 0
        divisible_by_5 = number % 5 == 0

        if divisible_by_3 and divisible_by_5:
            print("FIZZBUZZ")
        elif divisible_by_3:
            print("FIZZ")
        elif divisible_by_5:
            print("BUZZ")
        else:
            print(number)

limit = 100
fizzbuzz(limit)
