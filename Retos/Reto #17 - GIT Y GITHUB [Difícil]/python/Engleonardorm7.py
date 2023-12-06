from github import Github

g = Github("pon tu access token aqui...")
repo = g.get_repo("mouredev/retos-programacion-2023")

commits = repo.get_commits()[:10]

for i, commit in enumerate(commits):
    sha = commit.sha[:7]
    author = commit.commit.author.name
    message = commit.commit.message
    date = commit.commit.author.date.strftime("%d/%m/%Y %H:%M")
    print(f"Commit {i+1} | {sha} | {author} | {message} | {date}")
