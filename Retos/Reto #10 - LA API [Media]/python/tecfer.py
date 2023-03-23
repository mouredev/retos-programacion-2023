'''
Ejemlplo de petición a la Free Dictionary API. https://dictionaryapi.dev/
'''
import requests
word = "hello"
url = "https://api.dictionaryapi.dev/api/v2/entries/en/"
full_url = f"{url}{word}"

respuesta = requests.get (full_url)
print (respuesta.text)
