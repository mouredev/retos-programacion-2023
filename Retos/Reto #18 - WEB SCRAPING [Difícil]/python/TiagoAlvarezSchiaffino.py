from bs4 import BeautifulSoup
import requests
import pandas as pd

def scrape_hola_mundo_day_schedule(url: str) -> None:
    """
    Connect to the Hola Mundo Day website, scrape and print the schedule for day 8.

    Args:
        url (str): The URL of the Hola Mundo Day website.
    """
    response = requests.get(url)

    if response.status_code == 200:
        soup = BeautifulSoup(response.content, "html.parser")
        events = soup.find_all("blockquote")
        event_info = []

        for event in events:
            span = event.find("span", {"data-slate-string": "true"})
            if span:
                event_info.append(span.text.strip())

        for info in event_info:
            print(info)

        data = pd.DataFrame({'Events for Day 8': event_info})
        data.to_csv('hola_mundo_day_schedule.csv', index=False)

    else:
        print("Error: Unable to connect to the Hola Mundo Day website")

if __name__ == "__main__":
    hola_mundo_day_url = "https://holamundo.day"
    scrape_hola_mundo_day_schedule(hola_mundo_day_url)
