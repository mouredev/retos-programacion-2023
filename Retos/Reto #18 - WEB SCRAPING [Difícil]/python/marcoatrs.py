import requests
from bs4 import BeautifulSoup

url = "https://holamundo.day"
page = requests.get(url)
soup = BeautifulSoup(page.content, "html.parser")
title = soup.find_all(string=" Agenda 8 de mayo | ")[0].find_parent("h1")
for blockequote in title.find_all_next("blockquote"):
    print(blockequote.get_text())
