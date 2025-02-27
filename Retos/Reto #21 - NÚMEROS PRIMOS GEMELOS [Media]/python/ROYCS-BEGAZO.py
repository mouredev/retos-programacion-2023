def lista_prime(n : int):
    if n < 2:
        return []
    primes = [2]
    for num in range(3, n + 1, 2):
        if all(num % p != 0 for p in primes if p * p <= num):
            primes.append(num)
    return primes
def twin_primes(primes : list):
    return [(primes[i], primes[i+1]) for i in range(len(primes)-1) if abs(primes[i] - primes[i+1]) == 2]

print(twin_primes(lista_prime(14)))
