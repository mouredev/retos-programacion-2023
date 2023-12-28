numeroEscalones = int(input('Ingresa el número de escalones que deseas para tu escalera: '))
if numeroEscalones == 0:
    print('__')
elif numeroEscalones > 0:
    espaciosBlancos = (numeroEscalones * 2) + 2
    cadena = ''
    for x in range(0, espaciosBlancos):
        cadena += ' '
    print(cadena + '_')
    espaciosBlancos -= 2
    while espaciosBlancos >0:
        cadena = ''
        for x in range(0, espaciosBlancos):
            cadena += ' '
        print(cadena + '_|')
        espaciosBlancos -= 2
elif numeroEscalones < 0:
    print('_')
    espaciosBlancos = 1
    maxEspaciosBlancos = ((numeroEscalones * -1) * 2) -1
    while espaciosBlancos <= maxEspaciosBlancos:
        cadena = ''
        for x in range(0, espaciosBlancos):
            cadena += ' '
        print(cadena + '|_')
        espaciosBlancos += 2
