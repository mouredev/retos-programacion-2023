def printTable(number: int) -> None:
    print(f'Tabla de multiplacar del número {number}')
    for n in range(1, 11):
        print(f'{number} x {n} = {number * n}')
    
if __name__=='__main__':
    run = True
    while run:
        number_table = input('Introduce un número: ')
        if number_table.isnumeric():
            printTable(number=int(number_table))
            run = False
        else:
            print('Error: No has introducido un múmero')
