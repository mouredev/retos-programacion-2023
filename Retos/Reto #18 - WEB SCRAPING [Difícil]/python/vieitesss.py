import re
import requests
from bs4 import BeautifulSoup

URL = "https://holamundo.day"
# Cadena de texto principal, desde dónde queremos empezar a obtener los datos
TARGET = "Agenda 8 de mayo"

# Obtiene los datos de la página
page = requests.get(URL)

# Busca dónde aparece el text objetivo
coincidence = re.search(f".*{TARGET}", page.text)

if coincidence:
    end = coincidence.end()
    # Si encuentra el texto, se queda únicamente con el contenido que se encuentra
    # justo después
    new_text = page.text[end:]

# Parsea el nuevo texto
soup = BeautifulSoup(new_text, "html.parser")

# Busca todos los tags "blockquote", los cuales incluyen los "span" con el texto
# que se busca
blockquotes = soup.findAll("blockquote")

for block in blockquotes:
    text = ""
    # Dentro de cada "blockquote", por cada uno de los "span" con el atributo
    # "data-slate-string" = "true", obtiene su texto y lo va encadenando
    for span in block.findAll("span", {"data-slate-string": "true"}):
        text = f"{text}{span.text}"

    print(text)
