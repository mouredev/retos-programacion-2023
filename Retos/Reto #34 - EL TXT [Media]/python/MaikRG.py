import os

nombre_fichero = 'text.txt'


def mostrar_fichero():
    try:
        with open(nombre_fichero,'r') as fichero:
            print(f'[*] Contenido de {nombre_fichero}: ')
            print(fichero.read())
    except:
        print(f'El fichero "{nombre_fichero}" no existe')
        
def añadir_linea_fichero(modo_apertura):
    x = input("Inserta una nueva línea: ")
    with open(nombre_fichero,modo_apertura) as fichero:
        fichero.write(x+'\n')
        
        
        
        
        
        
        
        
if os.path.exists(nombre_fichero):
    res = input(f'[*] El "{nombre_fichero}" fichero ya existe, desea borrarlo y generarlo de nuevo? Y/N'+'\n')
    if res == 'Y':
        añadir_linea_fichero('w') # Borra y crea de nuevo
        mostrar_fichero()
    elif res == 'N':
        añadir_linea_fichero('a') # Añade nueva línea al final
        mostrar_fichero()
    else:
        print("ERROR: Respuesta incorrecta.") 
else:
    añadir_linea_fichero('a')    
    mostrar_fichero()
    
    
    
    