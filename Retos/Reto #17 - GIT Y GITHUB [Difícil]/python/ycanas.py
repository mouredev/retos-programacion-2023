import requests

def get_commits(n):
    OWNER = "mouredev"
    REPOSITORY = "retos-programacion-2023"
    URL = "https://api.github.com/repos/" + OWNER + "/" + REPOSITORY + "/commits?per_page=" + str(n)

    response = requests.get(URL)

    if response.status_code == 200:
        commits = response.json()

        for index, commit in enumerate(commits):
            Hash    = commit["sha"]
            Date    =  commit["commit"]["author"]["date"]
            Author  = commit["commit"]["author"]["name"]
            Message = commit["commit"]["message"]

            Message = Message.replace("\n\n", " ")

            print(f"Commit {index + 1} | {Hash} | {Author} | {Message} | {Date}", end="\n\n")

get_commits(10)
