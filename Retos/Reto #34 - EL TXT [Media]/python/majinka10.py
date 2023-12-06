opciones= ['1','2']
try: 
    text= open('text.txt','r')  
    text.close()
    eleccion = input('Escribe 1 para continuar escribiendo o 2 para sobreescribir el archivo\n')
    while eleccion not in opciones:
        eleccion = input('Escribe 1 para continuar escribiendo o 2 para sobreescribir el archivo\n')
    if eleccion == '1': 
        text = open('text.txt', 'r')
        contenido = text.read()
        print(contenido)
        text.close()
        text=open('text.txt','a')
        while True:
            texto = input('Agrega el texto o escribe exit para salir\n')
            if texto == 'exit':
                text.close()
                break
            else:
                text.write(f"{texto}\n")
    else: 
        text= open('text.txt', 'w')
        while True:
            texto = input('Agrega el texto o escribe exit para salir\n')
            if texto == 'exit':
                break
            else:
                text.write(f"{texto}\n")
except:
        text= open('text.txt', 'w')
        while True:
            texto = input('Agrega el texto o escribe exit para salir\n')
            if texto == 'exit':
                break
            else:
                text.write(f"{texto}\n")