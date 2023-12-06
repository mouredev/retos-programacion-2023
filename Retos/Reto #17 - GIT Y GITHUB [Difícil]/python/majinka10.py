import requests
from datetime import datetime

# Acá podemos poner el link de cualquier repositorio para obtener los últimos 10 commits
repositorio = 'mouredev/retos-programacion-2023'

# Con esta URL consumo la API que me entrega los commits del respositorio
url= f'https://api.github.com/repos/{repositorio}/commits'

# Con response utilizo la libreria request para traerme la informacion (a través del método GET) de la URL y la formateo a json.
response = requests.get(url).json()

for n,commit in enumerate(response):
    hash=commit.get('sha')[:7]
    autor=commit.get('commit').get('author').get('name')

    # Con el replace quito un salto de linea que viene con el mensaje para que este se vea más bonito en una sola línea.
    mensaje=commit.get('commit').get('message').replace('\n','')

    # Con esta linea de código analizo la fecha en el formato que la entrega el JSON de GitHub para luego formatearla. strptime la analiza. Y strftime la formatea.
    fecha=(datetime.strptime(commit.get('commit').get('author').get('date'),"%Y-%m-%dT%H:%M:%SZ")).strftime("%A, %d %B %Y - %H:%M")
    
    if n<10:    
        print(f"Commit {n+1} | {hash} | {autor} | {mensaje} | {fecha}\n")