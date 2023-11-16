from bs4 import BeautifulSoup
import requests

blockquotes = BeautifulSoup(requests.get(
    "https://holamundo.day").content).find_all("blockquote")

for blockquote in blockquotes[21:]:
    print(blockquote.text)