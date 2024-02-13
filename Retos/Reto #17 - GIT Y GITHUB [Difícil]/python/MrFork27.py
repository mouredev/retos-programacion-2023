from git import Repo


def show_last_commits():
    COMMITS_NUMBER = 10

    try:
        repository = Repo(search_parent_directories=True)
        previous_commits = list(
            repository.iter_commits(all=True, max_count=COMMITS_NUMBER)
        )

        for i in range(COMMITS_NUMBER):
            hash = previous_commits[i]
            author = previous_commits[i].author
            message = previous_commits[i].message
            date = previous_commits[i].committed_datetime

            print(f"Commit {i+1} | {hash} | {author} | {message} | {date}")
    except Exception as error:
        print("¡Ha ocurrido un error!")
        print(error)


show_last_commits()
