def fizzi_buzz(num: int) -> str:
    match num:
        case num if num % 3 == 0 and num % 5 == 0:
            return "fizzi_buzz"
        case num if num % 3 == 0:
            return "fizzi"
        case num if num % 5 == 0:
            return "buzz"
        case _:
            return "el valor no es divisible por 3 o 5"


print(fizzi_buzz(3))
print(fizzi_buzz(5))
print(fizzi_buzz(15))
print(fizzi_buzz(2))
