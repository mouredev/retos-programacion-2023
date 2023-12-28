'''
    Muestra en la terminal una lista de números en el 
    intervalo [1, 100] separados por saltos de línea
    son reemplazados según las siguientes condiciones:
        - Múltiplos de 3  por la palabra "fizz".
        - Múltiplos de 5  por la palabra "buzz".
        - Múltiplos de 3 y de 5 a la vez por la palabra "fizzbuzz".
'''


def main():
    for numero in range(1, 100+1):
        if es_multiplo_de(3, numero) and es_multiplo_de(5, numero):
            print('fizzbuzz')
        elif es_multiplo_de(3, numero):
            print('fizz')
        elif es_multiplo_de(5, numero):
            print('buzz')
        else:
            print(numero)


def es_multiplo_de(valor: int, numero: int) -> bool:
    '''Comprueba si "numero" es multiplo de "valor".'''
    return numero % valor == 0


if __name__ == "__main__":
    main()
