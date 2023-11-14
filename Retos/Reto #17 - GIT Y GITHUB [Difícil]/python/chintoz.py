import git
import pathlib

if __name__ == '__main__':
    repo = git.Repo(pathlib.Path(__file__).parent.resolve(), search_parent_directories=True)
    commits = list(repo.iter_commits(repo.active_branch, max_count=10))
    for i in range(len(commits)):
        to_print = "Commit " + str(i + 1) + " | "
        to_print = to_print + commits[i].hexsha + " | "
        to_print = to_print + commits[i].author.name + " | "
        to_print = to_print + commits[i].message.splitlines()[0] + " | "
        to_print = to_print + str(commits[i].committed_datetime)
        print(to_print)

