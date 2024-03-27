import os

# Ruta del archivo actual
ruta_del_script = os.path.dirname(__file__).split('/')
ruta = '/'.join(ruta_del_script[:-2]) # Me devuelvo dos carpetas para llegar a ../../Retos

users = {}
correciones = 0

for files in os.walk(ruta):
    for usuario in files[2]:
        if usuario not in ["ejercicio.md", "language_stats.py", ".ds_store", ".gitignore"]:
            usuario = usuario.split('.')[0].lower() 
            users[usuario] = users.get(usuario, 0) + 1 # Obtengo el usuario del diccionario y le sumo uno al valor que tenga.
            # el 0, es el caso default, en el ejemplo de que sea la primera vez que se inserta.
            correciones += 1
           
# Como el diccionario funciona de forma tal que se ordena
# a medida que se insertan elementos. (es decir, como una pila)
# hay que crear otro diccionario con la regla de que ordene los elementos
# del primer diccionario

sorted_users = {key: valor for key, valor in sorted(users.items(), key=lambda item: item[1], reverse=True)}

print(f'Número de usuarios únicos: {len(users)}')
print(f"Número de correcciones enviadas: {correciones}")
print("Ranking de usuarios por número de correcciones:")
for position, usuario in enumerate(sorted_users):
     if position < 20:
          print(f"{position+1}. {usuario}: {sorted_users[usuario]}")