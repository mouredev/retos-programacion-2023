import requests
import json

url = 'https://api.github.com/repos/mouredev/retos-programacion-2023/commits'
response = requests.get(url)
commits = json.loads(response.text)

variable = 0
for commit in commits[:10]:

    variable+= 1
    hash = commit['sha']
    author = commit['commit']['author']['name']
    message = commit['commit']['message']
    message = message.replace("\n", " ")
    date = commit['commit']['author']['date']

    print(f'Commit {variable} | {hash} | {author} | {message} | {date}')

