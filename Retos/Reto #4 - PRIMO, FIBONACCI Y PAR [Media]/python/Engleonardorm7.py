"""Escribe un programa que, dado un número, compruebe y muestre si es primo,
 * fibonacci y par.
 * Ejemplos:
 * - Con el número 2, nos dirá: "2 es primo, fibonacci y es par"
 * - Con el número 7, nos dirá: "7 es primo, no es fibonacci y es impar"""


def fibonacci(number):
    f1=0
    f2=1
    f3=0
    while f3<=number:
        f3=f1+f2
        f1=f2
        f2=f3
        if f3==number:
            return True
    return False

def prime(number):
    count=0
    for i in range(1,number+1):
        if number%i==0:
            count+=1
    if count ==2:
        return True
    else:
        return False
        
def even(number):
    if number%2==0:
        return True
    else:
        return False

if __name__=="__main__":
    number=int(input("Type a number"))
    if fibonacci(number):
        print("The number is fibonacci")
    else:
        print("The number is not fibonacci")

    if prime(number):
        print("The number is prime")
    else:
        print("The number is not prime")
        
    if even(number):
        print("The number is even")
    else:
        print("The number is odd")