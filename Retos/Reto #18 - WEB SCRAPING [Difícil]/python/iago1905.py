from bs4 import BeautifulSoup
import requests

url = "https://holamundo.day"

page = requests.get(url)

if page.status_code == 200:
    soup = BeautifulSoup(page.content, "html.parser")
    resultados = []
    blockquotes = soup.find_all("blockquote")
    for blockquote in blockquotes:
        resultados.append(blockquote.text)
    resultados = resultados[resultados.index("16:00 | Bienvenida"):]
    print("\n".join(resultados))
