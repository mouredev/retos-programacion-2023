import requests

# make a get request to get the image
ULR = "https://api.artic.edu/api/v1/artworks?limit=2"

response = requests.get(ULR)

print(response.json()["data"][0]["artist_title"]) #Paul Gauguin