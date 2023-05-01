from github import Github

# Access the repository
g = Github("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")
repo = g.get_repo("mouredev/retos-programacion-2023")

# Get the last 10 commits
commits = repo.get_commits()[:10]

# Display commit information
for i, commit in enumerate(commits):
    sha = commit.sha[:7]
    author = commit.commit.author.name
    message = commit.commit.message
    date = commit.commit.author.date.strftime("%d/%m/%Y %H:%M")
    print(f"Commit {i+1} | {sha} | {author} | {message} | {date}")
