def test_math_chars(num: int = 13):
    
    """ Test prime, fibonaccion and even number function """
    
    def is_even(num: int) -> bool:
        return (num % 2 == 0)
    
    def is_prime(num: int) -> bool:
        is_prime = True
        for n in range(2, num):
            #print(n)
            if num % n == 0:
                #print("p:", n)
                is_prime = False
                break
        return is_prime
    
    def is_fibonacci(num: int) -> bool:
        last_num = 0
        curr_num = 1
        fibo_list = [0, 1]
        while curr_num < num:
            fibo_num = curr_num + last_num
            fibo_list.append(fibo_num)
            last_num = curr_num
            curr_num = fibo_num            
            #print(fibo_list)
        return(num in fibo_list)
            
    even = is_even(num)
    prime = is_prime(num)   
    fibo = is_fibonacci(num)
    
    print(f"The number {num}\n- even: {even}\n- prime: {prime}\n- fibo: {fibo}") 
           
if __name__ == "__main__":
    test_math_chars(8)