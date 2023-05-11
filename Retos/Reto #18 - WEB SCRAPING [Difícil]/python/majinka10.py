import requests
from bs4 import BeautifulSoup
# Con request obtengo el contenido HTML de la pagina, luego con BeatifulSoup analizamos el contenido.

url='https://holamundo.day'
response = requests.get(url)

contenido = BeautifulSoup(response.content, 'html.parser')

# Luego de buscar en el código fuente de la pagina (con inspeccionar elemento), encontré que el id de la secccion que contiene la agenda es la siguiente. Así puedo obtener todo el contenido únicamente de esta sección.

id='section-37c93060-be70-11ed-a6a0-03f7635e8df3'

agenda=contenido.find('section',{'id':id})

# Analizando el código me di cuenta que la información de cada evento se encuentra en blockquotes, entonces, con la siguiente linea obtengo todos los blockquotes de la agenda. Pero antes de eso, los blockquotes que contienen los eventos del día 8 enstán después del segundo h1 de la sección.  

h1s=agenda.find_all('h1') # Con esta línea obtengo los h1s que hay en la sección

h1_2=h1s[1] # Con esta linea me voy al segundo h1

blockquotes=h1_2.find_next_siblings('blockquote') # Con esta linea agarro todos los blockquotes después del segundo h1

# Por último itero cada blockquote en la lista de blockquotes y con .text obtengo solo el texto.

for blockquote in blockquotes:
    print(f'{blockquote.text}\n')