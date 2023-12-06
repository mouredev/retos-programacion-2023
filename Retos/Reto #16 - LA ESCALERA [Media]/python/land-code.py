def dibujar_escalera(escalones: int):
    if escalones == 0:
        print('__')
    if escalones < 0:
        for x in range(abs(escalones)):
            print(2 * x * ' ' + '_|')
            
    if escalones > 0:
        for y in range(abs(escalones)):
            y = abs(escalones) - y - 1
            print(2 * y * ' ' + '_|')
dibujar_escalera(int(input()))
