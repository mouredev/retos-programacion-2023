from urllib.request import urlopen
from bs4 import BeautifulSoup

url = "https://holamundo.day"

page = urlopen(url)
html = page.read().decode("utf-8")
soup = BeautifulSoup(html, "html.parser")

box = soup.find_all("blockquote", class_= "BlockquoteElement___StyledBlockquote-sc-1dtx4ci-0 slate-BlockquoteElement notion-quote unset-width")
list = []

for l in box:
    list.append(l.text)
    
for hora in list[19:]:
        print(hora)