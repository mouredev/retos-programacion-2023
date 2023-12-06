import bs4
import requests

url = 'https://holamundo.day'


def Web_scrappling(url):

    web = requests.get(url)
    agenda = {}

    soup = bs4.BeautifulSoup(web.content, 'html.parser')

    allresults = soup.find_all('blockquote')
    dates = []
    for result in allresults:
        dates.append(result.text)

    for act in dates[13:]:
        print(act)


Web_scrappling(url)
