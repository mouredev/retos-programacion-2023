
# Crea un programa capaz de interactuar con un fichero TXT.
# IMPORTANTE: El fichero TXT NO debe subirse como parte de la corrección. 
# Únicamente el código.

# - Si no existe, debe crear un fichero llamado "text.txt".
# - Desde el programa debes ser capaz de introducir texto por consola y guardarlo
#   en una nueva línea cada vez que se pulse el botón "Enter".
# - Si el fichero existe, el programa tiene que dar la opción de seguir escribiendo
#   a continuación o borrar su contenido y comenzar desde el principio.
# - Si se selecciona continuar escribiendo, se tiene que mostrar por consola
#   el texto que ya posee el fichero.  

######################################################################################
#                                                                                    #
#                                INICIO DEL PROGRAMA                                 #  
#                                                                                    #
######################################################################################


import os 

#aca voy a guardar todos los archivos que sean .txt que esten en este directorio
archivos_TXT = []

#esta funcion la voy a usar para escribir en un archivo nuevo o uno existente
def escribir(nombre_txt, tipo):
    with open(nombre_txt, tipo) as f:
        print('escribe lo que quieras presiona enterpara saltar de linea y ME QUIERO IR para salir: ')
        while(True):
            nueva_linea = input()
            if(nueva_linea == 'ME QUIERO IR'):
                break
            else:
                f.write(f'{nueva_linea} \n')
    f.close()

#esta funcion la voy a usar para leer un archivo existente 
def leer(nombre_txt, tipo):
    print('continua donde te quedaste \n')
    with open(nombre_txt, 'r') as f:
        while True:
            line = f.readline()
            if not line:
                break
            print(line.strip())
    f.close
    escribir(nombre_txt, tipo)

#listo todos los .TXT que esten en el mismo directorio 
for archivos in os.listdir():
    if ('.txt' in archivos):
        archivos_TXT.append(archivos)
if(len(archivos_TXT)>0):
    while (True):    
        abrir = input(f'Tenemos los siguientes TXT,{" ".join(map(str, archivos_TXT))} escribe el nombre de cual te gustaria abrir: ')
        try:
            leer(abrir, 'a')
            break
        except FileNotFoundError:
            print('no puedo encontrar ese archivo, y si lo intentamos de vuelta recuerda escribirlo con la extension incluida')
else: 
    print(f'parece que no tienes ningun archivo .txt aca te voy a crear uno para que empiezes')
    escribir('text.txt', 'w')
    

