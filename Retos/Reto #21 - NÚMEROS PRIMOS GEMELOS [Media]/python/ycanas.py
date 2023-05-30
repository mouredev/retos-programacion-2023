def is_prime(n):
    for number in range(2, n):
        if n % number == 0:
            return False
        
    return False if n < 2 else True


def twin_primes(n):
    prime = []
    twins = []

    for number in range(2, n + 1):
        if prime and is_prime(number) and number - prime[0] == 2:
            twins.append((prime[0], number))
            prime.clear()

        if is_prime(number):
            prime.insert(0, number)

    return twins


print(twin_primes(14))
