from git import Repo
import datetime
import pandas as pd

def retrieve_last_commits():
    repo = Repo()
    last_commits = list(repo.iter_commits("main", max_count = 10))
    column_name_list = ["hash", "author", "message", "date"]
    data_list = []
    for commit in last_commits:
        hash = str(commit)[:8]
        author = commit.author
        message = commit.message.replace("\n", "")
        date = datetime.datetime.fromtimestamp(commit.committed_date)
        data_list.append([hash, author, message, date])
        #print(hash, author, message, date)
    commit_df = pd.DataFrame(
        columns = column_name_list,
        data = data_list)    
    return commit_df
            
if __name__ == "__main__":
    
    commit_df = retrieve_last_commits()
    print(commit_df)