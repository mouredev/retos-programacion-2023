import requests


word = str(input("What is meaning of the word: "))

url = 'https://api.dictionaryapi.dev/api/v2/entries/en/'
response = requests.get(url + word)
breakpoint()
print(response.json())
print(response)



#url = "https://pokeapi.co/api/v2/pokemon/"



#response = requests.get(url)



#response = requests.get(url)
#   print(name["name"])
  #  print(name["url"])
   # print(name) 

#pokemon="metapod"
#res_api = requests.get(url + pokemon)
#print(res_api.json())
#print(res_api)
# print(response.json()["results"])