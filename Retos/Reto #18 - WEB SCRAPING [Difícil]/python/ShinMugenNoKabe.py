from bs4 import BeautifulSoup
import requests

request = requests.get("https://holamundo.day/")
scrap = BeautifulSoup(request.content, "html.parser")


blockquotes = scrap.find_all("blockquote", attrs={"class", "BlockquoteElement___StyledBlockquote-sc-1dtx4ci-0 slate-BlockquoteElement notion-quote unset-width"})

for block in blockquotes[21:]:
    print(block.text)