'''
# Reto #14: Octal y Hexadecimal
#### Dificultad: Fácil | Publicación: 03/04/23 | Corrección: 10/04/23

## Enunciado

```
/*
 * Crea una función que reciba un número decimal y lo trasforme a Octal
 * y Hexadecimal.
 * - No está permitido usar funciones propias del lenguaje de programación que
 * realicen esas operaciones directamente.
 */
```
#### Tienes toda la información extendida sobre los retos de programación semanales en **[retosdeprogramacion.com/semanales2023](https://retosdeprogramacion.com/semanales2023)**.

'''




def to_hexadecimal(number:int)->str:

    def get_letter(number:str)->str:
        letters:list = ['A','B','C','D','E','F']
        position = number[1]
        return letters[int(position)]

    quotient:int = 1
    remainder:int = 0
    result_container:list = []
    hex_number: str = ''

    while quotient != 0:
        remainder = number % 16
        quotient = number//16
        if remainder >= 10:
            result_container.append(get_letter(str(remainder)))
        else:
            result_container.append(str(remainder)) 

        number = quotient

    result_container.reverse()
    for n in result_container:
        hex_number+=str(n)

    return hex_number


def to_octal(number:int)->str:

    remainder:int = 2
    quotient:int = 0
    whole_number:list[int]=[]
    result:int|str = ''

    while remainder > 1:
        quotient = number // 8
        remainder = number - ( quotient * 8 ) 
        whole_number.append(remainder)

        number = quotient

    whole_number.reverse()
    for n in whole_number:
        result += str(n)
    return result

def to_octal_and_hexadecimal(number:int)-> str:
    '''
    example: to_octal_and_hexadecimal(4730) -> octal number: 1332 , hex number : 2DA
    '''

    hex_number = to_hexadecimal(number)
    octal_number = to_octal(number)

    

    return f'octal number: {octal_number}, and hexadecimal number: {hex_number} '


print(to_octal_and_hexadecimal(730))
print(to_octal_and_hexadecimal(179))
