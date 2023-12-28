fizz_str = "fizz"
buzz_str = "buzz"

def fizz_buzz(
    start_num: int = 0, 
    stop_num: int = 100,
    fizz_str: str = fizz_str,
    buzz_str: str = buzz_str):
    
    """ Fizz Buzz function """
    
    for num in range (start_num, stop_num + 1):
        if num % 3 == 0 and num % 5 == 0:
            print(num, fizz_str + buzz_str)
        elif num % 3 == 0:
            print(num, fizz_str)
        elif num % 5 == 0:
            print(num, buzz_str)    
            
if __name__ == "__main__":
    fizz_buzz(1, 100)