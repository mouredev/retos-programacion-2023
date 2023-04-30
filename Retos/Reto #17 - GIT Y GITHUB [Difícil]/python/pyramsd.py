import git
import pathlib

if __name__ == '__main__':
    repo = git.Repo(pathlib.Path(__file__).parent.resolve(), search_parent_directories=True)
    commits = list(repo.iter_commits(repo.active_branch, max_count=10))
    for i in range(len(commits)):
        to_print = "Commit " + str(i + 1) + " : " + commits[i].hexsha + " \n Autor: " + commits[i].author.name + " \n Mensaje: " + commits[i].message.splitlines()[0] + " \n Fecha y hora: " + str(commits[i].committed_datetime) + "\n"
        print(to_print)
        
