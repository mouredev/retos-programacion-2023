def get_prime(n: int):
    i = 2
    while i < n:
        prime = True
        for a in range(2, i):
            prime = False if i % a == 0 else True
            break
        if prime:
            yield i
        i += 1


def get_twin_primes(limit: int):
    primes = [i for i in get_prime(limit)]

    twin_primes = []
    for i in range(len(primes) - 1):
        if primes[i + 1] - primes[i] == 2:
            twin_primes.append((primes[i], primes[i + 1]))
    return twin_primes


if __name__ == "__main__":
    l = get_twin_primes(42)
    print(l)
