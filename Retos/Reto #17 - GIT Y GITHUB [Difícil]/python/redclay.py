import requests
import bs4
from datetime import datetime
#Max x=35
def LastCommits(limit,repo):

    response = requests.get(repo)
    html = response.text
    soup = bs4.BeautifulSoup(html, 'html.parser')
    listadecommits = soup.find_all("li", {"class": "Box-row Box-row--focus-gray mt-0 d-flex js-commits-list-item js-navigation-item"})
    for x in range(limit):

            author = listadecommits[x].find(class_="commit-author user-mention")
            txtauthor = author.get_text()

            date = listadecommits[x].find("relative-time")["datetime"]
            date_obj = datetime.strptime(date, "%Y-%m-%dT%H:%M:%SZ")
            date_str = date_obj.strftime("%d/%m/%Y %H:%M")

            message = listadecommits[x].find(class_="Link--primary text-bold js-navigation-open markdown-title")
            txtmessage = message.get_text()

            hash_1 = listadecommits[x].find("clipboard-copy").get("value")
            #hash_2 = listadecommits[x].find(class_="tooltipped tooltipped-sw btn-outline btn BtnGroup-item text-mono f6").get_text()

            print(f"Commit { x + 1} | {hash_1} | {txtauthor} | {txtmessage} | {date_str}") # | {hash_2}
            
repositorio='https://github.com/mouredev/retos-programacion-2023/commits/main'

LastCommits(10,repositorio)
