'''
Todo llega a su fin... Este es el último reto de programación 
semanal de 2023.
Crea un programa que muestre un listado calculado en tiempo real
con todos los usuarios que han resuelto algún reto de programación
de este año.
- El listado debe estar ordenado por el número de ejercicios resueltos
  por cada usuario (y mostrar ese contador al lado de su nombre).
- También se debe de mostrar el número de usuarios que han participado
  y el número de correcciones enviadas.
Muchísimas gracias por ayudar a crear este gran recurso
para la comunidad... ¡Prepárate para 2024!   
'''
import os

usuarios = {}
ejercicios = 0

start_path = os.path.dirname(__file__)
start_path = os.path.abspath(os.path.join(start_path, os.pardir, os.pardir))

for ruta_actual, carpetas, archivos in os.walk(start_path):
    for archivo in archivos:
        if archivo not in ['language_stats.py', 'ejercicio.md']:
            ejercicios += 1
            usuario = archivo.split('.')[0]
            if usuario in usuarios:
                usuarios[usuario] += 1
            else:
                usuarios[usuario] = 1

usuarios_ordenados = sorted(usuarios.items(), key=lambda x: x[1], reverse=True)

print(f'Número de correcciones enviadas: {ejercicios}')
print(f'Número de usuarios participantes: {len(usuarios)}')
print(f'Ranking de participantes (TOP 50): ')
for index, usuario in enumerate(usuarios_ordenados):
    if index < 50:
        print(f' - {index + 1} {usuario[0]}: {usuario[1]}')