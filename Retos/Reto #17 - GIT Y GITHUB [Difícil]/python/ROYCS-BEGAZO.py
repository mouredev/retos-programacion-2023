import git

commit_counter = 0

for commit in list(git.Repo("/home/lex/Start_python/Retos_programacion").iter_commits())[:10]:
    print(f'{commit_counter}{commit.hexsha}{commit.author.name}{commit.message}{commit.authored_date}'.replace("\n", ""))
    commit_counter += 1