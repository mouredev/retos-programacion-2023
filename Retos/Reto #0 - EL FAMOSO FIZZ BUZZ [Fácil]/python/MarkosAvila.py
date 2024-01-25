#!/usr/bin/env python3
# -*- coding: utf-8 -*-


def fizzbuzz_filler(min: int, max: int) -> list:
    numbers = []
    for num in range(min, max + 1):
        if not num % 3 and not num % 5:
            num = "fizzbuzz"
        elif not num % 3:
            num = "fizz"
        elif not num % 5:
            num = "buzz"
        numbers.append(num)
    return numbers


if __name__ == "__main__":
    numbers = fizzbuzz_filler(1, 100)
    for num in numbers:
        print(num)
