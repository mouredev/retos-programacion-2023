import git

repoCloned = git.Repo("retos-programacion-2023")

print(repoCloned.git.log())
