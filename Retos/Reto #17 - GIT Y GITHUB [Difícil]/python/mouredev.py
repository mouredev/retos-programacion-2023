import git

commit_counter = 1

for commit in list(git.Repo(".").iter_commits())[:10]:
    print(f"Commit {commit_counter} | {commit.hexsha} | {commit.author.name} | {commit.message} | {commit.authored_datetime}".replace("\n", ""))
    commit_counter += 1