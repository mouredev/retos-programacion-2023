
'''
 Crea una función que reciba un número decimal y lo trasforme a Octal
 y Hexadecimal.
 - No está permitido usar funciones propias del lenguaje de programación que
 realicen esas operaciones directamente.
'''
dicccionario = {10: 'A', 11: 'B', 12: 'C', 13: 'D', 14: 'E', 15:'F'}

def conversorBase(n):
    octal = ''
    hexadecimal = ''
    i = n
    j = n
    while i > 0:
        octal = str(i % 8) + octal
        i = i // 8
    while j > 0:
        if (j % 16) > 9 and (j % 16) < 16:
            hexadecimal = dicccionario[j % 16] + hexadecimal
        else:
            hexadecimal = str(j % 16) + hexadecimal
        j = j // 16
    return octal, hexadecimal


if __name__ == '__main__':
    n = int(input('Ingrese un número decimal: '))
    print(f'El número {n} en octal es {conversorBase(n)[0]}')
    print(f'El número {n} en hexadecimal es {conversorBase(n)[1]}')