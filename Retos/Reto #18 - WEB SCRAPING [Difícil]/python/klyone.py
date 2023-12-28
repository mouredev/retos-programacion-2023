#!/usr/bin/env python3

import requests
from bs4 import BeautifulSoup

hello_world_info = requests.get("https://holamundo.day")
scraper = BeautifulSoup(hello_world_info.text, "lxml")

events = scraper.find_all(["h1", "blockquote"], {"data-slate-node" : "element"})

may_8th_found = False
for e in events:
    if "Agenda 8 de mayo" in e.text:
        may_8th_found = True

    if may_8th_found and e.text[0] != '>':
        print(e.text)
