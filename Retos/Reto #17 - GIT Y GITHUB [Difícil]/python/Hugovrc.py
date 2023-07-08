import git
import os

# directorio actual
dir = os.getcwd()
# Esta linea te manda al directorio anterior(un directorio atras)
dir = os.chdir("..")
repo = git.Repo(dir)

commits = list(repo.iter_commits(max_count=10))

for commit in commits:
    print("Hash: {}".format(commit.hexsha)+ " | " "Autor: {}".format(commit.author.name)+ " | " "Mensaje: {}".format(commit.message)+ " | " "Fecha y Hora: {}".format(commit.committed_datetime)+"\n")