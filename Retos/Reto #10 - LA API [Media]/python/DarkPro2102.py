import requests


response = requests.get(f"https://v2.jokeapi.dev/joke/Programming?lang=es")

if response.status_code == 200:
    data = response.json()

    if data["type"] == "single":
        print("Joke: ", data["joke"])
    elif data["type"] == "twopart":
        print("Setup: ", data["setup"])
        print("Delivery: ", data["delivery"])

else:
    print("Error:", response.status_code)