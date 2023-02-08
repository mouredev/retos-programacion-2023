#Reto #4: PRIMO, FIBONACCI Y PAR

"""
 * Escribe un programa que, dado un número, compruebe y muestre si es primo,
 * fibonacci y par.
 * Ejemplos:
 * - Con el número 2, nos dirá: "2 es primo, fibonacci y es par"
 * - Con el número 7, nos dirá: "7 es primo, no es fibonacci y es impar"
"""
def validate_number(number: int) -> str:
    result = ""
    count = 0

    #Validate if number is a prime number
    for i in range(1,number+1):
        if (number %i == 0):
            count += 1
   
    if count == 2:
        result += f"{number} es primo, "
    else:
        result += f"{number} no es primo"
     
    #Validate if number is into fibonacci
    l1 = 0
    l2 = 1
    fibonacci = [l1,l2]
    while l2 <= number:
        l1 = l1 + l2
        l2 = l1 + l2
        fibonacci.append(l1)
        fibonacci.append(l2)

    if number in fibonacci:
        result += ", es fibonacci "
    else:
        result += ",no es fibonacci "
    
    #Validate if number is odd or even
    if number %2 == 0:
        result += "y es par."
    else:
        result += "y es impar."

    return result


if __name__ == "__main__":
    print(validate_number(55))
