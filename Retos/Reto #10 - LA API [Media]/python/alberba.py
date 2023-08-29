import requests
import json

def random_BreakingBad_quotes():
    url = "https://api.breakingbadquotes.xyz/v1/quotes"

    response = requests.get(url)
    dict_quotes = json.loads(response.content)[0]
    print()
    print(f'Cita: {dict_quotes["quote"]}')
    print(f'Autor: {dict_quotes["author"]}')
    print()

random_BreakingBad_quotes()