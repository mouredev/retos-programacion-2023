from bs4 import BeautifulSoup
import requests

def get_data():
    url = "https://holamundo.day"
    response = requests.get(url).content

    bs = BeautifulSoup(response, "html.parser")
    blockquotes = bs.find_all("blockquote")

    return blockquotes[21:]


data = get_data()

for event in data:
    print(event.text)
