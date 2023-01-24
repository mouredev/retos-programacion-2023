""" 
 * Escribe un programa que, dado un número, compruebe y muestre si es primo, fibonacci y par.
 * Ejemplos:
 * - Con el número 2, nos dirá: "2 es primo, fibonacci y es par"
 * - Con el número 7, nos dirá: "7 es primo, no es fibonacci y es impar"

"""

def is_even(number: int):
    if number%2==0:
        return True
    else:
        return False
    
def is_fibonnaci(number: int):
    # 0, 1, 1, 2, 3, 5, 8, 13, 21
    list_of_number = [0,1]
    for i in range(2,2500):
        list_of_number.append(list_of_number[i-2]+list_of_number[i-1])
    if number in list_of_number:
        return True
    else:
        return False
        
def is_prime(number: int):
    count = 0
    if number > 0:
        for i in range(1,number):
            if number%i==0:
                count += 1
        if count ==2:
            return True
        else:
            return False
    else:
        return False
""" print(is_even(6))
print(is_fibonnaci(155)) """
print(is_prime(2))