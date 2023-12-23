import os

usuarios = []

def buscar_archivos_por_nombre(directorio_raiz, nombre_objetivo):
    for directorio_actual, carpetas, archivos in os.walk(directorio_raiz):
        for archivo in archivos:
            # Obtener el nombre del archivo sin la extensión
            nombre_archivo, extension = os.path.splitext(archivo)
            
            usuarios_match = list(filter(lambda usuario: usuario['username'] == nombre_archivo, usuarios))

            if(len(usuarios_match) > 0):
                usuario = usuarios_match[0]
                usuario["points"] += 1
            else:
                usuario = {
                    'username': nombre_archivo,
                    "points": 1
                }
                usuarios.append(usuario)

# Directorio raíz para comenzar la búsqueda
directorio_raiz = 'C:/Users/espinoleandroo/Code/MoureDev/retos-programacion-2023/Retos'
# Nombre del archivo objetivo (sin extensión)
nombre_objetivo = 'EspinoLeandroo'

# Llamar a la función para buscar archivos por nombre
buscar_archivos_por_nombre(directorio_raiz, nombre_objetivo)

sorted_list = sorted(usuarios, key=lambda x: x['points'], reverse=True)

ranking = 0
for user in sorted_list:
    ranking += 1
    user['ranking'] = ranking

    print(user['ranking'], " - ", user['username'], " - ", user["points"])