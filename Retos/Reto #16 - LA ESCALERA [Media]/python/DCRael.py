def escalera(escalones: int) -> str:
        
        if escalones > 0:
            print('  '*escalones, '_')
            for i in range(escalones-1, 0, -1):
                    print('  '*i, '_|')

        elif escalones == 0:
            print(' _')
        
        else:
            print('_')
            for i in range(0, abs(escalones+1), 1):
                    print('  '*i, '|_')


try:
    escalones = int(input('Ingresa el numero de escalones: '))
    escalera(escalones)
except:
    print('Invalido vuelve a intentarlo')