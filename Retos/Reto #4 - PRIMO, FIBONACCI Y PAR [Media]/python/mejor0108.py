
# ```
# /*
#  * Escribe un programa que, dado un número, compruebe y muestre si es primo, fibonacci y par.
#  * Ejemplos:
#  * - Con el número 2, nos dirá: "2 es primo, fibonacci y es par"
#  * - Con el número 7, nos dirá: "7 es primo, no es fibonacci y es impar"
#  */
# ```

def is_pair (number: int) -> bool:
    return ( number % 2 == 0)

def is_prime(number: int ) -> bool:
    if ( is_pair(number) == True and number > 2):
        return False  # no es primo por ser par 
    
    for x in range(3,number):
        if ( number % x == 0):
            return False
        
    return True

def is_fibonacci(number: str) -> bool:
    
    n_1 = 1
    n_2 = 1
    while n_2 <= number:
        if n_2 == number:
            return True
        n_1, n_2 = n_2 , n_1 + n_2
        
    return False
        
def validate_pair_fibo_prime(number: int) -> None:
    
    if number < 0 :
        print('El numero debe ser mayor a 0')
        return 
    
    # 2 es primo, fibonacci y es par
    
    text_message = str(number)
    
    if is_prime(number):
        text_message = text_message + " es primo"
    else:
        text_message = text_message + " no es primo"
        
    if is_fibonacci(number):
        text_message = text_message + ", fibonacci"
    else:
        text_message = text_message + ", no es fibonacci"
    
    if is_pair(number):
        text_message = text_message + " y es par"
    else:
        text_message = text_message + " y es impar"
        
    print(text_message)

    
    
    
if __name__ == "__main__":
    validate_pair_fibo_prime(1)
    validate_pair_fibo_prime(2)
    validate_pair_fibo_prime(7)
    validate_pair_fibo_prime(8)
    validate_pair_fibo_prime(3)
    validate_pair_fibo_prime(7)
    validate_pair_fibo_prime(12)
    validate_pair_fibo_prime(17)
    validate_pair_fibo_prime(997)
    validate_pair_fibo_prime(10000)
    validate_pair_fibo_prime(55)
    validate_pair_fibo_prime(610)