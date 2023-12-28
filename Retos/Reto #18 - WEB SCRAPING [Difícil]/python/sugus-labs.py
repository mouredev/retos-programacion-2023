import pandas as pd
from bs4 import BeautifulSoup
import requests
import re
import string

def download_events_from(url):

    body = requests.get(url)
    body_text = body.content
    #print(body)
    #print(body_text)

    clean = re.compile('<.*?>')

    alphabet_dict = dict()

    soup = BeautifulSoup(body_text, 'lxml')
    section = soup.find("section", 
        id = "section-37c93060-be70-11ed-a6a0-03f7635e8df3")
    div = section.find("div", 
        class_ = "notion-page-content")
    blockquotes = section.find_all("blockquote")
    calendar_list = []
    for blockquote in blockquotes:
        calendar_list.append(re.sub(clean, '', str(blockquote)))
    second_day_start_idx = 0
    last_hour = 0
    for num, row in enumerate(calendar_list):
        curr_hour = int(row[0:2])
        if last_hour > curr_hour:
            second_day_start_idx = num
            break
        last_hour = curr_hour
    second_day_calendar_list = calendar_list[second_day_start_idx:]
    return second_day_calendar_list

            
if __name__ == "__main__":
    
    url = "https://holamundo.day/"
    second_day_calendar_list = download_events_from(url)
    for event in second_day_calendar_list:
        print(event)