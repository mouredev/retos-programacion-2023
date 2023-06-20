from bs4 import BeautifulSoup
import requests

url = "https://holamundo.day/"

page = requests.get(url)
soup = BeautifulSoup(page.content, 'html.parser')

day = soup.find_all('h1')[-2]

if day:
    print(day.text)
    next_element = day.find_next_sibling()
    while next_element is not None and next_element.name == 'blockquote':
        print(next_element.text)
        next_element = next_element.find_next_sibling()
