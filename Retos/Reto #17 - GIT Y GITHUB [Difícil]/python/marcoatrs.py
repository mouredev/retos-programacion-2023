import requests

def main():
    res = requests.get("https://api.github.com/repos/mouredev/retos-programacion-2023/commits?per_page=10")
    if res.status_code != 200:
        return
    data: dict = res.json()
    for i, value in enumerate(data):
        hash_ = value["sha"]
        autor = value["commit"]["author"]["name"]
        message = value["commit"]["message"].split("\n")[-1]
        date = value["commit"]["author"]["date"]
        commit = f"Commit {i + 1} | {hash_} | {autor} | {message} | {date}"
        print(commit)

main()
