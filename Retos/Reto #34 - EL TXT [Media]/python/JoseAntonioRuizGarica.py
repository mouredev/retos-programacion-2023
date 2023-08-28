def readFile():
    try:
        with open('text.txt', encoding='utf-8') as f:
            read_lines = f.read().splitlines()
            read_exist = True

    except FileNotFoundError:
        read_lines = []
        read_exist = False
    return read_exist, read_lines

def printLines(list_text):
    print('\n Texto introducido hasta ahora:')
    _ = [print(n) for n in list_text]
    print('-' * 25)


# Lee o crea el archivo text.text
# Devuelve un boolean de control para saber si existe o no dicho archivo
exist, lines = readFile()

# Si el archivo existe pregunta al usuario si quiere conservar la información
# Que caso de que no quiera borra el contenido
if exist:
    clean = []
    while clean not in ['S', 'N']:
        clean = input('El archivo ya existe, ¿quieres conservar su contendio? [s/n]').upper()
        if clean == 'S':
            printLines(lines)
        else:
            lines = []

# Introduce la primera línea de texto
line = input('Introduce un texto:\n')
lines.append(line)

# Comienza un loop para seguir insertando líneas hasta que lo requiera el usuario
run = True
while run:
    answer = input('¿Quieres seguir introduciendo texto? [s/n]').upper()

    # En caso afirmativo pregunta el texto y lo añade
    if answer == 'S':
        printLines(lines)
        line = input('Introduce un texto:\n')
        lines.append(line)

    # En caso negativo para la ejecución del bucle
    # Cuarda el archivo con todo lo acumulado hasta ahora
    elif answer == 'N':
        run = False
        printLines(lines)

        with open('text.txt', 'w', encoding='utf-8') as export:
            export.write('\n'.join(lines))
        print('Archivo guardado correctamente.')
    
    else:
        print('¡Error! Has introducido un valor no válido.')
