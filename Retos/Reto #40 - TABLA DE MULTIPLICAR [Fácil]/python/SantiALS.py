from rich import print

def tablas(number: int) ->str:

    control = True

    while control == True:
        if  1> number or number > 10:
            print('Valor fuera de rango.')
            number = int(input('Ingrese un valor entre 1 y 10:'))
        else:
            control = False

    print(f'[bold green]*** RESULTADOS TABLA DEL "{number}" ***[bold]\n')
    
    for n in range(10):

        result = (n + 1)  * number
        print(f'[skyblue]{number} x {n + 1} = {result}')

    print('[bold yellow]--o--o--o--o--')

if __name__ == '__main__':

    tablas(int(input(f'Ingrese una tabla del 1 al 10: ')))
