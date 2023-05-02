from bs4 import BeautifulSoup
import requests

url = "https://holamundo.day/"
page = requests.get(url)
soup = BeautifulSoup(page.content, "html.parser")

main = soup.find_all("blockquote", class_="BlockquoteElement___StyledBlockquote-sc-1dtx4ci-0 slate-BlockquoteElement notion-quote unset-width")

eventos = []

for i in main:
    i = i.text
    eventos.append(i)

print("EVENTOS 8 DE MAYO:\n-------------------")
for j in eventos[19:]:
    print(j)
