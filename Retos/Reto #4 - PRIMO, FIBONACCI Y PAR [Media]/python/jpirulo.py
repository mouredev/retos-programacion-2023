def es_par(n)  -> bool:
    if n %2==0:
        return True
    else:
        return False
    

def es_primo(n) -> bool:
    is_prime = True
    for i in range(2, n):
        if n % i == 0:
            is_prime = False
    return is_prime


def es_fibo(n) -> bool:
    is_fibo = False
    a, b = 0, 1
    f_numbers = [a]
    while b <= n:
        f_numbers.append(b)
        a, b = b, a + b

    if n in f_numbers:
        return True
    
    
    

def run():
    to_evaluate=int(input("Indique numero a Evaluar.: "))
    
    if es_par(to_evaluate):
        print(f"{to_evaluate}, Es un numero Par")
    else:
        print(f"{to_evaluate}, Es Un numero Impar")
    if es_primo(to_evaluate):
        print(f"{to_evaluate}, Es un numero Primo")
    else:
        print(f"{to_evaluate}, No es Un numero Primo")
    if es_fibo(to_evaluate):
        print(f"{to_evaluate}, Es Fibbonacci")
    else:
        print(f"{to_evaluate}, No Es Fibbonacci")
        
        
        
if __name__ == "__main__":
    run()
