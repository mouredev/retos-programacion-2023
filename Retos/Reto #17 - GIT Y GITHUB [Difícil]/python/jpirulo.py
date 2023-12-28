import requests
import json

class Commit:
    def __init__(self, hash, author, message, date):
        self.hash = hash
        self.author = author
        self.message = message
        self.date = date

class GitHubAPI:
    def __init__(self, owner, repo):
        self.owner = owner
        self.repo = repo
        self.url = f"https://api.github.com/repos/{owner}/{repo}/commits?per_page=10"

    def get_last_commits(self):
        response = requests.get(self.url)
        commits_json = json.loads(response.text)
        commits = []
        for commit_json in commits_json:
            hash = commit_json['sha'][:6]
            author = commit_json['commit']['author']['name']
            message = commit_json['commit']['message']
            date = commit_json['commit']['author']['date'][:-6]
            commit = Commit(hash, author, message, date)
            commits.append(commit)
        return commits

# Ejemplo de uso
github_api = GitHubAPI("Mouredev", "retos-programacion-2023")
print('Ultimos 10 Commits')

commits = github_api.get_last_commits()
for i, commit in enumerate(commits):
    print(f"Commit {i+1} | {commit.hash} | {commit.author} | {commit.message} | {commit.date}")
