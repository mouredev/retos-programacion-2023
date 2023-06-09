import datetime
import requests
import json

repo = "mouredev/retos-programacion-2023"
reqUrl = f"https://api.github.com/repos/{repo}/commits"


response = requests.get(reqUrl, data={},  headers={}).json()

logs = []
for r in response:
    commit = r.get('commit')
    datetime.datetime.strptime(commit.get('author').get(
        'date'), "%Y-%m-%dT%H:%M:%S%z").strftime("%A, %d %B %Y")
    log = {
        'author': commit.get('author').get('name'),
        'date': datetime.datetime.strptime(commit.get('author').get('date'), "%Y-%m-%dT%H:%M:%S%z")
        .strftime("%A, %d %B %Y"),
        'message': commit.get('message')
    }
    logs.append(log)


print(json.dumps(logs, indent=4))
