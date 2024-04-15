
def is_prime(number):
    if number < 1 :
        return False
    n = 2
    while number > n:
        if number % n == 0:
            return False
        n+=1
    return True

def get_primes_par(range_number):
    primes_pars = []

    for n in range(2,range_number):
        next_par = n+2
        if is_prime(n) and is_prime(next_par):
            primes_pars.append((n,next_par))
    return primes_pars

