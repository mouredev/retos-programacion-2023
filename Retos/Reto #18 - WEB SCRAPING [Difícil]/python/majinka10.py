import requests
from bs4 import BeautifulSoup
# Con request obtengo el contenido HTML de la pagina, luego con BeatifulSoup analizamos el contenido.

url='https://holamundo.day'
response = requests.get(url)

contenido = BeautifulSoup(response.content, 'html.parser')

# Luego de buscar en el código fuente de la pagina (con inspeccionar elemento), encontré que el id de la secccion que contiene la agenda del día 8 es la siguiente. Así puedo obtener todo el contenido únicamente de esta sección.

id='section-37c93060-be70-11ed-a6a0-03f7635e8df3'

agenda=contenido.find('section',{'id':id})

# Analizando el código me di cuenta que la información de cada evento se encuentra en blockquotes, entonces, con la siguiente linea obtengo todos los blockquotes de la agenda

blockquotes=agenda.find_all('blockquote')

# Por último itero cada blockquote en la lista de blockquotes y con .text obtengo solo el texto.

for blockquote in blockquotes:
    print(f'{blockquote.text}\n')