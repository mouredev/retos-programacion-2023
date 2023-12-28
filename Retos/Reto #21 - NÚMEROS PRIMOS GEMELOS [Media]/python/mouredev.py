def is_prime(number: int) -> bool:
    
    if number <= 1:
        return False
    
    for index in range(2, number):
        if number % index == 0:
            return False

    return True

def find_prime_twins(range_number: int):
    for index in range(2, range_number):
        if index + 2 < range_number and is_prime(index) and is_prime(index + 2):
            print(f"({index}, {index + 2})")

find_prime_twins(14)
print("")
find_prime_twins(43)
print("")
find_prime_twins(44)