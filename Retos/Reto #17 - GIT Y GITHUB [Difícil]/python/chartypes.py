from git import Repo,Commit

def get_ten_repos(max_count)->list[Commit]:

    repo = Repo(search_parent_directories=True)
    commits = [
        {
            'hash':commit.hexsha,
            'author':commit.author,
            'message':commit.message,
            'date_time':commit.authored_date
        } 
        for commit in repo.iter_commits(max_count=max_count)
    ]

    return commits

print(get_ten_repos(10))
