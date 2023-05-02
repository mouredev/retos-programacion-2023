
import urllib.request
import json

url = "https://api.github.com/repos/mouredev/retos-programacion-2023/commits"

with urllib.request.urlopen(url) as response:
    data = json.loads(response.read().decode())
    for i, commit in enumerate(data):
        print("Commit {} | {} | {} | {} | {}".format(i+1, commit["sha"], commit["commit"]["author"]["name"], commit["commit"]["message"], commit["commit"]["author"]["date"]))