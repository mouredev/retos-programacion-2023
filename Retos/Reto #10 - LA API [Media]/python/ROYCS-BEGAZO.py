import requests

url = 'https://api.spacexdata.com/v4/launches/latest'

response = requests.get(url)

if response.status_code == 200:
    data = response.json()
    if data['success']:
        estado = 'exitoso'
    else:
        estado = 'fallido'
    print(f'lanzamiento: {data['name']}, detalles : {data['details']}, estado {estado} Fecha: {data['date_utc']}')