"""
/*
 * Crea un programa capaz de interactuar con un fichero TXT.
 * IMPORTANTE: El fichero TXT NO debe subirse como parte de la corrección. 
 * Únicamente el código.
 * 
 * - Si no existe, debe crear un fichero llamado "text.txt".
 * - Desde el programa debes ser capaz de introducir texto por consola y guardarlo
 *   en una nueva línea cada vez que se pulse el botón "Enter".
 * - Si el fichero existe, el programa tiene que dar la opción de seguir escribiendo
 *   a continuación o borrar su contenido y comenzar desde el principio.
 * - Si se selecciona continuar escribiendo, se tiene que mostrar por consola
 *   el texto que ya posee el fichero.  
 */
"""

try:
    file = open("text.txt","r")
    existeArchivo=True
except:
    print("No de encontro ningun archivo")
    file=open("text.txt", "x")
    existeArchivo=False

if (existeArchivo):
    resp=input("Se encontró un fichero text.txt \n ¿Continuar escribiendo?\n")
    if (resp not in ["no","No","n","N"]):
        texto_previo=file.read()
        print("--- El archivo contiene el siguiente texto ---\n")
        print(texto_previo)
        file=open("text.txt","a")
    else:    
        print("Comience a escribir en un fichero nuevo")
        file=open("text.txt","w")
while True:
    nueva_linea=input("Ingrese el texto a continuacion (escriba QUIT para salir):\n")
    if (nueva_linea=="QUIT"):
        break
    file.write(nueva_linea + "\n")
    file.flush()
file.close()



