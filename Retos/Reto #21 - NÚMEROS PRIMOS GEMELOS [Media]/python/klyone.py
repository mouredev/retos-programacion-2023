#!/usr/bin/env python3

import math

def is_prime(n):
    max_n = int(math.sqrt(n))
    prime = True

    if n == 0 or n == 1:
        return False

    for i in range(2, max_n+1):
        if n % i == 0:
            prime = False
            break

    return prime

def is_twin_prime(n, m):
    if is_prime(n) and is_prime(m) and abs(n-m) == 2:
        return True
    else:
        return False

def get_all_twin_primes(n):
    numbers = range(n+1)
    primes = list(filter(is_prime, numbers))
    twin_primes = []
    i = 0
    j = 1

    while j < len(primes):
        if is_twin_prime(primes[i],primes[j]):
            twin_primes.append([primes[i],primes[j]])
        i = i + 1
        j = j + 1

    return twin_primes

if __name__ == "__main__":
    twin_primes = get_all_twin_primes(100)
    print(twin_primes)
