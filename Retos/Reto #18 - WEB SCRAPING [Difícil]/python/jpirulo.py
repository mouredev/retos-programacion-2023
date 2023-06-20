import requests
from bs4 import BeautifulSoup


class HolaMundoDayScraper:
    def __init__(self, url):
        self.url = url
        self.events = []

    def scrape_day_8_agenda(self):
        response = requests.get(self.url)
        soup = BeautifulSoup(response.content, 'html.parser')

        events_blockquotes = soup.find_all('blockquote', class_='BlockquoteElement___StyledBlockquote-sc-1dtx4ci-0 slate-BlockquoteElement notion-quote unset-width')

        for blockquote in events_blockquotes:

            self.events.append(blockquote.text)

    def print_day_8_agenda(self):
        print('Agenda para el día 8:')
        for event in self.events[19:]:
            print(event)




scraper = HolaMundoDayScraper('https://holamundo.day/')
scraper.scrape_day_8_agenda()
scraper.print_day_8_agenda()
