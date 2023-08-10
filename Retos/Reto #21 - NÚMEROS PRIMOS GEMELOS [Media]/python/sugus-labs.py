import math

def twin_primes(num_max):
    
    is_prime = True
    prime_list = []
    
    for num in range(2, num_max):
        is_prime = True
        for pos in range(2, num):
            if num % pos == 0:
                is_prime = False
                break
        if is_prime:
            prime_list.append(num)
    
    twin_prime_list = []
    for iter in range(0, len(prime_list)):
        try:
            if prime_list[iter + 1] - prime_list[iter] == 2:
                twin_prime_list.append((prime_list[iter],prime_list[iter + 1]))       
        except:
            break
        
    return twin_prime_list
            
if __name__ == "__main__":
    
    num_max = 14
    twin_prime_list = twin_primes(num_max)
    print(twin_prime_list)

