file = open("text.txt")
if (file):
    texto_previo=file.read()
    file.close()
    print("Se encontró un fichero text.txt \n ¿Continuar escribiendo?\n")
    resp=input()
    file=open("text.txt","w")
    if (resp not in ["no","No","n","N"]):
        file.write(texto_previo)
        print(texto_previo)
    else:    
        print("Comience a escribir en un fichero nuevo")

while True:
    print("Ingrese el texto a continuacion (escriba QUIT para salir):")
    nueva_linea=input()
    if (nueva_linea=="QUIT"):
        break
    file.write(nueva_linea + "\n")
file.close()



